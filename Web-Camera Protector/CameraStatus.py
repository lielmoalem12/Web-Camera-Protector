#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 25/01/2016                                               #
# Name: CameraStatus                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.6 64-bit                             #
# Python Environment  : PyCharm                                  #
##################################################################
"""
#endregion

#region Imports
from win32com.client import GetObject
import os
import ctypes
import sys
#endregion

#region Constants
DEVICE_NAME = "USB Video Device"
HANDLE_EXE_PATH = r"C:/Handle.exe"
PROCESS_TERMINATE = 1
#endregion

class  CameraStatus:
    def __init__(self):  #Constructor
        self.physical_device_object_name = ""
        self.process_name = ""
        self.process_id = -999
        self.status = ""
        self.processDict = {}
        self.executable_path = ""
        self.exe_size = ""



    #Change to get from server
    def Get_Classification(self, process_name):
        return 0

    def Get_Camera_Status(self):

            #try:
                print 'Searching video device. Please wait..'

                self.wmi = GetObject('winmgmts:')
                self.get_physical_device_object_name()
                # 2 -- Camera connected but not in use  1 -- Camera is on   0 -- Disconnected

                if not self.physical_device_object_name:  #if device not connected
                    self.status = '0'  #return 0
                    print "Camera was not found, check the help file to find some possible solutions"
                    return self.status
                processes = self.wmi.InstancesOf('Win32_Process')

                for process in processes:  #for every process:
                    handlers = self.get_handlers(process.Properties_('Name').Value) #finds handlers
                    if handlers.find(self.physical_device_object_name) > -1: #checks if any are the webcam
                        self.process_name = (process.Properties_('Name').Value) #if do save process name
                        self.process_id = process.Properties_('ProcessId').Value #save process id
                        self.processDict[self.process_name] = self.Get_Classification(self.process_name)
                        self.executable_path = process.Properties_('ExecutablePath').Value
                        self.exe_size = self.Get_Exe_size(self.executable_path)
                        self.exe_size = unicode(self.exe_size, 'utf-8')
                        if self.processDict[self.process_name] == 2:
                            self.KillProcess(self.process_id)
                        break


                print self.processDict
                if self.process_name:
                    self.status = '1'
                    print "Camera was found and in use"
                else: #if the camera is connected but not in a process save status = 2
                    self.status = '2'
                    print "Camera was found but not in use"
                print self.status

                return self.status

            #except Exception as detail:
                #print 'run-time error : ', detail
    def Get_Exe_size(self, path):
        print os.path.getsize(str(self.executable_path))
        return str(os.path.getsize(str(self.executable_path)))


    def get_handlers(self, processName):#returns handlers for process
         return os.popen(HANDLE_EXE_PATH + " -a -p " + processName).read()

    def get_physical_device_object_name(self): #finds physical device name for camera (USB video device)
        video_name = None
        for serial in self.wmi.InstancesOf("Win32_PnPSignedDriver"):
            #print (serial.Name, serial.Description)
            if serial.Description and DEVICE_NAME in serial.Description:
                video_name = serial.Description
                break

        if video_name:
            self.physical_device_object_name = os.popen("wmic path Win32_PnPSignedDriver where \"devicename like '" + video_name + "'\" get pdo").read()

            self.physical_device_object_name = self.physical_device_object_name.split('\r\n')[1]
            self.physical_device_object_name = self.physical_device_object_name.strip(' ')
            print self.physical_device_object_name
        else:
            self.physical_device_object_name = None

    def KillProcess(self, pid):
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)

# -*- coding: utf-8 -*-
# region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 31/01/2016                                               #
# Name: CameraStatus                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.6 64-bit                             #
# Python Environment  : PyCharm                                  #
##################################################################
"""
# endregion

# region ---- Imports ----
import sqlite3
#endregion

class DataBase:
    #region ---- Table creating functions ----
    def __init__(self):  #Constructor
        self.database = sqlite3.connect("database.db")
        self.table_dict = {"Clients": "Client_name", "Classification": "Classification_ID"}
        try:
            self.create_classification_table()
            self.create_clients_table()
        except:
            pass

    def create_clients_table(self):
        self.database.execute('''CREATE TABLE Clients
        (Client_name STRING PRIMARY KEY   NOT NULL,
        Client_IP       STRING    NOT NULL,
        Client_port     INT     NOT NULL);''')

    def create_classification_table(self):
        self.database.execute('''CREATE TABLE Classification
        (Classification_ID INT PRIMARY KEY NOT NULL,
        Client_name STRING NOT NULL,
        Process_name STRING NOT NULL,
        Process_size INT NOT NULL,
        Classification INT NOT NULL,
        Notes STRING);''')

    #endregion

    def is_exist(self, table_name, primary_key):  #checks if a row is already exists in a table
        cur = self.database.cursor()
        if (table_name == "Clients"):
            res = cur.execute("SELECT * FROM Clients Where Client_name='" + primary_key + "'")
        else:
            res = cur.execute("SELECT * FROM Classification Where Classification_ID=" + str(primary_key))
        return res.fetchall()

    def add_row_to_table(self, table_name, param_tuple):  #adds a selected row from table
        if table_name == "Clients":
            if not self.is_exist("Clients", param_tuple[0]):
                self.database.execute(
                    "INSERT INTO Clients VALUES ('%s','%s',%d)" % (param_tuple[0], param_tuple[1], param_tuple[2]))
                self.database.commit()
                print "Client " + param_tuple[0] + " added"
            else:
                print "Client " + param_tuple[0] + " is exist"

        else:
            if not self.is_exist("Classification", param_tuple[0]):
                self.database.execute("INSERT INTO Classification VALUES (%d,'%s','%s',%d,%d, 'None')" % (
                    param_tuple[0], param_tuple[1], param_tuple[2], param_tuple[3], param_tuple[4]))
                self.database.commit()
                print "Process " + param_tuple[2] + " added"
            else:
                print "Process " + param_tuple[2] + " is exist"

    def delete_row(self, table_name, primary_key):  #deletes a selected row from table
        if self.is_exist(table_name, primary_key):
            if type(primary_key) == str:
                self.database.execute("DELETE from %s where %s = '%s'" % (
                    table_name, self.table_dict[table_name], primary_key.decode('utf-8')))
                self.database.commit()
            else:
                self.database.execute(
                    "DELETE from %s where %s = %s" % (table_name, self.table_dict[table_name], primary_key))
                self.database.commit()
        else:
            print "%s was not found" % primary_key

    def update_table(self, table_name, param, value, primary_key):  #update a parameter in a selected row in a table
        if param != self.table_dict[table_name]:
            if type(primary_key) == str:
                self.database.execute("UPDATE %s set %s= '%s' where %s = '%s'" % (
                    table_name, param, value, self.table_dict[table_name], primary_key.decode('utf-8')))
                self.database.commit()
            else:
                self.database.execute("UPDATE %s set %s= '%s' where %s = %s" % (
                    table_name, param, value, self.table_dict[table_name], primary_key))
                self.database.commit()
                if param == "Process_size":
                    self.database.execute(
                        "UPDATE Classification set Notes = 'Process size has been changed' where %s = %s" % (
                            self.table_dict[table_name], primary_key))
                    self.database.commit()
        else:
            print "Can't change primary key"

    def print_data(self, table_name):  #print selected table
        cur = self.database.cursor()
        print "%s Table:" % table_name
        cur.execute("SELECT * FROM %s" % table_name)
        rows = cur.fetchall()
        for row in rows:
            print row

    def check_classification(self, client_name, process_name):  #checks the classification of the process on a specific
    # client while 0 means ask the client again, 1 means white list and 2 means black list
        cur = self.database.cursor()
        cur.execute("SELECT Client_name, Process_name, Classification, Notes, Classification_ID from Classification")
        results = cur.fetchall()
        for row in results:
            if row[0] == client_name.decode('utf-8') and row[1] == process_name.decode('utf-8'):
                if row[3] != "None" and row[2] == 1:  #checks if the size was changed and process approved
                    self.update_table("Classification", "Classification", 0, row[4])
                    lst = list(row)
                    lst[2] = 0
                    row = tuple(lst)
                return row[2]
        return "Not found"
#
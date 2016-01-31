# -*- coding: utf-8 -*-
# region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 25/01/2016                                               #
# Name: CameraStatus                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.7 64-bit                             #
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

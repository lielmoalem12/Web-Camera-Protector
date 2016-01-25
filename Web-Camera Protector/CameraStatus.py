#region Imports
from win32com.client import GetObject
import os
import ctypes
import sys
#endregion


#region Constants
DEVICE_NAME = "USB Video Device"
HANDLE_EXE_PATH = os.path.dirname(os.path.realpath(sys.argv[0])) + r"\Handle.exe"
PROCESS_TERMINATE = 1
#endregion

#region ----------   CLASSES   -----------------------------
class  CameraStatus:
    # -----  DATA  -----
    def __init__(self):
        self.physical_device_object_name = ""
        self.process_name = ""
        self.process_id = -999
        self.status = ""
        self.processDict = {}
        self.executable_path = ""
        self.exe_size = ""



    #Change to get from server
    def Get_Classification(self, ProcessName):
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
#endregion
#-------Check-------
#a = CameraStatus()
#a.Get_Camera_Status()
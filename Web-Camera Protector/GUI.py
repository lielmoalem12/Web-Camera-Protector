#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 20/01/2016                                               #
# Name: CameraStatus                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.6 64-bit                             #
# Python Environment  : PyCharm                                  #
##################################################################
"""
#endregion

#region ----Imports----
from CameraStatus import *
import socket
import time
import threading
import pythoncom
import subprocess
#endregion

#region ----Constants----
IP = '127.0.0.1'
PORT = 5555
BUF_SIZE = 4096
GUI_PATH = os.path.dirname(os.path.realpath(sys.argv[0])) + r"\Web-Camera Protector\bin\Release\Web-Camera Protector.exe"
#endregion

class GUI:

    def __init__(self):  #Constructor
        self.camera_details = CameraStatus()
        self.status_now = self.camera_details.Get_Camera_Status()
        self.gui_socket = type(socket)
        self.client_name = ""

    def CheckStatus(self):  #Check the camera status every 5 seconds
        while True:
            pythoncom.CoInitialize()
            check = CameraStatus()
            status_now = check.Get_Camera_Status()
            self.camera_details = check
            self.status_now = status_now
            pythoncom.CoUninitialize()
            time.sleep(5)

    def handle_command(self):  #Handle commands received from GUI
            while True:
                command = self.gui_socket.recv(BUF_SIZE)
                dict_command = { "Status" :  self.get_status, "KillThis": self._kill_process}
                if ( command in dict_command.keys() ):
                    dict_command[command]()

    def get_status(self):  #send to GUI camera's status
        if self.status_now == '1':
            self.gui_socket.send("Camera is in use#"+self.camera_details.process_name + "#" +self.camera_details.exe_size)
            time.sleep(0.1)
        elif self.status_now == '0':
            self.gui_socket.send("Camera was not found")
        else:
            self.gui_socket.send("Camera is not in use")

    def _kill_process(self):  #Kill the process that using the camera
                try:
                    self.camera_details.KillProcess(self.camera_details.process_id)
                except Exception as detail:
                    print 'run-time error : ', detail

    def run(self): #activate GUI and handle commands from GUI, also checks the camera status
        subprocess.Popen([GUI_PATH])
        esocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        esocket.bind((IP, 5555))
        esocket.listen(1)
        print 'waiting for connections'
        self.gui_socket, gui_address = esocket.accept()
        print 'connected successfully'
        t1 = threading.Thread(target=self.CheckStatus)
        t2 = threading.Thread(target=self.handle_command)
        t1.start()
        t2.start()
GUI().run()

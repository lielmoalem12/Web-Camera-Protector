#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 20/01/2016                                               #
# Name: CameraStatus                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.7 64-bit                             #
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

#endregion

#region Constants
IP = '127.0.0.1'
PORT = 5555
BUF_SIZE = 4096
#endregion

class GUI:
    def __init__(self):
        self.cameradetails = CameraStatus()
        self.statusnow = self.cameradetails.Get_Camera_Status()
        self.guisocket = ""

    def CheckStatus(self):
        while True:
            pythoncom.CoInitialize()
            check = CameraStatus()
            statusnow = check.Get_Camera_Status()
            self.cameradetails = check
            self.statusnow = statusnow
            pythoncom.CoUninitialize()
            time.sleep(5)

    def Handle_Command(self):
            command = self.guisocket.recv(BUF_SIZE)
            dict_command = { "Status" :  self.get_status, "KillThis": self._kill_process}
            if ( command in dict_command.keys() ):
                dict_command[command]()


    def get_status(self):
        if self.statusnow == '1':
            self.guisocket.send("Camera is in use#"+self.cameradetails.process_name + "#" +self.cameradetails.exe_size)
            time.sleep(0.1)
        elif self.statusnow == '0':
            self.guisocket.send("Camera was not found")
        else:
            self.guisocket.send("Camera is not in use")

    def _kill_process(self):
                try:
                    self.cameradetails.KillProcess(self.cameradetails.process_id)
                except Exception as detail:
                    print 'run-time error : ', detail



    def threadnum2(self):
        while True:
            self.Handle_Command()

    def run(self):
        Esocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Esocket.bind((IP, 5555))
        Esocket.listen(1)
        print 'waiting for connections'
        self.guisocket, GUIADRESS = Esocket.accept()
        print 'connected sucssesfully'
        t1 = threading.Thread(target=self.CheckStatus)
        t2 = threading.Thread(target=self.threadnum2)
        t1.start()
        t2.start()
GUI().run()

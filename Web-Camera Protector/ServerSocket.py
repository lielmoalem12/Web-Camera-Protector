#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 31/01/2016                                               #
# Name: ServerSocket                                             #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.6 64-bit                             #
# Python Environment  : PyCharm                                  #
##################################################################
"""
#endregion

#region ---- Imports ----
import socket
import select
from DataBase import *
#endregion

class ServerSocket:

    def __init__(self): #Constructor
        self.server_socket = socket.socket()
        self.server_socket.bind(('0.0.0.0', 1729))
        self.server_socket.listen(10)
        self.open_client_sockets = []
        self.database = DataBase()
        self.commands_dict = {"GetWhiteList": self.send_white_list(), "GetBlackList": self.send_black_list(), "RemoveProcess": self.remove_process(), "UpdateProcess": self.update_process()}

    def handle_clients(self): #handle all the clients using the service
        while True:
            read_list , write_list, error_list = select.select([self.server_socket]+ self.open_client_sockets, [], [])
            for current_socket in read_list:
                if current_socket is self.server_socket:
                    (new_socket , address) = self.server_socket.accept()
                    self.open_client_sockets.append(new_socket)

                else:
                    data = current_socket.recv(1024)
                    if data =="":
                        self.open_client_sockets.remove(current_socket)
                        print "connection with client close"
                    else :
                        datalist = self.unpack_command(data)
                        self.handle_command(datalist)

    def unpack_command(self, command): #unpacking command parts like command itself, parameters , parameters' number
        params = []
        details = command.split('#')
        command = details[0]
        param_number = int(details[1])
        for x in xrange(param_number):
            params.append(details[x+2])
        return [command, param_number, params]

#region fill it
    def send_white_list(self, client_name, classification):
        self.database.get_list(client_name, classification)

    def send_black_list(self, client_name, classification):
        self.database.get_list(client_name, classification)

    def remove_process(self):
        pass

    def update_process(self):
        pass
#endregion

    def handle_command(self, datalist): #call the right command from the dictionary
        if (datalist[1] in self.commands_dict.keys()):
                    self.commands_dict[datalist[0]]()#datalist[2])
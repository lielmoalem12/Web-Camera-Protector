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
                        current_socket.send(self.handle_command(datalist))

    def unpack_command(self, command): #unpacking command parts like command itself, parameters , parameters' number
        params = []
        details = command.split('#')
        command = details[0]
        param_number = int(details[1])
        for x in xrange(param_number):
            params.append(details[x+2])
        return [command, param_number, params]

#region fill it
    def send_list(self, client_name, classification):
        return self.database.get_list(client_name, classification)

    def remove_process(self, classification_ID):
        self.database.delete_row("Classification", classification_ID)
        return "process removed"

    def update_process(self, param, value, classification_ID):
        self.database.update_table("Classification", param, value, classification_ID)
        return "process update"
#endregion

    def handle_command(self, datalist): #call the right command from the dictionary
        commands_dict = {"GetWhiteList": self.send_list(datalist[2][0], datalist[2][1]), "GetBlackList": self.send_list(datalist[2][0], datalist[2][1]), "RemoveProcess": self.remove_process(datalist[2][0]), "UpdateProcess": self.update_process(datalist[2][0], datalist[2][1], datalist[2][2])}
        if (datalist[1] in commands_dict.keys()):
            return commands_dict[datalist[0]]
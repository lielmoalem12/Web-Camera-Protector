#region ----------   ABOUT   -----------------------------
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
#endregion
#region ---- Imports ----
import sqlite3
#endregion


class DataBase:

    def __init__(self):  #Constructor
        self.database = sqlite3.connect("database.db")
        self.create_classification_table()
        self.create_clients_table()
        self.create_process_table()

#region ---- Table creating functions ----


    def create_clients_table(self):
        self.database.execute('''CREATE TABLE Clients
        (Client_name STRING PRIMARY KEY   NOT NULL,
        Client_IP       STRING    NOT NULL,
        Client_port     INT     NOT NULL);''')

    def create_process_table(self):
        self.database.execute('''CREATE TABLE Processes
        (Process_ID INT PRIMARY KET NOT NULL,
        Process_name STRING NOT NULL,
        Process_size INT NOT NULL);''')

    def create_classification_table(self):
        self.database.execute('''CREATE TABLE Classification
        (Classification_ID INT PRIMARY KEY NOT NULL,
        Client_name STRING NOT NULL,
        Process_ID INT NOT NULL,
        Classification INT NOT NULL,
        Notes STRING);''')

    def add_row_to_table(self,table_name, param_tuple):
        if table_name == "Clients":
            self.database.execute("INSERT TO Clients (Client_name, Client_IP, Client_port) \ VALUES (%s,%s,%s)", (param_tuple[0], param_tuple[1], param_tuple[2])
#endregion

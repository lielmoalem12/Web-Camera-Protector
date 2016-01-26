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

    def create_client_table(self):
        

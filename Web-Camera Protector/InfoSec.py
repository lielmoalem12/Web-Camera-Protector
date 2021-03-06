#region ----------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Liel Moalem                                        #
# Date: 16/01/2016                                               #
# Name: InfoSec                                                  #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 64-bit                          #
# Python Tested Versions: 2.7 64-bit                             #
# Python Environment  : PyCharm                                  #
##################################################################
"""
#endregion

#region ----Imports----
import base64
from Crypto.Cipher import AES
from Crypto import Random
#endregion

#region ----Constants----
BLOCK_SIZE = 16
PAD = lambda s: s + (BLOCK_SIZE- len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE- len(s) % BLOCK_SIZE)#Adds chars to the end of the plain text so it will a fit a 16 bytes block
UNPAD = lambda s : s[:-ord(s[len(s)-1:])]
#endregion

class AESCipher:

    def __init__( self, key ):  #Constructor
        #Generate a key with 16 bytes as a function of user's key
        if len(key)<16:
            self.key = key + chr((16-len(key)))*(16-len(key))
        elif len(key)>16:
            self.key = key[:16]
        else:
            self.key = key

    def encrypt( self, raw ):#encrypting the plain text by generated key
        raw = PAD(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):#decrypting the encrypted text by generated key
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return UNPAD(cipher.decrypt( enc[16:] ))
#test
key = raw_input("Enter Encryption key:")
aes = AESCipher(key)
msg = "hey"
print msg
msg = aes.encrypt(msg)
print msg
msg = aes.decrypt(msg)
print msg

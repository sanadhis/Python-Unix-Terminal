import getpass
import os

def getOraclePath():
    user = getpass.getuser()
    path = '/home/'+user+'/Oracle'
    return path

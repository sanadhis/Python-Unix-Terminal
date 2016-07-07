import getpass
import os

def getOraclePath():
    user = getpass.getuser()
    path = '/home/'+user+'/Oracle'
    return path

def sendOsCommand(command):
    os.system(command)    

def getDomainPath(domainName):
    baseOraclePath = getOraclePath()
    domainPath = baseOraclePath + '/user_projects/domains/' + domainName
    return domainPath

def sendWLSTCommand(filename):
    baseOraclePath = getOraclePath()
    wlstPath = baseOraclePath + '/oracle_common/common/bin/wlst.sh '
    sendOsCommand(wlstPath + filename)

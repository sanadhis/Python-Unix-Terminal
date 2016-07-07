import getpass
import os

def getOraclePath():
    user = getpass.getuser()
    path = '/home/'+user+'/Oracle'
    return path

def getDomainPath(domainName):
    baseOraclePath = getOraclePath()
    domainPath = baseOraclePath + '/user_projects/domains/' + domainName
    return domainPath

def setDomainName():
    domainName = raw_input('Enter domain name: ') 

def sendOsCommand(command):
    os.system(command)    

def sendWLSTCommand(filename):
    baseOraclePath = getOraclePath()
    wlstPath = baseOraclePath + '/oracle_common/common/bin/wlst.sh '
    sendOsCommand(wlstPath + filename)

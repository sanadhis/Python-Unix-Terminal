import getpass
import os
import sys

def addPath(path1,path2):
    return path1 + path2

def buildInstallCommand(updateOption,otdType):
    return "./otd_linux64.bin -silent ORACLE_HOME=" + getOraclePath() + " DECLINE_SECURITY_UPDATES="+ updateOption +" INSTALL_TYPE=" + otdType

#define a self-check for the path
def execProgram(filePath):
    if pathExists(filePath):
        sendOsCommand(filePath)
    else:
        print(filePath + " Doesn't Exists")

def execWLSTCommand(wlstScript):
    wlstPath = getOraclePath()+ '/oracle_common/common/bin/wlst.sh'
    if pathExists(wlstPath):
        sendOsCommand(wlstPath + ' ' + wlstScript)
    else:
        print(wlstPath + " Doesn't Exists")
    
def getOraclePath():
    user = getpass.getuser()
    oraclePath = '/home/'+user+'/Oracle'
    return oraclePath

def getFromBasePath(path):
    return getOraclePath() + path

def getDomainPath(domainName):
    domainPath = addPath(getFromBasePath('/user_projects/domains/'),domainName)
    return domainPath

def getWebLogicServerPath(domainPath):
    return addPath(domainPath,'/bin/startWebLogic.sh')

def getNodeManagerPath(domainPath):
    return addPath(domainPath,'/bin/startNodeManager.sh')

def pathExists(domainPath):
    if os.path.exists(domainPath):
        return True
    else:
        sys.exit("Domain Path Doesn't Exist!")

def selectDomain():
    domainPath = ''
    while(True):
        try:
            domainName = raw_input('Enter domain name: ')
            domainPath = getDomainPath(domainName)
            if pathExists(domainPath):
                break
            else:
                print("Domain doesn't exist! Try again")
        except:
            print('Wrong Input')
    return domainPath    

def sendOsCommand(command):
    os.system(command)    

def startOTD(domainName,configName,machineName):
    domainPath = getDomainPath(domainName)
    if pathExists(domainPath):
        instancePath = addPath(domainPath,'/config/fmwconfig/components/OTD/instances/otd_'+configName+"_"+machineName+"/")
        otdServerPath = addPath(instancePath,'bin/startserv')
        execProgram(otdServerPath)

def writeConfigurationScript(domainName,configurationName,listenerPort,serverName,originServer,scriptFile):
    props = {}
    props['configuration'] = configurationName
    props['listener-port'] = listenerPort
    props['server-name'] = serverName
    props['origin-server'] = originServer
    writeWLSTScript(props,domainName,'Configuration',scriptFile)

def writeInstanceScript(domainName,configurationName,machineName,scriptFile):
    props = {}
    props['configuration'] = configurationName
    props['machine'] = machineName
    writeWLSTScript(props,domainName,'Instance',scriptFile) 
    
def writeWLSTScript(props,domainName,unitCreated,scriptFile):
    file = open(scriptFile,'w')
    file.write("readDomain('"+getDomainPath(domainName)+"')\n")
    file.write("props="+str(props)+"\n")
    file.write("otd_create"+unitCreated+"(props)\n")
    file.write("updateDomain()\n")
    file.write("closeDomain()\n")
    file.close()

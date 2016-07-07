import getpass
import os

def addPath(path1,path2):
    return path1 + path2

def buildInstallCommand(updateOption,otdType):
    return "./otd_linux64.bin -silent ORACLE_HOME=" + getOraclePath() + " DECLINE_SECURITY_UPDATES="+ updateOption +" INSTALL_TYPE=" + otdType

def execProgram(filePath):
    if pathExists(filePath):
        sendOsCommand(filePath)
    else:
        print(filePath + " Doesn't Exists")

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
    return os.path.exists(domainPath)

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

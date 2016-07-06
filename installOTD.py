import getpass
import os

updateChoice = ('true','false')
otdType = ('\"Collocated OTD (Managed through WebLogic server)\"','\"Standalone OTD (Managed independently of WebLogic server)\"')

def configuration():
    user = getpass.getuser()
    path = '/home/'+user+'/Oracle'
    while(True):
        try:
            securityUpdate = raw_input('Decline Security Update? (y/n): ').lower()
            installType = raw_input('Install Type? (Collocated(C)/Stand Alone(S)): ').lower()
        except:
            print('Null Input')
        if((securityUpdate=='y' or securityUpdate.lower()=='n') and (installType=='c' or installType.lower()=='s')):
            break
        else:
            print('Wrong Input/Command')
    if securityUpdate == 'y':
        securityUpdate = updateChoice[0]
    else:
        securityUpdate = updateChoice[1]
    if installType == 'c':
        installType = otdType[0]
    else:
        installType = otdType[1]
    return path, securityUpdate, installType

def installation(configOption):
    path = configOption[0]
    updateOption = configOption[1]
    otdOption = configOption[2]
    installCommand = "./otd_linux64.bin -silent ORACLE_HOME=" + path + " DECLINE_SECURITY_UPDATES="+ updateOption +" INSTALL_TYPE=" + otdOption 
    os.system(installCommand)

installation(configuration())

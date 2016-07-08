from otdModule import buildInstallCommand,getOraclePath,sendOsCommand

updateChoice = ('true','false')
otdType = ('\"Collocated OTD (Managed through WebLogic server)\"','\"Standalone OTD (Managed independently of WebLogic server)\"')

def configuration():
    while(True):
        try:
            securityUpdate = raw_input('Decline Security Update? (y/n): ').lower()
            installType = raw_input('Install Type? (Collocated(C)/Stand Alone(S)): ').lower()
        except:
            print('Null Input')
        if((securityUpdate=='y' or securityUpdate=='n') and (installType=='c' or installType=='s')):
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
    return securityUpdate, installType

def install(configOption):
    updateOption = configOption[0]
    otdOption = configOption[1]
    installCommand = buildInstallCommand(updateOption,otdOption)
    print(installCommand)
    #sendOsCommand(installCommand)

install(configuration())

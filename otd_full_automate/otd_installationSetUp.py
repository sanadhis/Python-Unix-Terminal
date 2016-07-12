from otdModule import buildInstallCommand,sendOsCommand,readConfiguration,printFlag

updateChoice = ('true','false')
otdType = ('\"Collocated OTD (Managed through WebLogic server)\"','\"Standalone OTD (Managed independently of WebLogic server)\"')

def configuration():
    savedConfiguration = readConfiguration()
    securityUpdate = savedConfiguration['securityUpdate']
    installType = savedConfiguration['type']
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
    printFlag('Begin Installation')
    sendOsCommand(installCommand)
    printFlag('Installation Done')

install(configuration())

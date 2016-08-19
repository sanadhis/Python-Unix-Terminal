from otdModule import buildInstallCommand,sendOsCommand,readConfiguration,printFlag

"""Execute this file to begin the installation process
    Installation are conducted in silent mode of OTD installation

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

#the fixed string to pass as the parameters for OTD installation
updateChoice = ('true','false')
otdType = ('\"Collocated OTD (Managed through WebLogic server)\"','\"Standalone OTD (Managed independently of WebLogic server)\"')

def configuration():
    """This method gather and set the required params for creating an domain 

        For example, this method can return [true,Collocated OTD (Managed through WebLogic server)] => array contains two

        Returns:
            array[string] : return the security update choice string (Enum) and install type string (Enum)
    """
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
    """This method execute the process of installing the OTD 

        Args:
            configOption (array[string]) : contains the DECLINE_SECURITY_UPDATE (securityUpdate) and INSTALL_TYPE (installType) params for the installation in silent mode

        Returns:
            null.
    """
    updateOption = configOption[0]
    otdOption = configOption[1]
    installCommand = buildInstallCommand(updateOption,otdOption)
    printFlag('Begin Installation')
    sendOsCommand(installCommand)
    printFlag('Installation Done')

install(configuration())

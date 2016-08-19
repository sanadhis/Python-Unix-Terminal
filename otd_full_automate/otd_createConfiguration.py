from otdModule import readConfiguration,writeConfigurationScript,execWLSTCommand,printFlag

"""Execute this file to create a configuration

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

#default value
domainName = 'base_domain'
configurationName = 'defaultConfig'
listenerPort = '20010'
serverName = 'localhost'
originServer = 'localhost:80'
scriptFile = "otd_wlstScript.py"

def setConfiguration():
    """This method gather and set the required params for creating a configuration 

        Returns:
            null.
    """
    global domainName, configurationName, listenerPort, serverName, originServer
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    configurationName = savedConfiguration['configuration']
    listenerPort = savedConfiguration['listener']
    serverName = savedConfiguration['server']
    originServer = savedConfiguration['origin']

def createConfiguration():
    """This method execute the process of creating a configuration 

        Returns:
            null.
    """
    writeConfigurationScript(domainName,configurationName,listenerPort,serverName,originServer,scriptFile)
    printFlag('Begin Creating Configuration')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Configuration')

setConfiguration()
createConfiguration()

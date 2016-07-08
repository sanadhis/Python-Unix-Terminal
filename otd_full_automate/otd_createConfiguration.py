from otdModule import readConfiguration,writeConfigurationScript,execWLSTCommand

domainName = 'base_domain'
configurationName = 'defaultConfig'
listenerPort = '20010'
serverName = 'localhost'
originServer = 'localhost:80'
scriptFile = "otd_wlstScript.py"

def setConfiguration():
    global domainName, configurationName, listenerPort, serverName, originServer
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    configurationName = savedConfiguration['configuration']
    listenerPort = savedConfiguration['listener']
    serverName = savedConfiguration['server']
    originServer = savedConfiguration['origin']

def createConfiguration():
    writeConfigurationScript(domainName,configurationName,listenerPort,serverName,originServer,scriptFile)
    execWLSTCommand(scriptFile)

setConfiguration()
createConfiguration()

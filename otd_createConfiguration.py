from otdModule import getDomainPath,writeConfigurationScript,execWLSTCommand

domainName = 'base_domain'
configurationName = 'defaultConfig'
listenerPort = '20010'
serverName = 'localhost'
originServer = 'localhost:80'
scriptFile = "otd_wlstScript.py"

def setConfiguration():
    global domainName, configurationName, listenerPort, serverName, originServer
    domainName = raw_input('Enter domain name: ')
    configurationName = raw_input('Enter Configuration name: ')
    listenerPort = raw_input("Enter OTD's instances port: ")
    serverName = raw_input("Enter OTD's server name: ")
    originServer = raw_input("Enter the back-end's Server: ")

def createConfiguration():
    writeConfigurationScript(domainName,configurationName,listenerPort,serverName,originServer,scriptFile)
    execWLSTCommand(scriptFile)

setConfiguration()
createConfiguration()

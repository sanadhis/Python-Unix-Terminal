from otdModule import startOTD

domainName = 'base_domain'
configurationName = 'defaultConfig'
machineName = 'machine0'

def setInstance():
    global domainName, configurationName, machineName
    domainName = raw_input('Enter domain name: ')
    configurationName = raw_input('Enter Configuration name: ')
    machineName = raw_input("Enter target's machine: ")

def startInstance():
    startOTD(domainName,configurationName,machineName)

setInstance()
startInstance()

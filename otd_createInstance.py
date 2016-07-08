from otdModule import writeInstanceScript,execWLSTCommand,startOTD

domainName = 'base_domain'
configurationName = 'defaultConfig'
machineName = 'machine0'
scriptFile = "otd_wlstScript.py"

def setInstance():
    global domainName, configurationName, machineName
    domainName = raw_input('Enter domain name: ')
    configurationName = raw_input('Enter Configuration name: ')
    machineName = raw_input("Enter target's machine: ")

def createInstance():
    writeInstanceScript(domainName,configurationName,machineName,scriptFile)
    execWLSTCommand(scriptFile)
    startOTD(domainName,configurationName,machineName)

setInstance()
createInstance()

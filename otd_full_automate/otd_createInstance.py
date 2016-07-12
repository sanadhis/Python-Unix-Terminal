from otdModule import readConfiguration,writeInstanceScript,execWLSTCommand,startOTD,printFlag

domainName = 'base_domain'
configurationName = 'defaultConfig'
machineName = 'machine0'
scriptFile = "otd_wlstScript.py"

def setInstance():
    global domainName, configurationName, machineName
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    configurationName = savedConfiguration['configuration']
    machineName = savedConfiguration['machine']

def createInstance():
    writeInstanceScript(domainName,configurationName,machineName,scriptFile)
    printFlag('Begin Creating Instance')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Instance')
    startOTD(domainName,configurationName,machineName)
    

setInstance()
createInstance()

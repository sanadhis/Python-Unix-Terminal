from otdModule import readConfiguration,writeCreateDomainScript,execWLSTCommand,printFlag

domainName = 'base_domain'
username = 'weblogic'
password = 'otd123otd'
scriptFile = "otd_wlstScript.py"

def setDomain():
    global domainName, configurationName, listenerPort, serverName, originServer
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    username = savedConfiguration['username']
    password = savedConfiguration['password']

def createDomain():
    writeCreateDomainScript(domainName,username,password)
    printFlag('Begin Creating Domain')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Domain')

setDomain()
createDomain()

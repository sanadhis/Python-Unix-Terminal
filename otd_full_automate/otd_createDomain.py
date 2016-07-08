from otdModule import readConfiguration,writeCreateDomainScript,execWLSTCommand

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
    execWLSTCommand(scriptFile)

setDomain()
createDomain()

from otdModule import writeCreateDomainScript,execWLSTCommand

domainName = 'base_domain'
username = 'weblogic'
password = 'otd123otd'
scriptFile = "otd_wlstScript.py"

def setDomain():
    global domainName, configurationName, listenerPort, serverName, originServer
    domainName = raw_input('Enter the name of Domain you want to create: ')
    username = raw_input('Enter domain\'s admin username: ')
    password = raw_input("Enter domain's admin password: ")

def createDomain():
    writeCreateDomainScript(domainName,username,password)
    execWLSTCommand(scriptFile)

setDomain()
createDomain()

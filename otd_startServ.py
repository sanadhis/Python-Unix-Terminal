from configModule import getDomainPath,sendWLSTCommand

domainName = 'base_domain'

def setConfiguration():
    global domainName, configurationName, listenerPort, serverName, originServer
    domainName = raw_input('Enter domain name: ')

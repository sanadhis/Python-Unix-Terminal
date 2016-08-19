from otdModule import readConfiguration,writeCreateDomainScript,execWLSTCommand,printFlag

"""Execute this file to create a domain

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

#default value
domainName = 'base_domain'
username = 'weblogic'
password = 'otd123otd'
scriptFile = "otd_wlstScript.py"

def setDomain():
	"""This method gather and set the required params for creating a domain 

        Returns:
            null.
    """
    global domainName, configurationName, listenerPort, serverName, originServer
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    username = savedConfiguration['username']
    password = savedConfiguration['password']

def createDomain():
	"""This method execute the process of creating a domain 

        Returns:
            null.
    """
    writeCreateDomainScript(domainName,username,password)
    printFlag('Begin Creating Domain')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Domain')

setDomain()
createDomain()

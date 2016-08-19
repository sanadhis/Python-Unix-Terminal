from otdModule import readConfiguration,writeInstanceScript,execWLSTCommand,startOTD,printFlag

"""Execute this file to create an instance from existing domain and machine

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

#default value
domainName = 'base_domain'
configurationName = 'defaultConfig'
machineName = 'machine0'
scriptFile = "otd_wlstScript.py"

def setInstance():
    """This method gather and set the required params for creating an instance 

        Returns:
            null.
    """
    global domainName, configurationName, machineName
    savedConfiguration = readConfiguration()
    domainName = savedConfiguration['domain']
    configurationName = savedConfiguration['configuration']
    machineName = savedConfiguration['machine']

def createInstance():
    """This method execute the process of creating an instance 

        Returns:
            null.
    """
    writeInstanceScript(domainName,configurationName,machineName,scriptFile)
    printFlag('Begin Creating Instance')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Instance')
    startOTD(domainName,configurationName,machineName)
    

setInstance()
createInstance()

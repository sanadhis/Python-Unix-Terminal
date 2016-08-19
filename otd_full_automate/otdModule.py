import getpass
import os
import sys

"""This module contains the required functions/methods to install, set, and configuring OTD.
    The installation method install both Standalone and Collocated OTD
    The methods :writeCreateDomainScript, writeConfigurationScript, writeCreateMachineScript, and writeInstanceScript are used only for Collocated OTD

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

def addPath(path1,path2):
    """addPath function, is used to build a path from 2 given path

        Args:
            path1 (str): the beginning path
            path2 (str): the continuation of path

        Returns:
            string: the formed path detail
    """
    return path1 + path2

def buildInstallCommand(updateOption,otdType):
    """buildInstallCommand function, is used to form an installation command for OTD installation

        Args:
            updateOption (str): the choice of security updates (true/false)
            otdType (str): the otd installation type (Standalone or Collocated)

        Returns:
            string: the linux shell installation command for OTD
    """
    installString = "./otd_linux64.bin -silent ORACLE_HOME=" + getOraclePath() + " DECLINE_SECURITY_UPDATES="+ updateOption +" INSTALL_TYPE=" + otdType
    if otdType == 'Collocated OTD (Managed through WebLogic server)':
        return installString
    else:
        return installString + " MYORACLESUPPORT_USERNAME=xx.yy.zz@cern.ch SECURITY_UPDATES_VIA_MYORACLESUPPORT=false"

def execProgram(filePath):
    """execProgram function, is used to execute a file in specific path

        perform a shelf-check of the filepath
        print an error message if the file doesn't exists

        Args:
            filePath (str): the complete path for the file

        Returns:
            null.
    """
    if pathExists(filePath):
        sendOsCommand(filePath)
    else:
        print(filePath + " Doesn't Exists")

def execWLSTCommand(wlstScript):
    """execWLST function, is used to execute an otd_wlstScript.py using the WLST Runtime

        perform a shelf-check of the wlst.sh existence
        print an error message if the wlst.sh doesn't exists in the system

        Args:
            wlstScript (str): the name of the file that contains the WLST commands that want to be executed

        Returns:
            null.
    """
    wlstPath = getOraclePath()+ '/oracle_common/common/bin/wlst.sh'
    if pathExists(wlstPath):
        sendOsCommand(wlstPath + ' ' + wlstScript)
    else:
        print(wlstPath + " Doesn't Exists")
    
def getOraclePath():
    """getOraclePath function, is used to build a string of Oracle home default path

        the Oracle default path should be /home/<User>/Oracle

        Returns:
            string: the default Oracle path for specific user 
    """
    user = getpass.getuser()
    oraclePath = '/home/'+user+'/Oracle'
    return oraclePath

def getFromBasePath(path):
    """getFromBasePath function, is used to give additional path from Oracle default path (child directory)

        the Oracle default path should be /home/<User>/Oracle
        the child directory for example /oracle_common/common/bin

        Args:
            path (str) : the child directory inside the Oracle directory

        Returns:
            string: the formed path of file or directory inside the default Oracle home directory
    """
    return getOraclePath() + path

def getDomainPath(domainName):
    """getDomainPath function, is used to form a path or location of the specific domain name

        the domain default path should be inside /home/<User>/Oracle/user_projects/domains/

        Args:
            domainName (str) : the name of the domain

        Returns:
            string: the complete location (path) of the domain directory
    """
    domainPath = addPath(getFromBasePath('/user_projects/domains/'),domainName)
    return domainPath

def getTemplatePath(templateName):
    """getTemplatePath function, is used to form a path or location of the specific template name for the OTD domain creation

        Args:
            templateName (str) : the name of the template

        Returns:
            string: the complete location (path) of the template file
    """
    return getFromBasePath('/user_projects/templates/') + templateName

def getWebLogicServerPath(domainPath):
    """getWebLogicServerPath function, is used to form a path or location of the weblogic file of the specific domain name

        the weblogic file default path should be inside /home/<User>/Oracle/user_projects/domains/<Domain_Name>/bin/startWebLogic.sh

        Args:
            domainPath (str) : the domain's directory path

        Returns:
            string: the complete location (path) of the weblogic file of the specific domain 
    """
    return addPath(domainPath,'/bin/startWebLogic.sh')

def getNodeManagerPath(domainPath):
    """getNodeManagerPath function, is used to form a path or location of the node manager file of the specific domain name

        the node manager file default path should be inside /home/<User>/Oracle/user_projects/domains/<Domain_Name>/bin/startNodeManager.sh

        Args:
            domainPath (str) : the domain's directory path

        Returns:
            string: the complete location (path) of the node manager file of the specific domain 
    """
    return addPath(domainPath,'/bin/startNodeManager.sh')

def pathExists(domainPath):
    """pathExists function, is used to check the existence of a domain in the system

        force stop the python engine and print an error message if the domain doesn't exist

        Args:
            domainPath (str) : the domain's directory path

        Returns:
            boolean: return true if the domain is exist
            null: if the domain doesn't exist in the system
    """
    if os.path.exists(domainPath):
        return True
    else:
        sys.exit("Domain Path Doesn't Exist!")

def printFlag(message):
    """printFlag function, is used to print a flag with message indicates a process is begin or finished

        Args:
            message (str) : the string that want to be displayed and states the process

        Returns:
            null
    """
    print("\n================= "+message+" =================\n")

def readConfiguration():
    """readConfiguration function, is used to read the configuration of OTD for installation, domain creation and instance deployment

        read configuration that are stored in otdConfiguration.txt

        Returns:
            array[string]: the array contains all the configuration in the stored file
    """
    configuration = {}
    file = open('otdConfiguration.txt','r')
    for line in file:
        conf = line.rstrip().split(' ')
        configuration[conf[0]] = conf[1]
    return configuration    

def selectDomain():
    """
        Don't really used
    """
    domainPath = ''
    while(True):
        try:
            domainName = raw_input('Enter domain name: ')
            domainPath = getDomainPath(domainName)
            if pathExists(domainPath):
                break
            else:
                print("Domain doesn't exist! Try again")
        except:
            print('Wrong Input')
    return domainPath    

def sendOsCommand(command):
    """sendOsCommand function, is used to send or execute a command in the terminal

        Args:
            command (str) : the command that want to be executed in terminal

        Returns:
            null
    """
    os.system(command)    

def startOTD(domainName,configName,machineName):
    """startOTD function, is used to start a Standalone otd instance to the specific machine

        this function run a specific instance of the specific Standalone OTD domain with given configuration name and machine name

        Args:
            domainName (str) : the domain name
            configName (str) : the domain configuration name
            machineName (str) : the machine where instance is deployed

        Returns:
            null
    """
    domainPath = getDomainPath(domainName)
    if pathExists(domainPath):
        instancePath = addPath(domainPath,'/config/fmwconfig/components/OTD/instances/otd_'+configName+"_"+machineName+"/")
        otdServerPath = addPath(instancePath,'bin/startserv')
        execProgram(otdServerPath)

def writeConfigurationScript(domainName,configurationName,listenerPort,serverName,originServer,scriptFile):
    """writeConfigurationScript function, is used to write the required WLST command for creating configuration

        the WLST commands are being stored in a long string variable : scriptText,
        then they are being written into a script file to be executed later using WLST runtime

        Args:
            domainName (str) : the domain's name
            configurationName (str) : the name of the configuration that want to be created
            listenerPort (str) : the listen port
            serverName (str) : the hostname of the machine target for this configuration
            originServer (str) : the associate back-end server(s) for this configuration
            scriptFile (str) : the file name to store the WLST command for creating configuration

        Returns:
            null
    """
    props = {}
    props['configuration'] = configurationName
    props['listener-port'] = listenerPort
    props['server-name'] = serverName
    props['origin-server'] = originServer
    scriptText = "readDomain('"+getDomainPath(domainName)+"')\n"
    scriptText += "props="+str(props)+"\n"
    scriptText += "otd_createConfiguration(props)\n"
    scriptText += "updateDomain()\n"
    scriptText += "closeDomain()\n"
    writeWLSTScript(scriptText,scriptFile)

def writeCreateDomainScript(domainName,username,password):
    """writeCreateDomainScript function, is used to write the required WLST command for creating a Collocated domain

        the WLST commands are being stored in a long string variable : scriptText,
        then they are being written into a script file to be executed later using WLST runtime

        Args:
            domainName (str) : the domain's name
            username (str) : the name of admin user for the domain
            password (str) : the password of admin user for the domain

        Returns:
            null
    """
    #applies if the otd template path is exists
    #templatePath = getTemplatePath('otd_domainTemplate.jar')
    #domainPath = getDomainPath(domainName)
    #props = [templatePath,domainPath,username,password]
    #scriptText = "createDomain('" + "','".join(props) + "')"

    defaultListenAddress = "localhost"
    defaultListenPort = "7001"
    domainPath = getDomainPath(domainName)

    scriptText = "selectTemplate('Oracle Traffic Director - Restricted JRF')\n"
    scriptText += "loadTemplates()\n"
    scriptText += "cd('Servers/AdminServer')\n"
    scriptText += "set('ListenAddress','"+defaultListenAddress+"')\n"
    scriptText += "set('ListenPort',"+defaultListenPort+")\n"
    scriptText += "cd('/')\n"
    scriptText += "cd('Security/base_domain/User/"+username+"')\n"
    scriptText += "cmo.setPassword('"+password+"')\n"
    scriptText += "setOption('OverwriteDomain','true')\n"
    scriptText += "writeDomain('"+domainPath+"')\n"
    scriptText += "closeTemplate()\n"
    scriptText += "exit('y')\n"
    
    writeWLSTScript(scriptText,'otd_wlstScript.py')

def writeCreateMachineScript(serverUser,serverPass,serverAdmURL,machineName,machineAddress,machinePort):
    """writeCreateMachineScript function, is used to write the required WLST command for registering a machine

        the WLST commands are being stored in a long string variable : scriptText,
        then they are being written into a script file to be executed later using WLST runtime

        Args:
            serverUser (str) : the name of admin user for the domain
            serverPass (str) : the password of admin user for the domain
            serverAdmURL (str) : the administration console url
            machineName (str) : the alias name of the machine that want to be registered
            machineAddress (str) : the machine address (hostname)
            machinePort (str) : the machine listen port (the node manager port number)

        Returns:
            null
    """
    props = [serverUser,serverPass,serverAdmURL]
    scriptText = "connect('"+"','".join(props)+"')\n"
    scriptText += "edit()\n"
    scriptText += "startEdit()\n"
    scriptText += "create('"+machineName+"','Machine')\n"
    scriptText += "cd('Machines/"+machineName+"/NodeManager/"+machineName+"')\n"
    scriptText += "set('ListenAddress','"+machineAddress+"')\n"
    scriptText += "set('ListenPort','"+machinePort+"')\n"
    scriptText += "save()\n"
    scriptText += "stopEdit('y')\n"
    scriptText += "exit('y')\n"
    writeWLSTScript(scriptText,'otd_wlstScript.py')

def writeInstanceScript(domainName,configurationName,machineName,scriptFile):
    """writeInstanceScript function, is used to write the required WLST command for creating an instance

        the WLST commands are being stored in a long string variable : scriptText,
        then they are being written into a script file to be executed later using WLST runtime

        Args:
            domainName (str) : the name of the domain
            configurationName (str) : the name of the configuration that wants to be diployed (should be existing configuration)
            machineName (str) : the alias name of the machine that want to be registered (should be registered machine)
            scriptFile (str) : the file name to store the WLST command for creating configuration

        Returns:
            null
    """
    props = {}
    props['configuration'] = configurationName
    props['machine'] = machineName
    scriptText = "readDomain('"+getDomainPath(domainName)+"')\n"
    scriptText += "props="+str(props)+"\n"
    scriptText += "otd_createInstance(props)\n"
    scriptText += "updateDomain()\n"
    scriptText += "closeDomain()\n"
    writeWLSTScript(scriptText,scriptFile) 
    
def writeWLSTScript(scriptText,scriptFile):
    """writeWLSTScript function, is used to write WLST commands in string variable into a file

        this function opens a file and write the WLST commands in the variable into it 

        Args:
            scriptText (str) : the WLST commands that want to be executed
            scriptFile (str) : the file name to store the WLST command for creating configuration

        Returns:
            null
    """
    file = open(scriptFile,'w')
    file.write(scriptText)
    file.close()

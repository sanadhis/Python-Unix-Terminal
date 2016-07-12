from otdModule import readConfiguration,writeCreateMachineScript,execWLSTCommand,printFlag

serverUser = 'weblogic'
serverPass = 'otd123otd'
serverAdmURL = 't3://kacper-desktop.cern.ch:7001/em'
machineName = 'machineX'
machineAddress = 'kacper-desktop.cern.ch'
machinePort = '5556'
scriptFile = 'otd_wlstScript.py'

def setMachine():
    global serverUser, serverPass, serverAdmURL, machineName, machineAddress, machinePort
    savedConfiguration = readConfiguration()
    serverUser = savedConfiguration['username']
    serverPass = savedConfiguration['password']
    serverAdmURL = "t3://"+savedConfiguration['serverURL']+":7001/em"
    machineName = savedConfiguration['machine']
    machineAddress = savedConfiguration['machineAddress']
    machinePort = savedConfiguration['machinePort']

def createMachine():
    writeCreateMachineScript(serverUser,serverPass,serverAdmURL,machineName,machineAddress,machinePort)
    printFlag('Begin Creating Machine')
    execWLSTCommand(scriptFile)
    printFlag('Done Creating Machine')

setMachine()
createMachine()

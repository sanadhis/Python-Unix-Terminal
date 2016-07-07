from configModule import getDomainPath,sendWLSTCommand

domainName = 'base_domain'
configurationName = 'defaultConfig'
machineName = 'machine0'

def setConfiguration():
    global domainName, configurationName, machineName
    domainName = raw_input('Enter domain name: ')
    configurationName = raw_input('Enter Configuration name: ')
    listenerPort = raw_input("Enter OTD's instances port: ")
    serverName = raw_input("Enter OTD's server name: ")
    originServer = raw_input("Enter the back-end's Server: ")

def createConfiguration():
    domainPath = getDomainPath(domainName)
    file = open('wlstScript.py','w')
    file.write("readDomain('"+domainPath+"')\n")
    file.write("props={}\n")
    file.write("props['configuration'] = '"+configurationName+"'\n")
    file.write("props['listener-port'] = '"+listenerPort+"'\n")
    file.write("props['server-name'] = '"+serverName+"'\n")
    file.write("props['origin-server'] = '"+originServer+"'\n")
    file.write("otd_createConfiguration(props)\n")
    file.write("updateDomain()\n")
    file.write("closeDomain()\n")
    file.close()
    wlstPath = getPath('/oracle_common/common/bin/wlst.sh ' + 'otd_wlstScript.py')
    execProgram(wlstPath)

setConfiguration()
createConfiguration()

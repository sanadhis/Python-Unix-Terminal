from otdModule import selectDomain,getWebLogicServerPath,execProgram

domainPath = selectDomain()
otdServPath = getWebLogicServerPath(domainPath)
execProgram(otdServPath)

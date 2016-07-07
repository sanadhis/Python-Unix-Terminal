from otdModule import selectDomain,getNodeManagerPath,execProgram

domainPath = selectDomain()
otdServPath = getNodeManagerPath(domainPath)
execProgram(otdServPath)

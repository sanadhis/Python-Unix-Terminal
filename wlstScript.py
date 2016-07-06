readDomain('/home/openlabsummerstudent/Oracle/user_projects/domains/domain1')
props={}
props['configuration'] = 'configNew'
props['listener-port'] = '20011'
props['server-name'] = 'localhost'
props['origin-server'] = 'localhost:80'
otd_createConfiguration(props)
updateDomain()
closeDomain()

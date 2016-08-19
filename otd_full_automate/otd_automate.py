import os

"""Execute this file to trigger all of OTD process from installation until deployment

    Author:
        I Made Sanadhi Sutandi (Openlab Summer Student 2016)

    Version:
        Friday, 19th August 2016
"""

os.system("python otd_installationSetUp.py")
os.system("python otd_createDomain.py")
os.system("python otd_createMachine.py")
os.system("python otd_createConfiguration.py")
os.system("python otd_createInstance.py")

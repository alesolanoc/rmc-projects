import json
import os

FIREFOX_WEBDRIVER_PATH = "c:\se\geckodriver.exe"
CREDENTIALS_FOLDER = "C:/Users/itadmin/PycharmProjects/RMC-Project/Credentials"
CREDENTIALS_FILE = 'credentials.json'

CONTRIBUTOR_EMAIL = "test@test.com"
UPDATEVALUEJSONSCRIPT = "update"
UPDATEVALUEJSONSCRIPTLANGUAGE = "-fr"
UPDATEGLOBALCATALOG = "update"

RESOURCES = {"service" : "SERVICE","operations only" : "OPERATIONS ONLY","composite" : "COMPOSITE","parent" : "PARENT","child" : "CHILD"}
RESOURCE_TYPES = ["SERVICE","OPERATIONS ONLY","COMPOSITE SERVICE","PARENT","CHILD"]
RESOURCE_COMPOSITE_TAG = "is"
RESOURCE_CONTAINED_TYPES = "test1test2"
RESOURCE_NAME_AS_SERVICE = "rmc-1p-asc-deleteme-01"
RESOURCE_NAME_AS_COMPOSITE = "rmc-1p-deleteme-automation---02d"
RESOURCE_NAME_AS_OPERATIONS = "rmc-1p-deleteme-automation---03"

VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG = ["-gc","ss","aa","dd","https://ibm.com1","https://ibm.com2","https://ibm.com3","https://ibm.com4","https://ibm.com5","test@test.com","https://ibm.com6","bullet title","bullet description","media","https://media1.com","https://media2.com","caption media"]
VALIDATE_REQUIRED_FIELDS_SERVICE = ["ga","3Q2020","service","3rd Party","84 Codes"]

def read_credentials():
    os.chdir(CREDENTIALS_FOLDER)
    with open (CREDENTIALS_FILE) as myfile:
        data = json.load(myfile)
        for record in data['env']:
            print("")
    return (record)



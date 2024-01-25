import datetime

BROWSER = ""
SERVICE_TYE = {"service" : "SERVICE","operations only" : "OPERATIONS ONLY","composite" : "COMPOSITE","parent" : "PARENT","child" : "CHILD","platform service" : "PLATFORM SERVICE"}
VALIDATE_REQUIRED_FIELDS_SERVICE = [['experimental','beta','ga'],['1Q2020','3Q2020'],['service','composite','operations only','platform service'],['3rd Party'],['84 Codes']]
TARGET_RELEASE_LEVEL = {'GA':{'top':'GA','CURRENT MATURITY':'CURRENT MATURITY: CATALOG MIN (GA)','TARGET MATURITY':'TARGET MATURITY: ONE CLOUD'},
                     'GA0':{'top':'BETA','CURRENT MATURITY':'CURRENT MATURITY: BETA','TARGET MATURITY':'TARGET MATURITY: CATALOG MIN (GA)'},
                        'EXPERIMENTAL':{'top':' ','CURRENT MATURITY':'CURRENT MATURITY: NEW','TARGET MATURITY':'TARGET MATURITY: EXPERIMENTAL'},
                        'BETA':{'top':'EXPERIMENTAL','CURRENT MATURITY':'CURRENT MATURITY: EXPERIMENTAL','TARGET MATURITY':'TARGET MATURITY: BETA'}}
COMPOSITE_RESOURCE = {'composite_tag':'is','contained_resource_types':'test','contained_resource_types2':'test1, test2'}
CURRENT_DATE = datetime.date.today().strftime('%B') + " " + datetime.date.today().strftime('%d').lstrip("0").replace(" 0"," ") + ", " + datetime.date.today().strftime('%Y')
FUTURE_DATE = (datetime.date.today()+datetime.timedelta(days=1)).strftime('%B') + " " + (datetime.date.today()+datetime.timedelta(days=1)).strftime('%d').lstrip("0").replace(" 0"," ") + ", " + (datetime.date.today()+datetime.timedelta(days=1)).strftime('%Y')
VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG = ["-gc","ss","aa","dd","https://ibm.com1","https://ibm.com2","https://ibm.com3","https://ibm.com4","https://ibm.com5","test@test.com","https://ibm.com6","bullet title","bullet description","image","https://media1.com","https://media2.com","caption media"]
#TAGS_CATALOG_LISTING = ["ai","analytics","apidocs_enabled","blockchain","compute","containers","databases","devops","hipaa","ibm_created","integration","iot","logging_monitoring","migration_tools","mobile","network","platform_services","rc_compatible","security","storage","supports_syndication"]
TAGS_CATALOG_LISTING = ["ai","analytics","blockchain","compute","containers","databases","devops","ibm_created","integration","iot","logging_monitoring","migration_tools","mobile","network","platform_services","rc_compatible","security","storage"]
JSON_SCRIPT = {}
JSON_SCRIPT_MODALEDITOR = {}
JSON_SCRIPT_TRANSLATION = {}
VALUES_FROM_CATALOG_LISTING = {}
VALUES_FROM_GLOBAL_CATALOG = {}
VALUES_FROM_PART = [{},{}]
JSON_SCRIPT_FROM_GC = {}
window_before = None

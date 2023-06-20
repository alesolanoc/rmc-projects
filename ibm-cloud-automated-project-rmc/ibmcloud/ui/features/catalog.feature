Feature: Catalog Listing general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login in IBMcloud web application as owner
    When Dashboard page is shown

      @functional
#  Scenario: Verify that a resource can be published into global catalog
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001c'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#   And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001c"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed


#  Scenario: Verify that all required fields were filled in catalog listing
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001z'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#   And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001z"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then All required fields in "Listing Page" tab should be displayed as filled
#   When Go to "Settings" tab in CL page
#   Then All required fields in "Settings" tab should be displayed as filled


#  Scenario: Verify that a bullet can be added
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Save button was pressed in CL page
#   Then Go to 'summary' tab
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Bullets should be displayed as filled

#  Scenario: Verify that a bullet can be removed
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Press Delete Feature button in optional section
#   When Save button was pressed in CL page
#   Then Go to 'summary' tab
#   Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#   Then Bullets should not be displayed


#  Scenario: Verify that a media can be added
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Go to 'summary' tab
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then media should be displayed as filled


#  Scenario: Verify that a media can be removed
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Press remove media
#   When Save button was pressed in CL page
#   Then Go to 'summary' tab
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#  Then media should not be displayed as filled

#   Scenario: Verify checkboxes were checked
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#  Then Go to 'catalog listing' tab
#   When Go to "Settings" tab in CL page
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#  When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then "ai" checkbox should be displayed as checked
#   Then "analytics" checkbox should be displayed as checked
#   Then "blockchain" checkbox should be displayed as checked
#   Then "compute" checkbox should be displayed as checked
#   Then "containers" checkbox should be displayed as checked
#   Then "databases" checkbox should be displayed as checked
#   Then "devops" checkbox should be displayed as checked
#   Then "integration" checkbox should be displayed as checked
#   Then "iot" checkbox should be displayed as checked
#   Then "logging_monitoring" checkbox should be displayed as checked
#   Then "migration_tools" checkbox should be displayed as checked
#   Then "mobile" checkbox should be displayed as checked
#   Then "iot" checkbox should be displayed as checked
#   Then "network" checkbox should be displayed as checked
#   Then "platform_services" checkbox should be displayed as checked
#   Then "security" checkbox should be displayed as checked
#   Then "storage" checkbox should be displayed as checked


#  Scenario: Verify checkboxes were unchecked
#   When Filter by 'rmc-1p-asc-deleteme001z'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#   When Go to "Settings" tab in CL page
#   When Uncheck "ai" checkbox
#   When Uncheck "analytics" checkbox
#   When Uncheck "blockchain" checkbox
#   When Uncheck "compute" checkbox
#   When Uncheck "containers" checkbox
#   When Uncheck "databases" checkbox
#   When Uncheck "devops" checkbox
#   When Uncheck "integration" checkbox
#   When Uncheck "iot" checkbox
#   When Uncheck "logging_monitoring" checkbox
#   When Uncheck "migration_tools" checkbox
#   When Uncheck "mobile" checkbox
#   When Uncheck "iot" checkbox
#   When Uncheck "network" checkbox
#   When Uncheck "platform_services" checkbox
#   When Uncheck "security" checkbox
#  When Uncheck "storage" checkbox
#  When Go "page up"
#   When Save button was pressed in CL page
#   Then "ai" checkbox should be displayed as unchecked
#   Then "analytics" checkbox should be displayed as unchecked
#   Then "blockchain" checkbox should be displayed as unchecked
#   Then "compute" checkbox should be displayed as unchecked
#   Then "containers" checkbox should be displayed as unchecked
#   Then "databases" checkbox should be displayed as unchecked
#   Then "devops" checkbox should be displayed as unchecked
#   Then "integration" checkbox should be displayed as unchecked
#   Then "iot" checkbox should be displayed as unchecked
#   Then "logging_monitoring" checkbox should be displayed as unchecked
#   Then "migration_tools" checkbox should be displayed as unchecked
#   Then "mobile" checkbox should be displayed as unchecked
#   Then "iot" checkbox should be displayed as unchecked
#   Then "network" checkbox should be displayed as unchecked
#   Then "platform_services" checkbox should be displayed as unchecked
#   Then "security" checkbox should be displayed as unchecked
#   Then "storage" checkbox should be displayed as unchecked


#  Scenario: Verify that json view script is equal than catalog listing page
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-deleteme010209a'
#   And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#   And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209a"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#  When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#   When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Press View Json button
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Verify that catalog listing values are equal than json script modal


#  Scenario: Verify that a resource can be published into global catalog and all values are the same
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-deleteme010209b'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209b"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#  When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#  When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#  When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#   When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get GC content values
#   Then Go to "Overview" tab in GC
#   Then Get GC overview values
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#   Then Verify that catalog listing values are equal than global catalog

#  Scenario: Verify that any update in json script from GC then values are the same in GC
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme010209d'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#  Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209d"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   When Filter by 'rmc-1p-asc-deleteme0701'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#  When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#  Then Press tree dots
#  Then Press Edit action for Json menu
#   Then Get json script values
#   Then Update Json script with "update"
#   Then Save Json script updates
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get GC content values
#   Then Go to "Overview" tab in GC
#   Then Get GC overview values
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#   Then Validate Json script agains Global Catalog

#  Scenario: Verify that global catalog update values are the same as catalog listing
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme010209e'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#  When Resource name was filled with "rmc-1p-asc-deleteme010209e"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#  When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   When Filter by 'rmc-1p-asc-deleteme0701'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Update content tab values in GC with "update"
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#   Then Go to "Overview" tab in GC
#   Then Update overview tab values in GC with "update"
#   Then Press Save button in GC
#   Then Go back to RMC page
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Press import button
#   Then Confirm import from GC
#   When Press close button from success popup
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#   When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Verify that global catalog updates are iqual than imported to catalog listing


#  Scenario: Verify json script updated is the same as catalog listing
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme010209f'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209f"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   When Filter by 'rmc-1p-asc-deleteme0701'
#   When Go to first resource from table
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#  Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Press tree dots
#  Then Press Edit action for Json menu
#  Then Get json script values
#  Then Update Json script with "update"
#  Then Save Json script updates
#   Then Go to "Overview" tab in GC
#   Then Go back to RMC page
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Press import button
#   Then Confirm import from GC
#   When Press close button from success popup
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#   When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Validate Json script from GC against catalog listing

#  Scenario: Verify json script updated is the same as json view from catalog listing
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-deleteme010209g'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209g"
#  When Shot description was filled with "ss"
#  When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#  When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#  When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#  When Instructions URL was filled with "https://ibm.com4"
#  When Support URL was filled with "https://ibm.com5"
#  When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#  When Plan Changes selected is "Yes"
#  When Require unique selected is "Yes"
#  When Resource keys selected is "Yes"
#  When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#  When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
# Then Global catalog link should be displayed
#  Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#  Then Go to global catalog page
#  Then Go to "Content" tab in GC
#  Then Press tree dots
#  Then Press Edit action for Json menu
#  Then Get json script values
# Then Update Json script with "update"
#  Then Save Json script updates
#  Then Go to "Overview" tab in GC
#  Then Go back to RMC page
#  Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#  Then Press import button
#  Then Confirm import from GC
#  When Press close button from success popup
#  When Go to "Listing Page" tab in CL page
#  Then Press View Json button
#  Then Get json script values from CL
# Then Press close button from json script modal
#  Then Verify that json script modal values are equal than json script from GC
#  Then Verify1


#  Scenario: Verify that any update in catalog listing is replied in json scrip from GC
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#  And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-deleteme010209h'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#  Then Go to 'catalog listing' tab
# When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209h"
#  When Shot description was filled with "ss"
#  When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#  When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#  When Press Add Media button in optional section
#  When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#  When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#  When Instructions URL was filled with "https://ibm.com4"
#  When Support URL was filled with "https://ibm.com5"
#  When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#  When Plan Changes selected is "Yes"
# When Require unique selected is "Yes"
#  When Resource keys selected is "Yes"
#  When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#  When Check "migration_tools" checkbox
#  When Check "mobile" checkbox
#   When Check "iot" checkbox
#  When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#  Then Global catalog link should be displayed
#   When Go to "Listing Page" tab in CL page
#   Then Updates all values from "listing page" with "update"
#  When Go to "Settings" tab in CL page
#   Then Updates all values from "settings" with "update"
#  When Save button was pressed in CL page
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#  When Go to "Settings" tab in CL page
#  When Get Settings values
#  Then Go to global catalog page
#  Then Go to "Content" tab in GC
#  Then Press tree dots
#  Then Press Edit action for Json menu
#  Then Get json script values
#  Then Press cancel button from json script
#  Then Validate Json script from GC against catalog listing
#  Then Verify1

#  Scenario: Verify that any update catalog listing are the same in global catalog
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme010209i'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#  Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#   And 'service' was selected for type
#   And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#   And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#  When Go to "Listing Page" tab in CL page
#  When Resource name was filled with "rmc-1p-asc-deleteme010209i"
#  When Shot description was filled with "ss"
#  When Author was filled with "aa"
#  When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#  When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
# When Go "page up"
#  When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#  When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#  When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#  When Go "page up"
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Updates all values from "listing page" with "update"
#   When Go to "Settings" tab in CL page
#  Then Updates all values from "settings" with "update"
#   When Save button was pressed in CL page
#   When Go to "Listing Page" tab in CL page
#  When Get Listing Page values
#   When Go to "Settings" tab in CL page
#  When Get Settings values
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get GC content values
#   Then Go to "Overview" tab in GC
#   Then Get GC overview values
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#  Then Verify that catalog listing values are equal than global catalog
#  Then Verify1



#  Scenario: Verify that any update catalog listing are the same in json view modal
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001b109'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001b109"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#  When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Updates all values from "listing page" with "update"
#   When Go to "Settings" tab in CL page
#   Then Updates all values from "settings" with "update"
#   When Save button was pressed in CL page
#   When Go to "Listing Page" tab in CL page
#   When Get Listing Page values
#   When Go to "Settings" tab in CL page
#   When Get Settings values
#   Then Press View Json button
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Verify that catalog listing values are equal than json script modal
#   Then Verify1


#  Scenario: Verify that any update in global catalog values are the same as Json script from GC
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001d3'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  When 'ga' was selected for target release level
#   And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001d3"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#   When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#  When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#  When Check "databases" checkbox
#  When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#  Then Go to "en" language tab
#   Then Update content tab values in GC with "update"
#  Then Go to "tags" tab in GC
#   Then Get GC tags values
#  Then Go to "Overview" tab in GC
#   Then Update overview tab values in GC with "update"
#   Then Press Save button in GC
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get GC content values
#   Then Go to "Overview" tab in GC
#   Then Get GC overview values
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#   Then Press tree dots
#   Then Press Edit action for Json menu
#  Then Get json script values
#  Then Press cancel button from json script
#   Then Validate Json script agains Global Catalog
#   Then Verify1


#  Scenario: Verify that any update in global catalog are the same than json script in view modal
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-deleteme010209'
#   And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme010209"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#   When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#   When media url was filled with "https://media2.com"
#   When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Check "ai" checkbox
#   When Check "analytics" checkbox
#   When Check "blockchain" checkbox
#   When Check "compute" checkbox
#   When Check "containers" checkbox
#   When Check "databases" checkbox
#   When Check "devops" checkbox
#   When Check "integration" checkbox
#   When Check "iot" checkbox
#   When Check "logging_monitoring" checkbox
#   When Check "migration_tools" checkbox
#   When Check "mobile" checkbox
#   When Check "iot" checkbox
#   When Check "network" checkbox
#   When Check "platform_services" checkbox
#   When Check "security" checkbox
#   When Check "storage" checkbox
#   When Go "page up"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Update content tab values in GC with "update"
#   Then Go to "Overview" tab in GC
#   Then Update overview tab values in GC with "update"
#   Then Press Save button in GC
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get GC content values
#   Then Go to "Overview" tab in GC
#   Then Get GC overview values
#   Then Go to "tags" tab in GC
#   Then Get GC tags values
#   Then Go to "Overview" tab in GC
#   Then Go back to RMC page
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   Then Press import button
#   Then Confirm import from GC
#   When Press close button from success popup
#   When Go to "Listing Page" tab in CL page
#   Then Press View Json button
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Validate global catalog against Json script view modal

 #  Then Verify1

#   When Filter by 'rmc-1p-asc-part01a'
#    And Go to first resource from table
#   Then Go to 'summary' tab

Feature: Summary general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login in IBMcloud web application as owner
    When Dashboard page is shown

#  Scenario: Verify that a new part can be added and it is approved if its effective date is current
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-part01v1'
#  And Select 'service' for resource type
#   And Press 'submit' buttons
#  Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#  And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#  And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-part01v1"
#  When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "Yes" from choose new experience popup
#  When Press "Next" button from choose new experience popup
#  When Select "Yes" from choose part type popup
#  When Press "Next" button from choose part type popup
#  When Select "No" from choose priced setting
#  When Press "Next" button from choose priced setting popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v1"
#  When Press "Next" button from add new part popup
#  When Select "Default" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Fill part description with "part description" for "first" part
#  When Fill product name with "product name"
#  When Fill product tradename with "product tradename"
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "ACCESS" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "access" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01v1" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01v1" part is displayed in "first" row
#  Then Verify that "DEFAULT" region is displayed for "first" row
#  Then Verify that "Roll Up Part" type is displayed for "first" row
#  Then Verify that "part-rmc-1p-asc-part01v1" part was "approved" for "first" row
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "No" from choose part type popup
#  When Press "Next" button from choose part type popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v1"
#  When Press "Next" button from add new part popup
#  When Select "global" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Select "first invoice" invoice part number
#  When Fill part description with "part description" for "second" part
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "API" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "api call" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then select "linear tier" from pricing model
#  Then Input "1" for charge unit quantity
#  Then Input "2" for usa price
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01v1" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01v1" part is displayed in "second" row
#  Then Verify that "GLOBAL" region is displayed for "second" row
#  Then Verify that "METRIC PART" type is displayed for "second" row
#  Then Verify that "part-rmc-1p-asc-part01v1" part was "approved" for "second" row


#  Scenario: Verify that a new part can be added and it is not approved if it is effective date is not today
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-part01t3'
#  And Select 'service' for resource type
#   And Press 'submit' buttons
#  Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#  And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#  And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-part01t3"
#  When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
# When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#  When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#  When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "Yes" from choose new experience popup
#  When Press "Next" button from choose new experience popup
#  When Select "Yes" from choose part type popup
# When Press "Next" button from choose part type popup
#  When Select "No" from choose priced setting
#  When Press "Next" button from choose priced setting popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01t3"
#  When Press "Next" button from add new part popup
#  When Select "Default" region from dropdown menu
#  When "Future" date was selected for effective from date
#  When Fill part description with "part description" for "first" part
#  When Fill product name with "product name"
#  When Fill product tradename with "product tradename"
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "ACCESS" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "access" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
# Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01t3" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01t3" part is displayed in "first" row
#  Then Verify that "DEFAULT" region is displayed for "first" row
#  Then Verify that "Roll Up Part" type is displayed for "first" row
#  Then Verify that "part-rmc-1p-asc-part01t3" part was "Not Approved" for "first" row


#  Scenario: Verify that a json was generated with linear tier pricing method for the second part added
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-part01v1'
#  And Select 'service' for resource type
#   And Press 'submit' buttons
# Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#  And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#  And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#  When Resource name was filled with "rmc-1p-asc-part01v1"
# When Shot description was filled with "ss"
#   When Author was filled with "aa"
#  When Detailed description was filled with "dd"
# When Service icon URL was filled with "https://ibm.com1"
# When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#  When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#  When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "Yes" from choose new experience popup
#  When Press "Next" button from choose new experience popup
#  When Select "Yes" from choose part type popup
#  When Press "Next" button from choose part type popup
#  When Select "No" from choose priced setting
#  When Press "Next" button from choose priced setting popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v1"
#  When Press "Next" button from add new part popup
#  When Select "Default" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Fill part description with "part description" for "first" part
#  When Fill product name with "product name"
#  When Fill product tradename with "product tradename"
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "ACCESS" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "access" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01v1" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01v1" part is displayed in "first" row
#  Then Verify that "DEFAULT" region is displayed for "first" row
#  Then Verify that "Roll Up Part" type is displayed for "first" row
#  Then Verify that "part-rmc-1p-asc-part01v1" part was "approved" for "first" row
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "No" from choose part type popup
#  When Press "Next" button from choose part type popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v1"
#  When Press "Next" button from add new part popup
#  When Select "global" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Select "first invoice" invoice part number
#  When Fill part description with "part description" for "second" part
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "API" from metric grouping dropdown menu
# When Click over metric dropdown menu
#  Then Select "api call" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then select "linear tier" from pricing model
#  Then Input "1" for charge unit quantity
#  Then Input "2" for usa price
#  Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Press View Json button from part page
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Get values from "first" part
#   Then Press Edit action for "first" part
#   Then Get values from define popup for "first" part
#   Then Press "close" button from part popup
#   Then Get values from "second" part
#   Then Press Edit action for "second" part
#   Then Get values from define popup for "second" part
#   Then Press "close" button from part popup
#   Then Verify that json values are equal than "first" part
#  Then Verify that json values are equal than "second" part



#  Scenario: Verify that a json was generated with simple tier pricing method for the second part added
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-part01v8'
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
#   When Resource name was filled with "rmc-1p-asc-part01v8"
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
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "Yes" from choose new experience popup
#   When Press "Next" button from choose new experience popup
#   When Select "Yes" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from choose priced setting
#   When Press "Next" button from choose priced setting popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v8"
#   When Press "Next" button from add new part popup
#   When Select "Default" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Fill part description with "part description" for "first" part
#   When Fill product name with "product name"
#   When Fill product tradename with "product tradename"
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "ACCESS" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "access" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Search "part-rmc-1p-asc-part01v8" in filter criteria field
#   Then Verify that "part-rmc-1p-asc-part01v8" part is displayed in "first" row
#   Then Verify that "DEFAULT" region is displayed for "first" row
#   Then Verify that "Roll Up Part" type is displayed for "first" row
#   Then Verify that "part-rmc-1p-asc-part01v8" part was "approved" for "first" row
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "No" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v8"
#   When Press "Next" button from add new part popup
#   When Select "global" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Select "first invoice" invoice part number
#   When Fill part description with "part description" for "second" part
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "API" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "api call" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#   Then select "Simple tier" from pricing model
#   Then Input "1" for charge unit quantity
#   Then Input "2" for usa price
#   Then Input "3" for upper limit
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Press View Json button from part page
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Get values from "first" part
#   Then Press Edit action for "first" part
#   Then Get values from define popup for "first" part
#   Then Press "close" button from part popup
#   Then Get values from "second" part
#   Then Press Edit action for "second" part
#   Then Get values from define popup for "second" part
#   Then Press "close" button from part popup
#   Then Verify that json values are equal than "first" part
#  Then Verify that json values are equal than "second" part



#  Scenario: Verify that a json was generated with simple tier pricing method for the second part added
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-part01v9'
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
#   When Resource name was filled with "rmc-1p-asc-part01v9"
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
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "Yes" from choose new experience popup
#   When Press "Next" button from choose new experience popup
#   When Select "Yes" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from choose priced setting
#   When Press "Next" button from choose priced setting popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v9"
#   When Press "Next" button from add new part popup
#   When Select "Default" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Fill part description with "part description" for "first" part
#   When Fill product name with "product name"
#   When Fill product tradename with "product tradename"
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "ACCESS" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "access" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Search "part-rmc-1p-asc-part01v9" in filter criteria field
#   Then Verify that "part-rmc-1p-asc-part01v9" part is displayed in "first" row
#   Then Verify that "DEFAULT" region is displayed for "first" row
#   Then Verify that "Roll Up Part" type is displayed for "first" row
#   Then Verify that "part-rmc-1p-asc-part01v9" part was "approved" for "first" row
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "No" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v9"
#   When Press "Next" button from add new part popup
#   When Select "global" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Select "first invoice" invoice part number
#   When Fill part description with "part description" for "second" part
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "API" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "api call" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#   Then select "Graduated tier" from pricing model
#   Then Input "1" for charge unit quantity
#   Then Input "2" for usa price
#   Then Input "3" for upper limit
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Press View Json button from part page
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Get values from "first" part
#   Then Press Edit action for "first" part
#   Then Get values from define popup for "first" part
#   Then Press "close" button from part popup
#   Then Get values from "second" part
#   Then Press Edit action for "second" part
#   Then Get values from define popup for "second" part
#   Then Press "close" button from part popup
#   Then Verify that json values are equal than "first" part
#  Then Verify that json values are equal than "second" part



#  Scenario: Verify that a json was generated with simple tier pricing method for the second part added
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-part01v11'
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
#   When Resource name was filled with "rmc-1p-asc-part01v11"
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
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "Yes" from choose new experience popup
#   When Press "Next" button from choose new experience popup
#   When Select "Yes" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from choose priced setting
#   When Press "Next" button from choose priced setting popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v11"
#   When Press "Next" button from add new part popup
#   When Select "Default" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Fill part description with "part description" for "first" part
#   When Fill product name with "product name"
#   When Fill product tradename with "product tradename"
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "ACCESS" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "access" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Search "part-rmc-1p-asc-part01v11" in filter criteria field
#   Then Verify that "part-rmc-1p-asc-part01v11" part is displayed in "first" row
#   Then Verify that "DEFAULT" region is displayed for "first" row
#   Then Verify that "Roll Up Part" type is displayed for "first" row
#   Then Verify that "part-rmc-1p-asc-part01v11" part was "approved" for "first" row
#   Then Go to 'pricing plans' tab
#   When Select "Part/Pricing Definition" tab from pricing plan
#   When Press "Add Part" button from pricing plan
#   When Select "No" from choose part type popup
#   When Press "Next" button from choose part type popup
#   When Select "No" from add new part
#   Then Part number should be "part-rmc-1p-asc-part01v11"
#   When Press "Next" button from add new part popup
#   When Select "global" region from dropdown menu
#   When "Current" date was selected for effective from date
#   When Select "first invoice" invoice part number
#   When Fill part description with "part description" for "second" part
#   When Press edit metric button
#   When Select "No" from custom metric
#   When Click over metric grouping dropdown menu
#   Then Select "API" from metric grouping dropdown menu
#   When Click over metric dropdown menu
#   Then Select "api call" from metric dropdown menu
#   When "Confirm" button was pressed from edit metric popup
#  Then select "Block tier" from pricing model
#   Then Input "1" for charge unit quantity
#   Then Input "2" for usa price
#   Then Input "3" for upper limit
#   Then Press "Publish pricing" button from part popup
#   When Press close button from success popup
#   Then Press "Save" button from part popup
#   Then Press View Json button from part page
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Get values from "first" part
#   Then Press Edit action for "first" part
#   Then Get values from define popup for "first" part
#   Then Press "close" button from part popup
#   Then Get values from "second" part
#   Then Press Edit action for "second" part
#   Then Get values from define popup for "second" part
#   Then Press "close" button from part popup
#   Then Verify that json values are equal than "first" part
#   Then Verify that json values are equal than "second" part


#  Scenario: Verify that a default pricing part that was approved then can be udpated and its status persist as approved
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#  And Fill resource name with 'rmc-1p-asc-part01v15'
#  And Select 'service' for resource type
#  And Press 'submit' buttons
#  Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#  And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#  And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-part01v15"
#  When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#  When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
# When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#  When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "Yes" from choose new experience popup
#  When Press "Next" button from choose new experience popup
#  When Select "Yes" from choose part type popup
# When Press "Next" button from choose part type popup
#  When Select "No" from choose priced setting
# When Press "Next" button from choose priced setting popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v15"
#  When Press "Next" button from add new part popup
#  When Select "Default" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Fill part description with "part description" for "first" part
#  When Fill product name with "product name"
#  When Fill product tradename with "product tradename"
#  When Press edit metric button
#  When Select "No" from custom metric
# When Click over metric grouping dropdown menu
#  Then Select "ACCESS" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "access" from metric dropdown menu
# When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
# When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01v15" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01v15" part is displayed in "first" row
#  Then Verify that "DEFAULT" region is displayed for "first" row
#  Then Verify that "Roll Up Part" type is displayed for "first" row
#  Then Verify that "part-rmc-1p-asc-part01v15" part was "approved" for "first" row
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  Then Press "Edit" action for "first" part
#  When Fill part description with "part description update" for "first" part
#  When Fill product name with "product name update"
#  When Fill product tradename with "product tradename update"
#  When Press edit metric button
# When Select "No" from custom metric
# When Click over metric grouping dropdown menu
#  Then Select "Api" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "api call" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Verify that "part-rmc-1p-asc-part01v15" part was "approved" for "first" row



#  Scenario: Verify that a default pricing part that was approved then can be udpated and the updates values are equal against json script
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#   And Fill resource name with 'rmc-1p-asc-part01v17'
#  And Select 'service' for resource type
#  And Press 'submit' buttons
#  Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#  And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#   And '84 Codes' was selected for sub-category
#  And Save button was pressed
#  And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-part01v17"
#  When Shot description was filled with "ss"
#  When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
#  When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Press Add Feature button in optional section
#   When bullet title was filled with "bullet title"
#  When bullet description was filled with "bullet description"
#   When Press Add Media button in optional section
#   When type of media option was filled with "image"
#   When thumbnail was filled with "https://media1.com"
#  When media url was filled with "https://media2.com"
#  When media caption was filled with "caption media"
#   When Go "page up"
#   When Go to "Settings" tab in CL page
#  When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#   When Provisionable selected is "Provision-Through"
#  When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#  When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  When Press "Add Part" button from pricing plan
#  When Select "Yes" from choose new experience popup
#  When Press "Next" button from choose new experience popup
#  When Select "Yes" from choose part type popup
#  When Press "Next" button from choose part type popup
#  When Select "No" from choose priced setting
#  When Press "Next" button from choose priced setting popup
#  When Select "No" from add new part
#  Then Part number should be "part-rmc-1p-asc-part01v17"
#  When Press "Next" button from add new part popup
#  When Select "Default" region from dropdown menu
#  When "Current" date was selected for effective from date
#  When Fill part description with "part description" for "first" part
#  When Fill product name with "product name"
#  When Fill product tradename with "product tradename"
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "ACCESS" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "access" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#  Then Search "part-rmc-1p-asc-part01v17" in filter criteria field
#  Then Verify that "part-rmc-1p-asc-part01v17" part is displayed in "first" row
#  Then Verify that "DEFAULT" region is displayed for "first" row
#  Then Verify that "Roll Up Part" type is displayed for "first" row
#  Then Verify that "part-rmc-1p-asc-part01v17" part was "approved" for "first" row
#  Then Go to 'pricing plans' tab
#  When Select "Part/Pricing Definition" tab from pricing plan
#  Then Press "Edit" action for "first" part
#  When Fill part description with "part description update" for "first" part
#  When Fill product name with "product name update"
#  When Fill product tradename with "product tradename update"
#  When Press edit metric button
#  When Select "No" from custom metric
#  When Click over metric grouping dropdown menu
#  Then Select "Api" from metric grouping dropdown menu
#  When Click over metric dropdown menu
#  Then Select "api call" from metric dropdown menu
#  When "Confirm" button was pressed from edit metric popup
#  Then Press "Publish pricing" button from part popup
#  When Press close button from success popup
#  Then Press "Save" button from part popup
#   Then Verify that "part-rmc-1p-asc-part01v17" part was "approved" for "first" row
#   Then Press View Json button from part page
#   Then Get json script values
#   Then Press close button from json script modal
#   Then Get values from "first" part
#   Then Press Edit action for "first" part
#   Then Get values from define popup for "first" part
#   Then Press "close" button from part popup
#   Then Verify that json values are equal than "first" part


  Scenario: Verify that a part with linear tier pricing method can be duplicated
   When Press new resource button
   Then 'Create a new resource' popup is displayed
   And 'No' for would you like to import
   And 'No' for is your resource going to be a child
   And Fill resource name with 'rmc-1p-asc-part01v06'
   And Select 'service' for resource type
   And Press 'submit' buttons
  Then Go to 'summary' tab
  When 'ga' was selected for target release level
   And '3Q2020' was selected for service framework version
   And 'Current' date was selected for release date
   And 'service' was selected for type
   And '3rd Party' was selected for offering category
   And '84 Codes' was selected for sub-category
   And Save button was pressed
   And Press close button from success popup
  Then Go to 'catalog listing' tab
  When Go to "Listing Page" tab in CL page
  When Resource name was filled with "rmc-1p-asc-part01v06"
  When Shot description was filled with "ss"
  When Author was filled with "aa"
  When Detailed description was filled with "dd"
  When Service icon URL was filled with "https://ibm.com1"
  When Documentation URL was filled with "https://ibm.com2"
  When Terms URL was filled with "https://ibm.com3"
  When Press Add Feature button in optional section
  When bullet title was filled with "bullet title"
  When bullet description was filled with "bullet description"
  When Press Add Media button in optional section
  When type of media option was filled with "image"
  When thumbnail was filled with "https://media1.com"
  When media url was filled with "https://media2.com"
  When media caption was filled with "caption media"
  When Go "page up"
  When Go to "Settings" tab in CL page
  When Management type selected is "Public"
  When Instructions URL was filled with "https://ibm.com4"
   When Support URL was filled with "https://ibm.com5"
   When Provisionable selected is "Provision-Through"
  When Bindable selected is "Yes"
   When Plan Changes selected is "Yes"
   When Require unique selected is "Yes"
   When Resource keys selected is "Yes"
  When Support email was filled with "test@test.com"
  When Custom URL was filled with "https://ibm.com6"
  When Save button was pressed in CL page
   Then Global catalog link should be displayed
  Then Go to 'pricing plans' tab
  When Select "Part/Pricing Definition" tab from pricing plan
  When Press "Add Part" button from pricing plan
  When Select "Yes" from choose new experience popup
  When Press "Next" button from choose new experience popup
  When Select "Yes" from choose part type popup
  When Press "Next" button from choose part type popup
  When Select "No" from choose priced setting
  When Press "Next" button from choose priced setting popup
  When Select "No" from add new part
  Then Part number should be "part-rmc-1p-asc-part01v06"
  When Press "Next" button from add new part popup
  When Select "Default" region from dropdown menu
  When "Current" date was selected for effective from date
  When Fill part description with "part description" for "first" part
  When Fill product name with "product name"
  When Fill product tradename with "product tradename"
  When Press edit metric button
  When Select "No" from custom metric
  When Click over metric grouping dropdown menu
  Then Select "ACCESS" from metric grouping dropdown menu
  When Click over metric dropdown menu
  Then Select "access" from metric dropdown menu
  When "Confirm" button was pressed from edit metric popup
  Then Press "Publish pricing" button from part popup
  When Press close button from success popup
  Then Press "Save" button from part popup
  Then Search "part-rmc-1p-asc-part01v06" in filter criteria field
  Then Verify that "part-rmc-1p-asc-part01v06" part is displayed in "first" row
  Then Verify that "DEFAULT" region is displayed for "first" row
  Then Verify that "Roll Up Part" type is displayed for "first" row
  Then Verify that "part-rmc-1p-asc-part01v06" part was "approved" for "first" row
  Then Go to 'pricing plans' tab
  When Select "Part/Pricing Definition" tab from pricing plan
  When Press "Add Part" button from pricing plan
  When Select "No" from choose part type popup
  When Press "Next" button from choose part type popup
  When Select "No" from add new part
  Then Part number should be "part-rmc-1p-asc-part01v06"
  When Press "Next" button from add new part popup
  When Select "global" region from dropdown menu
  When "Current" date was selected for effective from date
  When Select "first invoice" invoice part number
  When Fill part description with "part description" for "second" part
  When Press edit metric button
  When Select "No" from custom metric
  When Click over metric grouping dropdown menu
  Then Select "API" from metric grouping dropdown menu
  When Click over metric dropdown menu
  Then Select "api call" from metric dropdown menu
  When "Confirm" button was pressed from edit metric popup
  Then select "linear tier" from pricing model
  Then Input "1" for charge unit quantity
  Then Input "2" for usa price
  Then Press "Publish pricing" button from part popup
   When Press close button from success popup
   Then Press "Save" button from part popup


   Then Go to all resources link
   When Filter by 'rmc-1p-asc-part01v06'
   When Go to first resource from table


   Then Go to 'summary' tab
   Then Go to 'pricing plans' tab
   When Select "Part/Pricing Definition" tab from pricing plan

   When Press duplicate button for second part
   When Press close button from success popup
#   Then Get values from "second" part
#   Then Press Edit action for "second" part
#   Then Get values from define popup for "second" part
#   Then Press "close" button from part popup
   Then Press Edit action for "third" part
   When Select "all regions" region from dropdown menu
   Then Press "Publish pricing" button from part popup
   When Press close button from success popup
   Then Press "Save" button from part popup
   Then Get values from define popup for "third" part
   Then Press "close" button from part popup
   Then Get values from "third" part

#   Then Verify that json values are equal than "first" part
#   Then Verify that json values are equal than "second" part


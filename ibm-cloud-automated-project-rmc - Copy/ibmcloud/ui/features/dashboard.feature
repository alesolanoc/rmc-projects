
Feature: Dashboard general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login in IBMcloud web application as owner
    When Dashboard page is shown

  @functional
#  Scenario: Verify that RMC dashboard is displayed with all resources on it
#    Then 'Resource Onboarded onto IBM Cloud' should be displayed at the top
#    Then 'Filter resources by name:' should be displayed at filter section
#    Then 'New resource' button should be displayed
#    Then 'RESOURCE NAME' column header should be displayed at {first} column
#    Then 'OWNER' column header should be displayed at {second} column
#    Then 'RELEASE DATE (UTC)' column header should be displayed at {third} column
#    Then All resources are displayed
#    Then All resources should have 'resource name'
#    Then All resources should have 'owner'
#    Then Getting started popup should be displayed after clicked over its link
#    Then 'Getting started' should be displayed at the top of the popup
#    Then after pressed close button dashboard page should be displayed
#    Then Filter table should display according filter criteria 'rmc-1p-asc-deleteme010209'
#    Then first 'rmc-1p-asc-deleteme010209' resource should be equal than filter criteria 'rmc-1p-asc-deleteme010209'

#  Scenario: Verify that a resource can be removed
#    When Press new resource button
#    Then 'Create a new resource' popup is displayed
#     And 'No' for would you like to import
#     And 'No' for is your resource going to be a child
#     And Fill resource name with 'rmc-1p-asc-deleteme010210'
#     And Select 'service' for resource type
#     And Press 'submit' buttons
#    Then Go to 'summary' tab
#    Then Go to all resources link
#    When Filter by 'rmc-1p-asc-deleteme010210'
#     And The press remove icon for 'rmc-1p-asc-deleteme010210'
#    Then 'Delete confirmation required for offering:' Remove popup should be displayed
#     And 'rmc-1p-asc-deleteme010210' resource name should be displayed in order to be removed
#     And 'rmc-1p-asc-deleteme010210' resource name was confirmed
#     And Press delete button
#   Then Resource should not be displayed in dashboard


#  Scenario: Verify that a new service resource can be added
#    When Press new resource button
#    Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#   And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001b1a'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#    Then Go to 'summary' tab
#    Then 'rmc-1p-asc-deleteme001b1a' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor


#  Scenario: Verify that a new operation only resource can be added
#    When Press new resource button
#    Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001e'
#    And Select 'operations only' for resource type
#    And Press 'submit' buttons
#    Then Go to 'summary' tab
#   And 'operations_only' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor

#  Scenario: Verify that a new compsite resource and its child can be added both as service resources
#    When Press new resource button
#    Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001h9a'
#    And Select 'composite' for resource type
#    And Fill composite tag with "is"
#    And Fill contained resource types with "test"
#    And Press 'submit' buttons
#    Then Go to 'summary' tab
#    Then 'rmc-1p-asc-deleteme001h9a' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'composite' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#    And "is" should be displayed for composite tag
#    And "test" should be displayed for contained resource types
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#   And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001h9a"
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
#   Then Go to all resources link
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-deleteme001h9a"
#   Then Fill resource child name with "test"
#   Then Select 'service' for resource type
#   Then Press 'submit' buttons
#   Then Go to 'summary' tab
#   Then 'rmc-1p-asc-deleteme001h9a.test' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor

#  Scenario: Verify that a new compsite resource and its child can be added parent as service resource and child as platform service
#    When Press new resource button
#    Then 'Create a new resource' popup is displayed
#   And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001h10b'
#    And Select 'composite' for resource type
#    And Fill composite tag with "is"
#    And Fill contained resource types with "test"
#    And Press 'submit' buttons
#    Then Go to 'summary' tab
#    Then 'rmc-1p-asc-deleteme001h10b' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#   And 'composite' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#    And "is" should be displayed for composite tag
#    And "test" should be displayed for contained resource types
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-deleteme001h10b"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#  When Service icon URL was filled with "https://ibm.com1"
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
#  When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to all resources link
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-deleteme001h10b"
#   Then Fill resource child name with "test"
#   Then Select 'platform service' for resource type
#   Then Press 'submit' buttons
#   Then Go to 'summary' tab
#   Then 'rmc-1p-asc-deleteme001h10b.test' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'platform_service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor

#  Scenario: Create new resource as composite publish it after that create its child as service and publish it too
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-composite03h'
#    And Select 'composite' for resource type
#    And Fill composite tag with "is"
#    And Fill contained resource types with "test"
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03h' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'composite' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#    And "is" should be displayed for composite tag
#    And "test" should be displayed for contained resource types
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-composite03h"
#   When Shot description was filled with "ss"
#   When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Go to "Settings" tab in CL page
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
#  When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#  Then Get "composite" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "composite" reference "rmc-1p-asc-composite03h.test" "service" "is" in json script from GC
#  Then Go to "Overview" tab in GC
#  Then Go back to RMC page
#   Then Go to all resources link
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-composite03h"
#   Then Fill resource child name with "test"
#  Then Select 'service' for resource type
#   Then Press 'submit' buttons
#  Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03h.test' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
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
#   When Resource name was filled with "rmc-1p-asc-composite03h.test"
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
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get "service" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "service" reference "rmc-1p-asc-composite03h.test" "service" "is" in json script from GC


#  Scenario: Create new resource as composite publish it after that create its child as platform service and publish it too
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-composite03o'
#    And Select 'composite' for resource type
#    And Fill composite tag with "is"
#    And Fill contained resource types with "test"
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03o' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#   And 'composite' should be displayed for type
#   And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#   And "is" should be displayed for composite tag
#   And "test" should be displayed for contained resource types
#  When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#   And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#   And Press close button from success popup
#   Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-composite03o"
#   When Shot description was filled with "ss"
#  When Author was filled with "aa"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#  When Terms URL was filled with "https://ibm.com3"
#  When Go to "Settings" tab in CL page
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
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get "composite" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "composite" reference "rmc-1p-asc-composite03o.test" "service" "is" in json script from GC
#   Then Go to "Overview" tab in GC
#   Then Go back to RMC page
#   Then Go to all resources link
#  When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-composite03o"
#   Then Fill resource child name with "test"
#   Then Select 'platform service' for resource type
#   Then Press 'submit' buttons
#   Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03o.test' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'platform_service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#    And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-composite03o.test"
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
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get "service" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "platform" reference "rmc-1p-asc-composite03o.test" "platform_service" "is" in json script from GC
#   Then Go to "Overview" tab in GC


# Scenario: Create new resource as composite publish it after that create its children, first one as service and second one as platform and publish them too
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-composite03z1'
#    And Select 'composite' for resource type
#    And Fill composite tag with "is"
#    And Fill contained resource types with "test1, test2"
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#  Then 'rmc-1p-asc-composite03z1' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'composite' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
#    And "is" should be displayed for composite tag
#    And "test1, test2" should be displayed for contained resource types2
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#   And Save button was pressed
#   And Press close button from success popup
#  Then Go to 'catalog listing' tab
#   When Go to "Listing Page" tab in CL page
#   When Resource name was filled with "rmc-1p-asc-composite03z1"
#   When Shot description was filled with "ss"
#   When Detailed description was filled with "dd"
#   When Service icon URL was filled with "https://ibm.com1"
#   When Documentation URL was filled with "https://ibm.com2"
#   When Terms URL was filled with "https://ibm.com3"
#  When Go to "Settings" tab in CL page
#   When Management type selected is "Public"
#   When Instructions URL was filled with "https://ibm.com4"
#   When Support URL was filled with "https://ibm.com5"
#  When Provisionable selected is "Provision-Through"
#   When Bindable selected is "Yes"
#   When Plan Changes selected is "Yes"
#   When Require unique selected is "Yes"
#   When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
# When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#  Then Get "composite" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "multiple" reference "rmc-1p-asc-composite03z1.test" "service" "is" in json script from GC
#  Then Go to "Overview" tab in GC
#  Then Go back to RMC page
#   Then Go to all resources link
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-composite03z1"
#   Then Fill resource child name with "test1"
#  Then Select 'service' for resource type
#   Then Press 'submit' buttons
#  Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03z1.test1' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
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
#  When Resource name was filled with "rmc-1p-asc-composite03z1.test1"
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
#   Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get "service" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "service" reference "rmc-1p-asc-composite03z1.test1" "service" "is" in json script from GC
#  Then Go to "Overview" tab in GC
#  Then Go back to RMC page
#   Then Go to all resources link
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#   Then 'No' for would you like to import
#   Then 'Yes' for is your resource going to be a child
#   Then Fill resource parent name with "rmc-1p-asc-composite03z1"
#   Then Fill resource child name with "test2"
#  Then Select 'service' for resource type
#   Then Press 'submit' buttons
#  Then Go to 'summary' tab
#   Then 'rmc-1p-asc-composite03z1.test2' resource should be displayed at top
#    And 'experimental' should be displayed for target release
#    And 'service' should be displayed for type
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' account should be displayed for first contributor
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
#   When Resource name was filled with "rmc-1p-asc-composite03z1.test2"
#  When Shot description was filled with "ss"
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
#  When Resource keys selected is "Yes"
#   When Support email was filled with "test@test.com"
#   When Custom URL was filled with "https://ibm.com6"
#   When Save button was pressed in CL page
#   Then Global catalog link should be displayed
#  Then Go to global catalog page
#   Then Go to "Content" tab in GC
#   Then Go to "en" language tab
#   Then Get "service" label
#   Then Press tree dots
#   Then Press Edit action for Json menu
#   Then Get json script values
#   Then Press cancel button from json script
#   Then Validate "service" reference "rmc-1p-asc-composite03z1.test2" "service" "is" in json script from GC

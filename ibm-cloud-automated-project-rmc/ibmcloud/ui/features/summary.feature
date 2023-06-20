
Feature: Summary general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login in IBMcloud web application as owner
    When Dashboard page is shown

#  Scenario: Verify that a new contributor can be added
#    When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001b2c'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#    When Press add contributor button
#    And Fill 'test@test1.com' contributor
#    And Press add contributor
#   Then Contributor 'test@test1.com' should be displayed in contributor table

#  Scenario: Verify that a contributor can be removed
#   When Filter by 'rmc-1p-asc-deleteme001b2c'
#    And Go to first resource from table
#    Then Go to 'summary' tab
#    And Press remove contributor
#    And Press remove button
#    Then Contributor should be removed from table
#   Then Go to all resources link
#   When Filter by 'rmc-1p-asc-deleteme001b2'
#   And The press remove icon for 'rmc-1p-asc-deleteme001b2c'
#   Then 'Delete confirmation required for offering:' Remove popup should be displayed
#    And 'rmc-1p-asc-deleteme001b2c' resource name should be displayed in order to be removed
#    And 'rmc-1p-asc-deleteme001b2c' resource name was confirmed
#    And Press delete button
#   Then Resource should not be displayed in dashboard

#  Scenario: Verify that a new resouce can be added and no issue is displayed if all required fields were filled
#    When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001b3a1b'
#    And Select 'service' for resource type
#    And Press 'submit' buttons
#    Then Go to 'summary' tab
#   When 'ga' was selected for target release level
#    And '3Q2020' was selected for service framework version
#    And 'Current' date was selected for release date
#    And 'service' was selected for type
#    And '3rd Party' was selected for offering category
#    And '84 Codes' was selected for sub-category
#    And Save button was pressed
#  When Press close button from success popup
#   Then Go to all resources link
#   When Filter by 'rmc-1p-asc-deleteme001b3a1b'
#   Then 'rmc-1p-asc-deleteme001b3a1b' resource should be displayed in resouce name column
#    And 'alejandro.solano1+dev.stage1@mail.test.ibm.com' owner should be displayed in owner column
#    And 'Current' date should be displayed in release date column
#   When Go to first resource from table
#    Then Go to 'summary' tab
#   Then 'ga' '3Q2020' 'service' '3rd_Party' '84_Codes' 'current_date' inputs should be displayed

#  Scenario: Verify updates in target release level
#   When Press new resource button
#   Then 'Create a new resource' popup is displayed
#    And 'No' for would you like to import
#    And 'No' for is your resource going to be a child
#    And Fill resource name with 'rmc-1p-asc-deleteme001b66a'
#   And Select 'service' for resource type
#    And Press 'submit' buttons
#   Then Go to 'summary' tab
#   When 'experimental' was selected for target release level
#   And Save button was pressed
#   When Press close button from success popup
#  Then Current maturity is "Current maturity: New" for "EXPERIMENTAL"
#   Then Target maturity is "Target maturity: Experimental" for "EXPERIMENTAL"
#   When 'beta' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#   Then Label at top is "EXPERIMENTAL" for "BETA"
#    Then Current maturity is "Current maturity: Experimental" for "BETA"
#    Then Target maturity is "Target maturity: Beta" for "BETA"
#   When 'ga' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#  Then Label at top is "BETA" for "GA0"
#   Then Current maturity is "Current maturity: Beta" for "GA0"
#    Then Target maturity is "Target maturity: Catalog Min (GA)" for "GA0"
#   When '3Q2020' was selected for service framework version
#   When 'Current' date was selected for release date
#   When 'ga' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#   Then Label at top is "GA" for "GA"
#   Then Current maturity is "Current maturity: Catalog Min (GA)" for "GA"
#    Then Target maturity is "Target maturity: One Cloud" for "GA"
#   When 'experimental' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#   Then Current maturity is "Current maturity: New" for "EXPERIMENTAL"
#   Then Target maturity is "Target maturity: Experimental" for "EXPERIMENTAL"
#   When 'beta' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#   Then Label at top is "EXPERIMENTAL" for "BETA"
#    Then Current maturity is "Current maturity: Experimental" for "BETA"
#    Then Target maturity is "Target maturity: Beta" for "BETA"
#   When 'future' date was selected for release date
#   When 'ga' was selected for target release level
#    And Save button was pressed
#   When Press close button from success popup
#   Then Label at top is "BETA" for "GA0"
#   Then Current maturity is "Current maturity: Beta" for "GA0"
#   Then Target maturity is "Target maturity: Catalog Min (GA)" for "GA0"


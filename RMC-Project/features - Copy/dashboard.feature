Feature: validate dashboard page

    Scenario: Verify that dashboard page is displayed
      Then Title label should be displayed
      Then Filter label should be displayed
      Then Filter input field should be displayed
      Then Resource name header should be displayed
      Then Owner header should be displayed
      Then Release date header should be displayed
      Then New resource button should be displayed
      Then All resource should be displayed
      Then Getting started popup is displayed after clicked getting started link

#    Scenario: Create new resource
#      Given New resource button was pressed
#      When Create new resource popup is displayed
#      Then Would you like to import your services from your service broker "No"
#      Then Is your resource going to be a child of a composite parent service "No"
#      Then Fill resource name "service"
#      Then Select resource type "service"
#      Then Press Submit button
#      Then New resource "Service" should be displayed in summary page

#    Scenario: Validate required fields in summary page
#      Given filter a resource by name: "service"
#      When summary page is displayed
#      When GA was selected for Target release level
#      When 3Q2020 was selected for Service Framework Version
#      When A date was selected for Release date
#      When "Service" type was selected
#      When 3rd Party was selected for Offering category
#      When 84 Codes was selected for Sub-category
#      Then Success message should be displayed after pressed save button
#      Then Go back to resource list
#      Given filter a resource by name: "service"
#      When summary page is displayed
#      Then Required fields should be displayed filled in summary page


#  Scenario: Validate if a contributor can be added
#      Given filter a resource by name: "service"
#      When summary page is displayed
#      When owner of the resource should be the same user as logged
#      When Press Add button
#      Then Add contributor popup is displayed
#      When filled a new contributor
#      When Pressed Add button
#      Then a new contributor should be added and displayed in contributor table

#  Scenario: Validate if a contributor can be removed
#  Given filter a resource by name: "service"
#      When summary page is displayed
#      When go to contributor section and select remove icon for the second row
#      When confirm remove
#      Then the contributor should be removed


#  Scenario: Validate required fields in catalog listing page
#     Given filter a resource by name: "service"
#      When summary page is displayed
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "service"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required unique
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      Then Go back to resource list
#      Given filter a resource by name: "service"
#      When summary page is displayed
#      Then Required fields should be displayed filled in catalog listing page

#  Scenario: Validate if a bullet can be added
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      When Add feature button was pressed
#      Then Bullet can be added
#      When save button is pressed

#  Scenario: Validate if a bullet can be removed
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      When remove a bullet
#      When save button is pressed

#  Scenario: Validate if a media can be added
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      When Add media button was pressed
#      Then Media can be added
#      When save button is pressed

#  Scenario: Validate if a media can be removed
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      When remove a media
#      When save button is pressed


#  Scenario: Validate JSon view against catalog listing page
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "service"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required unique
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When Go to listing page tab
#      When Add feature button was pressed
#      Then Bullet can be added
#      When Add media button was pressed
#      Then Media can be added
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      When pressed view json button
#      Then json editor modal should be displayed
#      Then validate catalog listing page against json view modal



#   Scenario: Validate json script against global catalog
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "service"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required unique
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When Go to listing page tab
#      When Add feature button was pressed
#      Then Bullet can be added
#      When Add media button was pressed
#      Then Media can be added
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      When pressed view json button
#      Then json editor modal should be displayed
#      Then validate catalog listing page against json view modal
#      Then get catalog list values
#      Then go to global catalog
#      Then validate catalog listing page against global catalog
#      Then select three dots
#      Then select edit option of three dots dropdown menu
#      Then update json script in json editor
#      Then get global catalog values
#      Then validate global catalog page against global catalog json script


#   Scenario: Validate json script against catalog listing
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When go to global catalog and update JSon script
#      When Import from global catalog
#      Then get catalog list values
#      Then go to global catalog
#      Then validate catalog listing page against global catalog

#   Scenario: Validate global catalogt against catalog listing
#      Given filter a resource by name: "service"
#      When Go to catalgo listing page
#      When go to global catalog and update its values
#      Then get global catalog values
#      When Import from global catalog
#      Then get catalog list values
#      Then go to global catalog
#      Then validate catalog listing page against global catalog


#   Scenario: Validate that a resource can be removed
#      Given filter a resource to be removed
#      Then press remove icon
#      Then confirm remove
#      Then resource should not be displayed in dashboard

#    Scenario: Create new resource as operations only
#      Given New resource button was pressed
#      When Create new resource popup is displayed
#      Then Would you like to import your services from your service broker "No"
#      Then Is your resource going to be a child of a composite parent service "No"
#      Then Fill resource name "operations only"
#      Then Select resource type "Operations only"
#      Then Press Submit button
#      Then New resource "Operations only" should be displayed in summary page


#    Scenario: Create new resource as composite publish it after that create its child and publish it too
#      Given New resource button was pressed
#      When Create new resource popup is displayed
#      Then Would you like to import your services from your service broker "No"
#      Then Is your resource going to be a child of a composite parent service "No"
#      Then Fill resource name "composite"
#      Then Select resource type "Composite Service"
#      Then Fill composite tag
#      Then Fill contained resource types
#      Then Press Submit button
#      Then New resource "Composite Service" should be displayed in summary page
#      When GA was selected for Target release level
#      When 3Q2020 was selected for Service Framework Version
#      When A date was selected for Release date
#      When "composite service" type was selected
#      When 3rd Party was selected for Offering category
#      When 84 Codes was selected for Sub-category
#      Then Success message should be displayed after pressed save button
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "composite"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required unique
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When Go to listing page tab
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      Then Go back to resource list
#      Given New resource button was pressed
#      When Create new resource popup is displayed
#      Then Would you like to import your services from your service broker "No"
#      Then Is your resource going to be a child of a composite parent service "Yes"
#      Then Fill resource name "parent"
#      Then Select resource type "service"
#      Then Press Submit button
#      Then New resource "child" should be displayed in summary page
#      When GA was selected for Target release level
#      When 3Q2020 was selected for Service Framework Version
#      When A date was selected for Release date
#      When "Service" type was selected
#      When 3rd Party was selected for Offering category
#      When 84 Codes was selected for Sub-category
#      Then Success message should be displayed after pressed save button
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "child"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required uniqu
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When Go to listing page tab
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      Then Go back to resource list
#      Then filter a resource by parent
#      When Go to catalgo listing page
#      Then go to global catalog
#      Then select three dots
#      Then select edit option of three dots dropdown menu
#      Then validate that json script has "child" "service" reference



#   Scenario: Create new resource as service and validate translationc
#      Given New resource button was pressed
#      When Create new resource popup is displayed
#      Then Would you like to import your services from your service broker "No"
#      Then Is your resource going to be a child of a composite parent service "No"
#      Then Fill resource name "service"
#      Then Select resource type "Service"
#      Then Press Submit button
#      When GA was selected for Target release level
#      When 3Q2020 was selected for Service Framework Version
#      When A date was selected for Release date
#      When "service" type was selected
#      When 3rd Party was selected for Offering category
#      When 84 Codes was selected for Sub-category
#      Then Success message should be displayed after pressed save button
#      When Go to catalgo listing page
#      When Go to listing page tab
#      Then resource name should be filled "service"
#      Then short description should be filled
#      Then author should be filled
#      Then detailed description should be filled
#      Then service icon url should be filled
#      Then documentation url should be filled
#      Then terms of agreenment should be filled
#      When Go to settings tab
#      Then from management type dropdown menu select public
#      Then instruction url should be filled
#      Then supported url should be filled
#      Then select yes for bindable
#      Then select yes for required unique
#      Then select yes for provisionable
#      Then select yes for plan changes
#      Then select yes for resource type API
#      Then support email should be filled
#      Then custom provisioning url should be filled
#      When Go to listing page tab
#      When Add feature button was pressed
#      Then Bullet can be added
#      When Add media button was pressed
#      Then Media can be added
#      When Go to listing page tab
#      When save button is pressed
#      Then success message is displayed and review offering in global catalog is displayed
#      Then select translation option
#      Then expand translation json sample
#      Then copy translation from json sample
#      Then paste json example into json editor
#      Then save json script
#      Then press close button
#      When Go to catalgo listing page
#      When Import from global catalog
#      Then get catalog list values
#      Then go to global catalog
#      Then validate catalog listing page against global catalog


#   Scenario: Create new resource as service and validate translationc with new language
#      Given filter a resource by name
#      Then select translation option
#      Then expand translation json sample
#      Then copy translation from json sample
#      Then paste json example into json editor with new language
#      Then save json script
#      Then press close button
#      When Go to catalgo listing page
#      Then go to global catalog
#      Then go to "en" language tab
#      Then get global catalog values from "en" to be compared with translations
#      Then validate "en" translate language against global catalog
#      Then go to "fr" language tab
#      Then get global catalog values from "fr" to be compared with translations
#      Then validate "fr" translate language against global catalog

#   Scenario: Validate access iam
#      Given filter a resource by name: "service"
#      When Go to access iam page
#      When Go to required tab
#      When Select "yes" for iam integration settings
#      When Press save button for for iam integration settings
#      When Press enable IAM button
#      Then validate that status is approved "enabling"

   Scenario: Verify status popupe
      Given filter a resource by name: "service"
      When Go to access iam page
      When Go to required tab
      Then Click status button
      Then validate that status is approved "status"

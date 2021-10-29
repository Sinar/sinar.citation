# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.citation -t test_citation.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.citation.testing.SINAR_CITATION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/citation/tests/robot/test_citation.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Citation
  Given a logged-in site administrator
    and an add Citation form
   When I type 'My Citation' into the title field
    and I submit the form
   Then a Citation with the title 'My Citation' has been created

Scenario: As a site administrator I can view a Citation
  Given a logged-in site administrator
    and a Citation 'My Citation'
   When I go to the Citation view
   Then I can see the Citation title 'My Citation'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Citation form
  Go To  ${PLONE_URL}/++add++Citation

a Citation 'My Citation'
  Create content  type=Citation  id=my-citation  title=My Citation

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Citation view
  Go To  ${PLONE_URL}/my-citation
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Citation with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Citation title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

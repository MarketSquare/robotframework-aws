## SUITE NAME
--name AWS Testing Demo

## SETTINGS
# tools must be in same directory as run_arguments.robot
--pythonpath ./AWSLibrary
--pythonpath .

# LOG LEVEL
# --loglevel DEBUG
--loglevel INFO

# put all logs into directory
--outputdir reports
# --timestampoutputs
--debugfile debug.log

## TEST BROWSER
# -v BROWSER:chrome
# -v BROWSER:c
# -v DISPLAY_WIDTH:1920
# -v DISPLAY_HEIGHT:1080

## VIRTUAL DISPLAY
# -v USE_XVFB:False
-v USE_XVFB:True

## PROXY
-v USE_PROXY:False
-v PROXY_TYPE:socks
-v PROXY_HOST:localhost
-v PROXY_PORT:9999

## VARIABLES
# -v REPO_PATH:data/ui_elements.yml

## CONFIGURATION
# use `config_stack1.py` of `config_stack2.py`
# -V config_stack1.py

## EXCLUDE
# --exclude monitoring
# --test Manage Email Notifications
## TEST SUITES
# run single test suite
test.robot

# run all test suites
# ./tests
*********************************
Guide for Contributing & Workflow
*********************************

Testing
#######

For every method or keyword, there shall be a unit test written in parrallel. All unit tests will be stored in
tests/unit, following the convention of test_{name of class}.py

Next, create a TestCase for the keyword created in robotframework. These tests are found in tests/robot/testsuites and follow
the same naming convention.

Create an run_arguments.robot file at the root of the robot directory and configure your settings as such.

:: run_arguments.robot
## SUITE NAME
--name AWS Library Testing

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

## VIRTUAL DISPLAY
-v USE_XVFB:True

## PROXY
-v USE_PROXY:False
-v PROXY_TYPE:socks
-v PROXY_HOST:localhost
-v PROXY_PORT:9999

## VARIABLES
-v ACCESS_KEY: AKIAVXUJU3VU6VEYSHJD
-v SECRET_KEY: PQxrDqUwjC9wtetHSICI1OKBW1cGSE8ar8Sxce9f

testsuites/

For robot tests to run, configure your AWS Credentials in run_arguments.robot in the variables section

.. code-block:: python
   # variables
   -v ACESS_KEY: your-key-here
   -v SECRET_KEY: your-key-here

Tests are automated with Tox and will run upon pushing to the branch.

.. code-block:: bash
   $ tox
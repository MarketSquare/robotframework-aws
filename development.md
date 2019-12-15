# GUIDE FOR DEVELOPMENT WORKFLOW



####  TESTING

For every keyword or method created, will be followed with two different tests. Unit and Robot tests.
Located in the tests directory are seperated tests by type unit/robot.

Robot Tests will need a configuration file added to the root of robot/ for tests to run.

run_arguments.robot
```
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
-v ACCESS_KEY:
-v SECRET_KEY:

testsuites/
```

make sure and add your aws credentials in the variables section.


Unit tests and Robot Tests are automated with tox. You can run tox to test your build before committing your changes
```
tox
```

Upon pushing your branch. Tox will run and travis ci will run the reports

### Pre Commit Checks

Flake8

Git Secrets - No hardcoded AWS Credentials

Trailing White Spaces

Check YAML syntax


### Dependency Management

pip tools

add dependency to requirements.in like so

```
dependency==0.0.1
```

Then run to compile into requirements.txt

```
pip-compile output-file=requirements.txt requirements.in
```



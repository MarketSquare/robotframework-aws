# ***** UNDER CONSTRUCTION *****

## Contributing to RobotFramework-AWS

Thank you for considering contributing to a library for interacting with AWS Services in RobotFramework for Test Automation.

Let's go over setting up the development environment.

Setup virtualenvironment:

```sh
python -m venv venv
```

activate

```sh
source venv/bin/activate
```

install dependencies

```sh
pip install -r requirements.txt
```

set environment variables for aws as ACCESS_KEY and SECRET_KEY

install package development setup from root directory where setup.py is

```sh
pip install -e .
```

## TESTING

For every keyword or method created, will be followed with two different tests. Unit and Robot tests.
Located in the tests directory are separated tests by type unit/robot.

Robot Tests will need a configuration file added to the root of robot/ for tests to run.

`run_arguments.robot`

```robotframework
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

## Local AWS Services with Localstack

```sh
docker-compose up -d

```

<http://localhost:8055/>

Make sure and add your aws credentials in the variables section.

Unit tests and Robot Tests are automated with tox. You can run tox to test your build before committing your changes

```sh
tox
```

Upon pushing your branch. Tox will run and travis ci will run the reports

Tox will grab the AWS environment variables that you set. which you can see in tox.ini

### Pre Commit

We use flake8 for checking for linting errors

Git Secrets will run on commit to make sure there are no hardcoded credentials in any files

Upon pushing your branch. Tox will run and travis ci will run the reports

### Issues

Feel free to create issues for ideas for new functionality with other aws services

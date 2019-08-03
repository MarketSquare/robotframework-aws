*********************************
Guide for Contributing & Workflow
*********************************

Testing
#######

For every method or keyword, there shall be a unit test written in parrallel. All unit tests will be stored in
tests/unit, following the convention of test_{name of class}.py

Next, create a TestCase for the keyword created in robotframework. These tests are found in tests/robot/testsuites and follow
the same naming convention.

For robot tests to run, configure your AWS Credentials in run_arguments.robot in the variables section

.. code-block:: python
   :linenos:

   # variables
   -v ACESS_KEY: your-key-here
   -v SECRET_KEY: your-key-here

Tests are automated with Tox and will run upon pushing to the branch.
```
    Tox
    
```
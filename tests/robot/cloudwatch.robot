*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${LOG_GROUP}      test


*** Test Cases ***
Test Wait For Log
    [Tags]    cloudwatch
    [Setup]    keywords.Send Cloudwatch Message    Hello From CloudWatch
    ${logs}    CloudWatch Wait For Logs    ${LOG_GROUP}    " "    Hello.*Watch    timeout=10
    Should Not Be Empty    ${logs}
    Should Contain    ${logs}[0]    Hello From CloudWatch

Test Log Insights
    [Tags]    cloudwatch
    [Setup]    keywords.Send Cloudwatch Message    Hello From CloudWatch
    Sleep    30s    #You need to wait for the log to be indexed in cloudwatch for the query to work
    ${query}    Set Variable    fields @message | filter @message like 'Hello' | sort @timestamp desc | limit 10
    ${logs}    CloudWatch Logs Insights    ${LOG_GROUP}    ${query}
    Should Not Be Empty    ${logs}

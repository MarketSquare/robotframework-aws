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
    ${logs}    CloudWatch Wait For Logs    ${LOG_GROUP}    " "    Hello    timeout=10
    Should Not Be Empty    ${logs}
    Should Contain    ${logs}[0]    Hello From CloudWatch

Test Log Insights
    [Tags]    cloudwatch
    [Setup]    keywords.Send Cloudwatch Message    Hello From CloudWatch
    ${logs}    CloudWatch Logs Insights    ${LOG_GROUP}    fields @message | filter @message like 'Hello' | sort @timestamp desc | limit 10
    Should Not Be Empty    ${logs}
    Should Contain    ${logs}[0]    Hello From CloudWatch
#!/bin/bash

# Hook file to create resources in localstack
awslocal sqs create-queue --queue-name test-queueName
echo succesfully created queue
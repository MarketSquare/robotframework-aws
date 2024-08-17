#!/bin/bash

# Hook file to create resources in localstack
awslocal sqs create-queue --queue-name test-queueName
awslocal s3api create-bucket --bucket test-bucket
echo succesfully created services

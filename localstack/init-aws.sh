#!/bin/bash

# Hook file to create resources in localstack
awslocal sqs create-queue --queue-name test-queueName
awslocal s3api create-bucket --bucket test-bucket
awslocal s3api create-bucket --bucket test-bucket-2
echo succesfully created services

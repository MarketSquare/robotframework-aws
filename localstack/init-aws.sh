#!/bin/bash

# Hook file to create resources in localstack
awslocal sqs create-queue --queue-name test-queueName
awslocal s3api create-bucket --bucket test-bucket-1
awslocal s3api create-bucket --bucket test-bucket-2
awslocal dynamodb create-table \
    --table-name storage \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region us-east-1
awslocal dynamodb create-table \
    --table-name music \
    --key-schema \
    AttributeName=Artist,KeyType=HASH \
    AttributeName=SongTitle,KeyType=RANGE \
    --attribute-definitions \
    AttributeName=Artist,AttributeType=S \
    AttributeName=SongTitle,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region us-east-1
echo succesfully created services

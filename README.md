# AmplifyLogsToS3
A Lambda that gets AWS Amplify logs and pushes them to an S3 bucket.

## Permissions Required

`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "amplify:*",
            "Resource": "*"
        }
    ]
}`

Also attach AmazonS3FullAccess and AWSLambdaBasicExecutionPolicy to your IAM role.

## Lambda Setup
1. 128MB RAM
2. 2 minute timeout

Setup a CloudWatch to do this say every week. 

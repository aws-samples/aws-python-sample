# AWS SDK for Python Sample Project

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as `boto3`).

## Requirements

This sample project depends on `boto3`, the AWS SDK for Python, and requires
Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` using pip:

    pip install boto3

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. For more information on configuring `boto3`,
check out the Quickstart section in the [developer guide](https://boto3.readthedocs.org/en/latest/guide/quickstart.html).

## Running the S3 sample

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
creates a bucket, and uploads a file to that bucket. The script will generate a
bucket name and file for you. All you need to do is run the code:

    python s3_sample.py

You need to make sure the credentials you're using have the correct permissions to access the Amazon S3 
service. If you run into 'Access Denied' errors while running this sample, please follow the steps below.

1. Log into the [AWS IAM Console](https://console.aws.amazon.com/iam/home)
2. Navigate to the Users page.
3. Find the AWS IAM user whose credentials you're using.
4. Under the 'Permissions' section, attach the policy called 'AmazonS3FullAccess'
5. Re-run the sample. Now your user should have the right permissions to run the sample.

The sample creates randomly generated bucket names for you, but please be aware of the [restrictions for bucket names](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) when you start creating your own buckets.

## License

This sample application is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).


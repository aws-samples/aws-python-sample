# AWS SDK for Python Sample Project

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as Boto).

## Requirements

This sample project depends on Boto, the AWS SDK for Python, and requires
Python 2.6 or 2.7. You can install Boto using pip:

    pip install boto

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(C:\Users\USER_NAME\.aws\ for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. It's also possible to configure your
credentials via other configuration files. See the [Boto Config documentation](http://boto.readthedocs.org/en/latest/boto_config_tut.html)
for more information.

## Running the S3 sample

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
creates a bucket, and uploads a file to that bucket. The script will generate a
bucket name and file for you. All you need to do is run the code:

    python s3_sample.py

The S3 documentation has a good overview of the [restrictions for bucket names](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)
for when you start making your own buckets.

## Debugging

### Access Denied
If you are seeing an __Access Denied__ error when the sample script tries to crete a new bucket,
it is most likely because their is an issue with your AWS IAM (Idenity and Access Management).
Follow the steps below to work resolve this issue:
1. Visit your [AWS IAM Console](https://console.aws.amazon.com/iam/home)
2. Select "Users" on the right hand side and follow the instructions to create a new user
   + Retrieve the access keys for this user and put them under ~/.aws/console
3. Select "Groups" on the right and side and follow the instructions to crete a new group
   + Make sure it has the __AdministratorAccess__ policy added
   + Add the user you created in step 2 to the group you create in step 3
4. Try re-running the script

## License

This sample application is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).


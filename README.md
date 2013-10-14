# AWS SDK for Python Sample Project

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as Boto).

## Requirements

This sample project depends on Boto, the AWS SDK for Python, and requires
Python 2.6 or 2.7. You can install Boto using pip:

    pip install boto

## Basic Configuration

You need to set your AWS security credentials before the sample is able to
connect to AWS. The SDK will automatically pick up credentials in environment
variables:

    export AWS_ACCESS_KEY_ID="Your AWS Access Key ID"
    export AWS_SECRET_ACCESS_KEY="Your AWS Secret Access Key"

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. It's also possible to configure your
credentials via a configuration file. See the [Boto Config documentation](http://boto.readthedocs.org/en/latest/boto_config_tut.html)
for more information.

## Running the S3 sample

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
creates a bucket, and uploads a file to that bucket. The script will generate a
bucket name and file for you. All you need to do is run the code:

    python s3_sample.py

The S3 documentation has a good overview of the [restrictions for bucket names](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)
for when you start making your own buckets.

## License

This sample application is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).


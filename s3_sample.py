# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import the SDK
import boto3
import uuid

# boto3 offers two different styles of API - Resource API (high-level) and
# Client API (low-level). Client API maps directly to the underlying RPC-style
# service operations (put_object, delete_object, etc.). Resource API provides
# an object-oriented abstraction on top (object.delete(), object.put()).
#
# While Resource APIs may help simplify your code and feel more intuitive to
# some, others may prefer the explicitness and control over network calls
# offered by Client APIs. For new AWS customers, we recommend getting started
# with Resource APIs, if available for the service being used. At the time of
# writing they're available for Amazon EC2, Amazon S3, Amazon DynamoDB, Amazon
# SQS, Amazon SNS, AWS IAM, Amazon Glacier, AWS OpsWorks, AWS CloudFormation,
# and Amazon CloudWatch. This sample will show both styles.
#
# First, we'll start with Client API for Amazon S3. Let's instantiate a new
# client object. With no parameters or configuration, boto3 will look for
# access keys in these places:
#
#    1. Environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)
#    2. Credentials file (~/.aws/credentials or
#         C:\Users\USER_NAME\.aws\credentials)
#    3. AWS IAM role for Amazon EC2 instance
#       (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

s3client = boto3.client('s3')

# Everything uploaded to Amazon S3 must belong to a bucket. These buckets are
# in the global namespace, and must have a unique name.
#
# For more information about bucket name restrictions, see:
# http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html
bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
print('Creating new bucket with name: {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

# Now the bucket is created, and you'll find it in your list of buckets.

list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))

# Files in Amazon S3 are called "objects" and are stored in buckets. A
# specific object is referred to by its key (i.e., name) and holds data. Here,
# we create (put) a new object with the key "python_sample_key.txt" and
# content "Hello World!".

object_key = 'python_sample_key.txt'

print('Uploading some data to {} with key: {}'.format(
    bucket_name, object_key))
s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'Hello World!')

# Using the client, you can generate a pre-signed URL that you can give
# others to securely share the object without making it publicly accessible.
# By default, the generated URL will expire and no longer function after one
# hour. You can change the expiration to be from 1 second to 604800 seconds
# (1 week).

url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)

try:
    input = raw_input
except NameError:
    pass
input("\nPress enter to continue...")

# As we've seen in the create_bucket, list_buckets, and put_object methods,
# Client API requires you to explicitly specify all the input parameters for
# each operation. Most methods in the client class map to a single underlying
# API call to the AWS service - Amazon S3 in our case.
#
# Now that you got the hang of the Client API, let's take a look at Resouce
# API, which provides resource objects that further abstract out the over-the-
# network API calls.
# Here, we'll instantiate and use 'bucket' or 'object' objects.

print('\nNow using Resource API')
# First, create the service resource object
s3resource = boto3.resource('s3')
# Now, the bucket object
bucket = s3resource.Bucket(bucket_name)
# Then, the object object
obj = bucket.Object(object_key)
print('Bucket name: {}'.format(bucket.name))
print('Object key: {}'.format(obj.key))
print('Object content length: {}'.format(obj.content_length))
print('Object body: {}'.format(obj.get()['Body'].read()))
print('Object last modified: {}'.format(obj.last_modified))

# Buckets cannot be deleted unless they're empty. Let's keep using the
# Resource API to delete everything. Here, we'll utilize the collection
# 'objects' and its batch action 'delete'. Batch actions return a list
# of responses, because boto3 may have to take multiple actions iteratively to
# complete the action.

print('\nDeleting all objects in bucket {}.'.format(bucket_name))
delete_responses = bucket.objects.delete()
for delete_response in delete_responses:
    for deleted in delete_response['Deleted']:
        print('\t Deleted: {}'.format(deleted['Key']))

# Now that the bucket is empty, let's delete the bucket.

print('\nDeleting the bucket.')
bucket.delete()

# For more details on what you can do with boto3 and Amazon S3, see the API
# reference page:
# https://boto3.readthedocs.org/en/latest/reference/services/s3.html

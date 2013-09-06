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
import boto
import uuid

# Create an S3 client
s3 = boto.connect_s3()

# Create a new bucket.
bucket_name = "python-sdk-sample-" + str(uuid.uuid4())
print "Creating new bucket with name: " + bucket_name
bucket = s3.create_bucket(bucket_name)

# Upload some data
from boto.s3.key import Key
k = Key(bucket)
k.key = 'hello_world.txt'

print "Uploading some data to " + bucket_name + " with key: " + k.key
k.set_contents_from_string('This is a test of S3. Hello World!')

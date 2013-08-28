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
k.set_contents_from_string('This is a test of S3. Hellow World!')

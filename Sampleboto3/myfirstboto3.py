import boto3
# Create an S3 client
s3 = boto3.client('s3')
# List all bucketsresponse = s3.list_buckets()
print('Existing buckets:')
for bucket in s3.list_buckets()['Buckets']:
    print(f'  {bucket["Name"]}')    

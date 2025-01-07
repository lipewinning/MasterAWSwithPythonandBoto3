import boto3

s3 = boto3.client('s3')
resource = boto3.resource('s3')

outBucket = resource.Bucket(name='com.felipe.popuxo.out')

paginator = s3.get_paginator('list_objects_v2')

results = paginator.paginate(Bucket=outBucket.name)

for item in results.search('Contents'):
    #print(item)
    print(item['Key'])
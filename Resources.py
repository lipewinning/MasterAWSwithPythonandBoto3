import boto3

resource = boto3.resource('s3')

print('buckets: ')
for bucket in resource.buckets.all():
    print(bucket)

outBucket = resource.Bucket(name='com.felipe.popuxo.out')

outBucket.upload_file(Filename='myFile.txt',Key='myFile')

print('out s3 files: ')
for obj in outBucket.objects.all():
    print(obj)

#outBucket.download_file(Filename='some_new_downloaded_file.txt', Key='myFile')

rt = outBucket.objects.filter(Prefix='my')
print(rt)
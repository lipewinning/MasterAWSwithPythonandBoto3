import boto3

location = {'LocationConstraint': 'eu-west-1'}
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

client = boto3.client('s3')

#s3.create_bucket(Bucket='com.felipe.popuxo.out',
#                 CreateBucketConfiguration=location)


#with open('myfile.txt', 'w') as file:
#    file.write('This is a text file for upload.')

#client.upload_file(Filename='myfile.txt',
#               Bucket='com.felipe.popuxo.input',
#               Key='test-upload-file')

#client.download_file(Bucket='com.felipe.popuxo.input',
#                     Key='test-upload-file',
#                     Filename='FromS3myfile.txt')

client.delete_object(Bucket='com.felipe.popuxo.input',
                     Key='test-upload-file')

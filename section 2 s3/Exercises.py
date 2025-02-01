import boto3

location = {'LocationConstraint': 'eu-west-1'}

client = boto3.client('s3')

for bucket in client.list_buckets()['Buckets']:
    print(bucket['Name'])


#client.create_bucket(Bucket='com.felipe.popuxo.exercise',
#                      CreateBucketConfiguration=location)


#f = open('myFileExercise.txt', 'a')
##f.write(' exercices ')
#f.close()

#client.upload_file('myFileExercise.txt','com.felipe.popuxo.exercise','exerciseFileKey')

#contents = client.list_objects(Bucket='com.felipe.popuxo.exercise')['Contents']

#for obj in contents:
#    print(obj['Key'])

#print(client.generate_presigned_url('get_object',
#                              Params={'Bucket':'com.felipe.popuxo.exercise',
#                                      'Key':'exerciseFileKey'},
#                             ExpiresIn=120))

#for obj in contents:
#    file_name = obj['Key']
#    if '.' not in file_name:
#        file_name = file_name + '.txt'
#
#    client.download_file('com.felipe.popuxo.exercise',obj['Key'], file_name)


#for obj in contents:
#    client.delete_object(Bucket='com.felipe.popuxo.exercise',Key=obj['Key'])

#client.delete_bucket(Bucket='com.felipe.popuxo.exercise')


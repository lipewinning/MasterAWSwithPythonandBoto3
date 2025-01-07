import boto3


resource = boto3.resource('s3')

bucket = resource.Bucket('myFirstBucket')

#delete the content inside the bucket
bucket.objects.all().delete()


client = boto3.client('s3')

#delete the bucket
client.delete_bucket(Bucket='myFirstBucket')
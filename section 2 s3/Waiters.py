import boto3

bucket_name='com.felipe.popuxo.123'

client = boto3.client('s3')

waiter = client.get_waiter('bucket_exists')

wait_config = {'Delay':10, 'MaxAttempts':30}

print(f'WAITING FOR THE BUCKET: {bucket_name}')

waiter.wait(Bucket=bucket_name,WaiterConfig=wait_config)

print(f'THE BUCKET HAS BEEN MADE')
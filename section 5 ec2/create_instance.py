import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    ImageId='ami-05edf2d87fdbd91c1'     #look up console 
)
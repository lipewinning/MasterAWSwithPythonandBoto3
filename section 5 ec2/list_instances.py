import boto3


ec2 = boto3.resource('ec2')

instances = ec2.instances.all()

print(list(instances))

client = boto3.client('ec2')
description = client.describe_instances(InstanceIds=['i-0bb264d3666d638a6'])

print(description)
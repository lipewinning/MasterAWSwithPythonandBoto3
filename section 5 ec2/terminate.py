import boto3

client = boto3.client('ec2')
client.terminate_instances(InstanceIds=['i-0bb264d3666d638a6'])

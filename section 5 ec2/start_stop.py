import boto3

client = boto3.client('ec2')
description = client.describe_instances(InstanceIds=['i-0bb264d3666d638a6'])
state = description['Reservations'][0]['Instances'][0]['State']
print(state['Name'])

if 'running' in state['Name']:
    client.stop_instances(InstanceIds=['i-0bb264d3666d638a6'])
    print('Stopping')
else:
    if 'stopped' in state['Name']:
        client.start_instances(InstanceIds=['i-0bb264d3666d638a6'])
        print('Starting')


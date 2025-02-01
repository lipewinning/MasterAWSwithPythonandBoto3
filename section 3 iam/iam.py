import boto3

iamclient = boto3.client('iam')

#users = iamclient.list_users()
#print(users['Users'][0])

#groups = iamclient.list_groups()
#print(groups)


#response = iamclient.create_user(UserName='newUserForTest')
#users = iamclient.list_users()
#print(users)


#result = iamclient.add_user_to_group(UserName='newUserForTest', GroupName='testBoto3-s3-read-only')
#print(result)

#result_group_removal = iamclient.remove_user_from_group(UserName='newUserForTest', GroupName='testBoto3-s3-read-only')
#print(result_group_removal)

result_user_removal = iamclient.delete_user(UserName='newUserForTest')


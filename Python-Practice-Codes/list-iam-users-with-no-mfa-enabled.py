# Boto3 code to list iam users whose mfa is not enabled
# first list the iam users then from users fetech the mfa device list where we pass the users, 
# in there we check the MFADevices parameter value, if its empty no mfa set for the user, there is no 
# boto3 mehtod to directly fetch this value from the list_user fucntion

import boto3
from pprint import pprint

aws_console = boto3.session.Session(profile_name="default")
aws_service = boto3.client("iam")

user_with_mfa_disabled = []
users_list = aws_service.list_users()
#pprint(users_list)
for usr in users_list['Users']:
    #print(usr['UserName'])
    iam = boto3.client('iam')
    mfa_devices_lst = iam.list_mfa_devices(UserName=usr['UserName'])
    #print(f"MFA devices for user {usr['UserName']} is -", mfa_devices_lst['MFADevices'])
    if mfa_devices_lst['MFADevices'] == []:
        user_with_mfa_disabled.append(usr['UserName'])
    else:
        continue
users_count = len(user_with_mfa_disabled)
print(f"There are {users_count} users whose MFA has not been enabled are -",user_with_mfa_disabled)

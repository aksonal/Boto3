#List all the IAM users in my AWS account

import boto3 #import boto3 to interact with aws
import json

aws_console = boto3.session.Session(profile_name= "default") #fetches AWS management console in terms of UI
iam_resource_resource = aws_console.resource("iam") #resource object
iam_resource_client = aws_console.client("iam") #client object

#for resource
# for users in iam_resource_resource.users.all():
#     print("Users:",users.name)

# Pretty-print the full dictionary
response = iam_resource_client.list_users()
#This command takes a Python dictionary (in this case, the response from boto3.client('iam').list_users()), and converts it into a nicely 
#formatted JSON string that can be printed or logged.
#print(json.dumps(response, indent=4, default=str)) 


#for client
for users in iam_resource_client.list_users()["Users"]:
    print("Users:",users["UserName"])

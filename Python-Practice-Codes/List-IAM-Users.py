#List all the IAM users in my AWS account

import boto3 #import boto3 to interact with aws

aws_console = boto3.session.Session(profile_name= "default") #fetches AWS management console in terms of UI
iam_resource = aws_console.resource("iam") #in here instructing to go to IAM resource in the AWS console

for users in iam_resource.users.all():
    print("Users:",users.name)

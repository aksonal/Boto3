#list all the running ec2 instances in your aws account

import boto3
import json

aws_console = boto3.session.Session(profile_name="default")
aws_service = boto3.client(service_name="ec2",region_name="us-west-1")

response = aws_service.describe_instance_status()
#print(json.dumps(response, indent=4, default=str))

for inst in response["InstanceStatuses"]:
    print("Running instances are :",inst["InstanceId"],"and instance statu is:",inst["InstanceState"]["Name"])

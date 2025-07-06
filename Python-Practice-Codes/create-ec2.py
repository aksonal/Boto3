#create ec2 instances using boto3

import boto3

aws_console = boto3.session.Session(profile_name='default')
aws_service=boto3.client('ec2')

ec2_inst=aws_service.run_instances(
    InstanceType = "t2.micro",
    SubnetId = "subnet-0cd063a54dwe234r5",
    SecurityGroupIds = ["sg-0dfe50a63de1cer43"],
    MaxCount=3,
    MinCount=1,
    ImageId='ami-020cba7c55dfde345'
)

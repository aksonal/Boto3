#Boto3 to stop all running ec2 instances in a region.
#Steps : 
#- list down all currently running instances in the region
#- stop those runing instances

import boto3

aws_console = boto3.session.Session(profile_name='default')
aws_service = boto3.client('ec2')

#list all running instances
ec2_lst = aws_service.describe_instance_status()

for inst in ec2_lst['InstanceStatuses']:
    inst_ids_list = inst["InstanceId"]
    #print(inst_ids_list)

    ec2=boto3.client('ec2')
    ec2_to_be_stopped = ec2.stop_instances(
        InstanceIds=[inst_ids_list]
    )

    print("Instances stopped are - ",inst_ids_list)


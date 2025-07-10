#lambda function to check if ebs volume is of type other then gp3 i.e gp2, convert the vol to gp3

import boto3

aws_console=boto3.session.Session(profile_name="default")
aws_service=aws_console.client(service_name="ec2",region_name="us-east-1")

vol_list = [] #empty vol list
volumes=aws_service.describe_volumes() #list all volumes

for vol in volumes['Volumes']:
    #print(vol['VolumeType'])
    if vol['VolumeType'] != 'gp3':
        vol_list.append(vol['VolumeId'])
print("Volumes which are not of type gp3 are:",vol_list) 

#by default, this vol will update the iops, throughput, values to min req
if vol_list != []:
    for vol_id in vol_list:
        vol_types = aws_service.modify_volume(VolumeId=vol_id,VolumeType="gp3")
        print(f"Volume id {vol_id} has been updated to vol type gp3")
else:
    print("No volumes found whose vol type is anything other than gp3")

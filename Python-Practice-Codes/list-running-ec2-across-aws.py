# can we list all running ec2 instances in a particular aws account (across all regions)

import boto3
import json

aws_console = boto3.session.Session(profile_name="default")
ec2 = aws_console.client("ec2")

list_regions=ec2.describe_regions(AllRegions=False) # Optional: use AllRegions=False to get enabled only regions in AWS
#print(json.dumps (list_regions, indent=4, default=str))

for region in list_regions['Regions']:
    #print("Regions:",region['RegionName'])
    regions_list = region['RegionName']
    #print(regions_list)

    ec2 = aws_console.client("ec2",region_name=regions_list)
    list_ec2 = ec2.describe_instance_status()

    for instance in list_ec2['InstanceStatuses']:
        print("Instance id is:",instance["InstanceId"],"and instance region is:",regions_list, "with status as,",instance["InstanceState"]["Name"])




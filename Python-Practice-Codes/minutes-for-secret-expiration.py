#lambda function to send an alert when secret is going to expire.

import boto3
from pprint import pprint
from datetime import datetime, timezone, timedelta

#Env Var
SECRET_NAME = "test-secret-sonal"
VALIDITY_MINUTES = 5

aws_console = boto3.session.Session(profile_name='default')
aws_service = boto3.client('secretsmanager')

#this method gives you the current secret value for a specific version (default: the one labeled AWSCURRENT), along with basic info:
secret=aws_service.get_secret_value(
    SecretId= SECRET_NAME
)
#pprint(secret)
#print("Secret Last Creation Date :",secret['CreatedDate'])

creation_date=secret['CreatedDate']
creation_date_utc = creation_date.astimezone(timezone.utc)
print("Secret Creation Time in UTC :",creation_date_utc)

#calculate expiry date
expiry_date = creation_date_utc + timedelta(minutes=VALIDITY_MINUTES)

print("Expiry-Date in UTC :",expiry_date)
now = datetime.now(timezone.utc) #This line gets the current UTC datetime
#now = datetime.now()
print("Current time now in UTC:",now)
minutes_left= expiry_date - now
print(minutes_left)
#print("Minutes n seconds left :",minutes_left)
minutes = int(minutes_left.total_seconds())
print(minutes)
min = minutes // 60
sec = minutes % 60
#Use an f-string (formatted string) to actually interpolate the values:This substitutes the actual values of min and sec into the string.
final_time = f"{min}:{sec:02d}"
#print("Time left in UTC:",min)
print(f"Time left: {final_time}") #:02d ensures seconds always show as two digits (e.g., 1:03 not 1:3)  

if minutes < 0:
    print(f"Secret '{SECRET_NAME}' EXPIRED {-min}:{abs(sec):02d} mins ago! (Created: {creation_date})")
elif minutes == 0:
    print(f"Secret '{SECRET_NAME}' expires NOW! (Created: {creation_date})")
else:
    print(f"Secret '{SECRET_NAME}' will expire in {final_time} mins. (Created: {creation_date})")




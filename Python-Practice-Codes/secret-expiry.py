#lambda function to send an alert when secret is going to expire.
#here, I am just going to print a msg for now

import boto3
from pprint import pprint
from datetime import datetime, timezone, timedelta

#Env Var
SECRET_NAME = "test-secret-sonal"
VALIDITY_DAYS = 90

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
expiry_date = creation_date + timedelta(days=VALIDITY_DAYS)
print("Expiry-Date in UTC :",expiry_date)
now = datetime.now(timezone.utc) #This line gets the current UTC datetime
#now = datetime.now()
print("Current time now in UTC:",now)

time_left = expiry_date - now
#print(time_left)
days = time_left.days
#print(days)

if days < 0:
    #abs() returns the absolute value of days_left, i.e., it removes the sign (–) and gives you a positive number.
    print(f"Secret '{SECRET_NAME}' EXPIRED '{abs(days)}' days ago! (Created: '{creation_date}')")
elif days == 0:
    print(f"Secret '{SECRET_NAME}' expires TODAY! (Created: '{creation_date}'")
else:
    print(f"Secret {SECRET_NAME} will expire in {days} days. (Created: {creation_date})")   

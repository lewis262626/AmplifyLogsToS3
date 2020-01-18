import json
import boto3
import urllib.request
from datetime import date

BUCKET_NAME = "test"
DOMAIN_NAME = "www.google.com"
APPID = "12345554"

def lambda_handler(event, context):
    
    NAME = str(date.today()) + "-" + "access-logs"
    
    client = boto3.client('amplify')
    response = client.generate_access_logs(
        domainName=DOMAIN_NAME,
        appId=APPID
        )
    
    if response is None:
        raise ValueError("Response was empty")
    
    logUrl = response['logUrl']
    
    urllib.request.urlretrieve(logUrl, '/tmp/' + NAME)
    
    
    s3_client = boto3.client("s3", region_name="eu-west-1")
    s3_client.upload_file('/tmp/' + NAME, BUCKET, NAME + '.csv')
    
    return {
        'statusCode': 200,
        'body': json.dumps("Successful")
    }

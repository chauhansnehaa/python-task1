import json
import boto3
from botocore.exceptions import ClientError

def send_Email(event, context):
    print("Event received:", event)  
    body = json.loads(event['body'])
    receiver_email = body['receiver_email']
    subject = body['subject']
    body_text = body['body_text']

    SENDER = "snehachauhan3005@gmail.com"

    AWS_REGION = "ap-south-1"

    SUBJECT = subject

    BODY_TEXT = body_text

    CHARSET = "UTF-8"

    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    receiver_email,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
        print("Email sent! Message ID:", response['MessageId'])  
    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])  
        return {
            "statusCode": 500,
            "body": json.dumps({"message": e.response['Error']['Message']})
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!"})
        }

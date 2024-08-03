import json
import boto3
from botocore.exceptions import ClientError

def send_email(event, context):
    try:
        body = json.loads(event['body'])
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        # Replace with your "From" address. This address must be verified with Amazon SES in production.
        SENDER = "snehachauhan3005@gmail.com"

        # Replace with your AWS region
        AWS_REGION = "ap-south-1"

        CHARSET = "UTF-8"

        # Create SES client
        client = boto3.client('ses', region_name=AWS_REGION, endpoint_url='http://localhost:4566')

        # Send email
        response = client.send_email(
            Destination={
                'ToAddresses': [receiver_email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=SENDER,
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!", "messageId": response['MessageId']})
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": e.response['Error']['Message']})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }

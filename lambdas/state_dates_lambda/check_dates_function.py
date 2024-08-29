import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

"""
E-mail
"""
# Initialize AWS clients
def send_email(subject, message, to_addresses):
    ses_client = boto3.client("ses", region_name="eu-central-1")

    try:
        ses_client.send_email(
            Destination={
                "ToAddresses": to_addresses,
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": "UTF-8",
                        "Data": message,
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source="info@devsaynode.ch",
        )
        print("Email sent successfully.")
    except ClientError as e:
        print("Error sending email:", e)


'''
DATES
'''
def get_today_info(file_name):
    today_str = datetime.today().strftime('%Y-%m-%d')  # Get today's date as a string in the format YYYY-MM-DD
    
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            today_info = data.get(today_str)  # Retrieve info for today's date
            
            if today_info:  # If there is information for today
                return today_info
            else:
                return "No information for today."
    
    except FileNotFoundError:
        return "No data found."


"""
Lambda
"""
#METER NOTIFICAÇÕES
def check_dates(event, context):
    
    try:
        today_info = get_today_info("state_dates_lambda/json_files/global_dates_info.json")

        if today_info == "No information for today.":
            pass
        else:
            print('Obrigacoes hoje:',len(today_info))
            for date in today_info:
                print('Nome:',date['nome'])
                print('Resumo:', date['resumo'])
    except FileNotFoundError:
        return "No data found."
    return {"statusCode": 200, "body": json.dumps("Dates processed.")}

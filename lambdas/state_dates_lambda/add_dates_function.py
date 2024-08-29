import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

"""
JSON
"""
def save_date_info(file_name, date_str, info):
    
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if date_str in data:
        if isinstance(data[date_str], list):  # Check if the current value is a list
            data[date_str].append(info)
        else:
            data[date_str] = [data[date_str], info]  # Convert to list if not already
    else:
        data[date_str] = [info]  # Create a new list with the info

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
        

"""
Lambda
"""


def check_dates(event, context):

    request_body = event.get("body")
    if not request_body:
        return {
            "isBase64Encoded" : False,
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
            },
            "body": "No JSON data found in the request body",
        }

    # Convert the request body to a dictionary
    if isinstance(request_body, str):
        if request_body.strip() == "":
            return {
                "isBase64Encoded" : False,
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
                },
                "body": "Empty request body",
            }
        try:
            request_body_dict = json.loads(request_body)
        except json.JSONDecodeError:
            return {
                "isBase64Encoded" : False,
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
                },
                "body": "Invalid JSON format in the request body",
            }
    elif isinstance(request_body, dict):
        request_body_dict = request_body
    else:
        return {
            "isBase64Encoded" : False,
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
            },
            "body": "Invalid request body format",
        }

    # Retrieve vin and user address from the request body
    date_str = request_body_dict.get("date_str")
    info = request_body_dict.get("info")
    
    try:
        save_date_info('json_files/global_dates_info.json', date_str, info)
    except FileNotFoundError:
        return "No data found."
    return {"statusCode": 200, "body": json.dumps("Dates processed.")}

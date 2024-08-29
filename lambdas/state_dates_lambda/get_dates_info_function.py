'''
Gets the info for a date (requested by the frontend)
'''
import json
from datetime import datetime

def get_info_by_date(event, context):
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

    try:
        with open('json_files/global_dates_info.json', 'r') as file:
            data = json.load(file)
            print('in')
            date_info = data.get(date_str)  # Retrieve info for the inputted date
            
            if date_info:  # If there is information for the inputted date
                return date_info
            else:
                return f"No information for {date_str}."
    
    except FileNotFoundError:
        return "No data found."
    
print(get_info_by_date("2024-08-20"))
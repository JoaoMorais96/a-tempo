import json
from datetime import datetime

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

# Example usage:
today_info = get_today_info("checkprojectbalances-lambda/json_files/global_dates_info.json")
print('Obrigacoes hoje:',len(today_info))
for date in today_info:
    print('Nome:',date['nome'])
    print('Resumo:', date['resumo'])

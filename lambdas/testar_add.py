import json
from datetime import datetime

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

# Example usage:
date_str = "2024-08-20"
info = {"nome": "IUC",
            "resumo": "Pagar o Imposto Unico de Circulaçao",
            "onde": "https://iva.portaldasfinancas.gov.pt/driva/portal/entregar-declaracao#!"}
save_date_info("checkprojectbalances-lambda/json_files/global_dates_info.json", date_str, info)

# date_str = "2024-08-27"
# info = {"nome": "4ro Trimestre IVA",
#             "resumo": "Fazer a declaracao trimestral do IVA para o 4ro trimestre",
#             "onde": "https://iva.portaldasfinancas.gov.pt/driva/portal/entregar-declaracao#!"}
# save_date_info("checkprojectbalances-lambda/json_files/global_dates_info.json", date_str, info)

# date_str = "2024-08-26"
# info = {"nome": "5ro Trimestre IVA",
#             "resumo": "Fazer a declaracao trimestral do IVA para o 5ro trimestre",
#             "onde": "https://iva.portaldasfinancas.gov.pt/driva/portal/entregar-declaracao#!"}
# save_date_info("checkprojectbalances-lambda/json_files/global_dates_info.json", date_str, info)

from flask import Flask, jsonify, request
from datetime import datetime
import os # interact with operating system

app = Flask(__name__)

processed_data = []  # To store processed data

def processar_dados(file_paths): # Function to process data from file
    if not file_paths: 
        return jsonify({"error": "Nenhum arquivo informado"}), 400 # If file path is empty, return error (validation)
    
    for file_paths in file_paths:
        if not os.path.isfile(file_paths):
            return jsonify({"error": f"Arquivo inexistente: {file_paths}"}), 404  # If file doesn't exist, return error (validation)  

        with open(file_paths, 'r') as file:
            lines = file.readlines()  # Read each line 
        
    users_data = {}

    for line in lines:  # Extract data from each line
        user_id = line[:10].lstrip('0')  # Line[:10] = dividing each line into specific fields based on character positions.
        name = line[10:55].strip()
        order_id = line[55:65].lstrip('0')  # Lstring = remove leading zeros
        product_id = line[65:75].lstrip('0')
        total = float(line[75:87])
        date_str = line[87:].strip()

        # Formatting date
        try:
           purchase_date = datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Formato de data inválido"}), 400  # If date format is invalid, return error (validation)

        # If user_id yet doesn't exist, create a new user
        if user_id not in users_data:
            users_data[user_id] = {
                'user_id': user_id,
                'name': name,
                'orders': {}
            }

        # If order_id yet doesn't exist, create a new order
        if order_id not in users_data[user_id]['orders']:
            users_data[user_id]['orders'][order_id] = {
                'order_id': order_id,
                'date': purchase_date,
                'products': [],
                'total': 0
            }

        # Add product to order
        users_data[user_id]['orders'][order_id]['products'].append({
            'product_id': product_id,
            'value': "{:.2f}".format(total)  
        })

        # Assign total to order
        users_data[user_id]['orders'][order_id]['total'] += total

    processed_data.extend(users_data.values())  # Add processed data to global variable
    return jsonify({"message": "Dados processados com sucesso"}), 200  





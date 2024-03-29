from flask import Flask, jsonify, request, render_template
from datetime import datetime
import os # Interact with the operating system

app = Flask(__name__)

processed_data = []  # To store processed data

def process_data(file_paths):  # Function to process data from file
    if not file_paths: 
        return jsonify({"error": "Nenhum arquivo informado"}), 400  # If file path is empty, return error (validation)
    
    processed_data.clear()  # Clear processed data before processing new files
    
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            return jsonify({"error": f"Arquivo inexistente: {file_path}"}), 404  # If file doesn't exist, return error (validation)

        users_data = {}  # Initialize users_data for each file

        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read each line
        
        for line in lines:  # Extract data from each line
            user_id = line[:10].lstrip('0')  # Line[:10] = dividing each line into specific fields based on character positions.
            name = line[10:55].strip()  # Strip() = remove white spaces
            order_id = line[55:65].lstrip('0')  # Lstring() = remove leading zeros
            product_id = line[65:75].lstrip('0')
            total = float(line[75:87])
            date_str = line[87:].strip()
            purchase_date = datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
                      
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
                    'total': 0,
                    'products': [],
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

# Function to filter data based on parameters
def filter_data(user_data, order_id, start_date, end_date):
    filtered_orders = {}
    for order in user_data['orders'].values():
        if (order_id is None or order['order_id'] == order_id) and \
           (start_date is None or order['date'] >= start_date) and \
           (end_date is None or order['date'] <= end_date):
            filtered_orders[order['order_id']] = order
    return filtered_orders

# API routes for data processing
@app.route('/process', methods=['GET'])
def process_data_api():
    file_paths = request.args.getlist('file_paths')  # Path to the file to be processed    
    return process_data(file_paths)  # Call the function to process the data

# API route for exibing data
@app.route('/display', methods=['GET'])
def display_data(): 
    # Parameters for filtering 
    order_id = request.args.get('order_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not processed_data:
        return jsonify({"error": "Nenhum dado processado ainda"}), 404

    # Validate order_id
    if order_id:
        order_ids = {order['order_id'] for user_data in processed_data for order in user_data['orders'].values()}
        if order_id not in order_ids:
            return jsonify({"error": f"ID do pedido não encontrado: {order_id}"}), 404

    # Validate date format
    if start_date:
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": f"Data de início inválida: {start_date}"}), 400

    if end_date:
        try:
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": f"Data de término inválida: {end_date}"}), 400

    # Filter data based on parameters
    filtered_data = {}
    for user_data in processed_data:
        orders = filter_data(user_data, order_id, start_date, end_date)
        if orders:
            user_data_copy = user_data.copy()
            user_data_copy['orders'] = list(orders.values())
            filtered_data[user_data['user_id']] = user_data_copy

    # Arround total value 
    for user_data in filtered_data.values():
        for order in user_data['orders']:
            order['total'] = round(order['total'], 2)
            
    return jsonify(list(filtered_data.values()))

# Route for Frontend
@app.route('/')
def front_init():
    return render_template('init.html')



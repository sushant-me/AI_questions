from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = {
    'items': [
        {'id': 1, 'name': 'Item 1', 'description': 'Description of Item 1'},
        {'id': 2, 'name': 'Item 2', 'description': 'Description of Item 2'}
    ]
}

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    data['items'].append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    update_data = request.get_json()
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item:
        item.update(update_data)
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data['items'] = [item for item in data['items'] if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
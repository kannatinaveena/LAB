from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Dummy database
users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Simple validation
    if not name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    # Save user to the dummy database
    users.append({
        'name': name,
        'email': email,
        'password': password
    })

    print("Registered Users:", users)  # Debugging purpose
    return jsonify({'message': 'User registered successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, jsonify, send_from_directory
from . import app, bcrypt
from .models import get_db_connection
import mysql.connector

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'signup.html')

@app.route('/signin_page')
def signin_page():
    return send_from_directory(app.static_folder, 'signin.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "User created successfully."}), 201

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    username = data['username']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and bcrypt.check_password_hash(user['password'], password):
        return jsonify({"message": "Login successful."})
    else:
        return jsonify({"message": "Invalid username or password."}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

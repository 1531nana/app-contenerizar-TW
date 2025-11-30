from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    """Establece conexión con la base de datos MySQL"""
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'user'),
                password=os.getenv('DB_PASSWORD', 'userpassword'),
                database=os.getenv('DB_NAME', 'linktree_db')
            )
            print("Conexión a la base de datos exitosa")
            return connection
        except mysql.connector.Error as err:
            print(f"Intento {attempt + 1} de {max_retries} fallido: {err}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

@app.route('/getMyInfo')
def getMyInfo():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        # Obtener los datos del usuario desde la base de datos
        cursor.execute("SELECT * FROM user_info LIMIT 1")
        user_data = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        if user_data:
            value = {
                "name": user_data['name'],
                "lastname": user_data['lastname'],
                "socialMedia": {
                    "facebookUser": user_data['facebook_user'],
                    "instagramUser": user_data['instagram_user'],
                    "xUser": user_data['x_user'],
                    "linkedin": user_data['linkedin_user'],
                    "githubUser": user_data['github_user']
                },
                "blog": user_data['blog'],
                "author": user_data['author']
            }
            return jsonify(value)
        else:
            return jsonify({"error": "No se encontraron datos"}), 404
            
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
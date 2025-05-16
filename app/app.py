from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="postgres-service",
            database="flaskdb",
            user="flaskuser",
            password="flaskpass"
        )
        return "Connected to PostgreSQL successfully!"
    except:
        return "Failed to connect to PostgreSQL."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

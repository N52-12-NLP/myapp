from flask import Flask, render_template, request
import os
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host='c.projekt-cloud-computing.postgres.database.azure.com',
    port='5432',
    user='citus',
    password='123QWEasd',
    database='citus'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        cur = conn.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cur.execute(query, (name, email))
        conn.commit()
        cur.close()


        return "Data received successfully!"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

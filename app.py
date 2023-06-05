from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Perform any desired processing or data storage here
        # For simplicity, we'll just print the values
        
        print(f"Name: {name}")
        print(f"Email: {email}")

        return "Data received successfully!"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

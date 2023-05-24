from flask import Flask, render_template, request, redirect, url_for
from botocore.exceptions import NoCredentialsError
import json
import boto3
import psycopg2

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'S': float(request.form['S']),
            'K': float(request.form['K']),
            'T': float(request.form['T']) / 365,
            'r': float(request.form['r']),
            'q': float(request.form['q']),
            'sigma': float(request.form['sigma']),
        }
        file_name = 'input.json'
        with open(file_name, 'w') as f:
            json.dump(data, f)
        s3.upload_file(file_name, 'swe590s3bucket', file_name)
        return redirect(url_for('data')) 
    else:
        return render_template('index.html')



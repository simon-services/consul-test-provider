from flask import Flask
import requests
import os
 
app = Flask(__name__)
 
@app.route('/')
def get_testdata():
    return '{"service":"consul-test-provider", "provider": "consul-test-provider"}\n'
 
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5001)

from flask import Flask, render_template, make_response
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(render_template(
        "index.html",
        patients=random.randint(15, 60),
        status="SECURE",
        updated=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        version="1.0"
    ))

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
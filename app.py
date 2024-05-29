#!/usr/bin/env python3
""" A simple API utilizing MinIO SDK to fetch bucket data.

How to use:
    Add a '.env' file with the MinIO credentials.

Execution:
    python3 app.py
    or
    ./app.py

"""

from flask import Flask
from config import configure_app
from routes import initialize_routes

app = Flask(__name__)
configure_app(app)
initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
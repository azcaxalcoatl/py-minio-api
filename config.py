from dotenv import load_dotenv
import os
from minio import Minio

def configure_app(app):
    load_dotenv()
    app.config['MINIO_SERVER'] = os.getenv('minio_server')
    app.config['MINIO_ACCESS_KEY'] = os.getenv('access_key')
    app.config['MINIO_SECRET_KEY'] = os.getenv('secret_key')

def get_minio_client():
    load_dotenv()
    client = Minio(
        os.getenv('minio_server'),
        access_key=os.getenv('access_key'),
        secret_key=os.getenv('secret_key'),
        secure=True
    )
    return client
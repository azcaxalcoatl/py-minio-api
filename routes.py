from flask import request, jsonify
from utils import get_bucket_size
from config import get_minio_client

client = get_minio_client()

def initialize_routes(app):

    @app.route('/', methods=['GET'])
    def home():
        return "API is working."

    @app.route('/list', methods=['GET'])
    def list_buckets():
        buckets = client.list_buckets()
        bucket_list = [{"name": bucket.name, "creation_date": bucket.creation_date} for bucket in buckets]
        return jsonify({"buckets": bucket_list})

    @app.route('/space', methods=['POST'])
    def bucket_space():
        data = request.get_json()
        bucket_name = data.get('bucket')
        if not bucket_name:
            return jsonify({"error": "Bucket name is missing"}), 400

        bucket_size = get_bucket_size(client, bucket_name)
        bucket_size = bucket_size / (1024**3)
        bucket_size = round(bucket_size, 2)
        return jsonify({"bucket_size": bucket_size})
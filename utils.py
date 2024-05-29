from minio.error import S3Error

def get_bucket_size(client, bucket_name):
    size = 0
    try:
        objects = client.list_objects(bucket_name, recursive=True)
        for obj in objects:
            size += obj.size
    except S3Error as e:
        print(f"Error retrieving bucket size {bucket_name}: {e}")
    return size
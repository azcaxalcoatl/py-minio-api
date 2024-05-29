# py-minio-api
A simple API utilizing MinIO SDK to fetch bucket data.

This project provides a simple API to manage and monitor storage usage in MinIO buckets. It is designed to help users list all buckets and retrieve the storage usage of individual buckets, facilitating billing and management of storage space.

## Features
- **List Buckets**: An endpoint to list all buckets created in the MinIO server.
- **Bucket Usage**: An endpoint to retrieve the name and space used by a specified bucket in GB.

## Endpoints
### `/list_buckets`

- **Method**: GET
- **Description**: Lists all buckets created in the MinIO server.
- **Response**:
```json
 {
    "buckets": [
        {
            "creation_date": "Thu, 23 May 2024 19:47:14 GMT",
            "name": "deer-bucket"
        },
        {
            "creation_date": "Thu, 23 May 2024 19:32:08 GMT",
            "name": "duck-bucket"
        }
    ]
}
```

### `/usage_bucket`
- **Method**: POST
- **Description**: Lists all buckets created in the MinIO server.
- **Request Body**:
```json
{
  "bucket_name": "deer-bucket"
}
```
- **Response**:
```json
{
    "bucket_size": 95.13
}
```

## Installation
1. Clone the repository:
```sh
git clone https://github.com/azcaxalcoatl/py-minio-api
```

2.	Navigate to the project directory:
```sh
cd py-minio-api
```

3.	Build the Docker image:
```sh
docker build -t py-minio-api:0.1 .
```

4. Run the Docker container:
```sh
docker run -d -p 5000:5000 py-minio-api:0.1
```
from azure.storage.blob import BlobServiceClient, ContainerClient
import os
import time
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get connection string and other sensitive info from .env
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")
local_photos_path = os.getenv("LOCAL_PHOTOS_PATH")

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Check if the container exists and create it if not
try:
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    if "ContainerAlreadyExists" in str(e):
        print(f"Container '{container_name}' already exists.")
    else:
        raise e

def upload_blob_in_chunks(blob_client, file_path, chunk_size=4*1024*1024):  # 4 MB chunks
    with open(file_path, "rb") as data:
        while True:
            chunk = data.read(chunk_size)
            if not chunk:
                break
            blob_client.upload_blob(chunk, overwrite=True, blob_type="BlockBlob")

def upload_with_retries(blob_client, file_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            upload_blob_in_chunks(blob_client, file_path)
            print(f"{file_path} uploaded successfully!")
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print(f"Failed to upload {file_path} after {max_retries} attempts.")

# Upload each file in the local_photos_path directory
for root, dirs, files in os.walk(local_photos_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        blob_name = os.path.relpath(file_path, local_photos_path)  # Maintain directory structure in the blob
        blob_client = container_client.get_blob_client(blob_name)
        
        print(f"Uploading {file_path} to {blob_name} in Azure Blob Storage...")
        
        upload_with_retries(blob_client, file_path)

print("All files have been uploaded.")

from flask import render_template, request, redirect, url_for, Blueprint
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

# Define the Blueprint
main = Blueprint('main', __name__)

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")

# Initialize BlobServiceClient using connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('folder_path')  # Retrieve the list of uploaded files
    
    for file in files:
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file.stream.read(), overwrite=True)  # Upload the file
        print(f"{file.filename} uploaded successfully!")

    return redirect(url_for('main.index'))  # Redirect after upload

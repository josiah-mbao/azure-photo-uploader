Photo Backup to Azure Blob Storage
Overview
This project provides a cost-effective solution for backing up photos from an iPhone to Azure Blob Storage using Python. The motivation behind this project was to overcome the storage limitations of iCloud's free plan, which only offers 5GB of storage, while avoiding the ongoing costs associated with paid cloud storage plans. By utilizing Azure Blob Storage, which offers flexible and scalable storage solutions, this project allows users to securely store large amounts of data at a potentially lower cost.

Motivation
During a recent holiday back in my country, Zambia, I encountered a problem: my iPhone's storage, as well as my iCloud storage, were completely full, preventing me from taking any more photos. I was on iCloud's free plan, which offers 5GB of storage, and my photos app was consuming around 25GB. The cheapest paid plan offered by iCloud is $1 per month for 50GB of storage. Instead of opting for the paid plan, I decided to create this project to upload my photos to Azure Blob Storage, leveraging my knowledge from studying for the Azure Fundamentals (AZ-900) certification.

Features
Automated Photo Upload: The script automatically uploads photos from a specified local directory to an Azure Blob Storage container.
Scalable Storage: By using Azure Blob Storage, users can store large amounts of data without worrying about running out of space.
Cost Efficiency: This solution offers a cost-effective alternative to iCloud's paid storage plans, with Azure providing flexible pricing based on actual usage.
Python-Powered: The project is implemented in Python, demonstrating proficiency in scripting and cloud service integration.
Prerequisites
Python 3.x: Ensure you have Python installed on your machine.

Azure Account: You'll need an Azure account to create a storage account and blob container.

Azure Storage Blob Python SDK: Install this package using pip:

bash
Copy code
pip install azure-storage-blob
Setup
Transfer Photos to Your Computer:

Connect your iPhone to your computer and transfer the photos you want to back up.
Azure Blob Storage Configuration:

Create a storage account and a blob container in Azure.
Obtain the connection string for your Azure Storage account.
Clone the Repository:

Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/photo-backup-to-azure.git
cd photo-backup-to-azure
Configure the Script:

Open the backup_photos.py script and update the following variables:
connection_string: Your Azure Storage connection string.
container_name: The name of your Azure Blob container.
local_directory: The path to the directory containing your photos.
Run the Script:

Execute the script to start uploading your photos to Azure Blob Storage:
bash
Copy code
python backup_photos.py
Usage
This script is designed to be run manually when you want to back up your photos. It can be extended to include additional features such as automatic backups, logging, and error handling.

Future Enhancements
Automation: Schedule the script to run automatically at regular intervals using cron jobs or task schedulers.
Error Handling: Improve error handling to deal with network interruptions and other potential issues.
User Interface: Develop a simple GUI or CLI to make the tool more user-friendly.
Compression: Add an option to compress photos before uploading to save on storage costs.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, feel free to contact me via LinkedIn or open an issue on this repository.

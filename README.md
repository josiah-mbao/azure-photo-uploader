# Photo Backup to Azure Blob Storage

<img width="1440" height="900" alt="azure photo uploader UI" src="https://github.com/user-attachments/assets/ef0ccce1-69e3-4b06-8300-c7fa2bba311f" />


## Overview

This project provides a cost-effective solution for backing up photos from an iPhone to Azure Blob Storage using Python. It was motivated by the storage limitations of iCloud’s free plan, which only offers 5GB of storage. By utilizing Azure Blob Storage, this project allows users to securely store large amounts of data at a potentially lower cost, avoiding the ongoing expenses associated with paid cloud storage plans.

## Motivation

During a recent holiday in Zambia, I faced a challenge: my iPhone’s storage and iCloud storage were full, preventing me from taking more photos. On the iCloud free plan, my photos app was consuming around 25GB. Instead of opting for the cheapest paid plan ($1/month for 50GB), I decided to create this project to upload my photos to Azure Blob Storage, leveraging my knowledge gained from studying for the Azure Fundamentals (AZ-900) certification.

## Features

- Automated Photo Upload: The script automatically uploads photos from a specified local directory to an Azure Blob Storage container.
- Scalable Storage: Store large amounts of data without worrying about running out of space.
- Cost Efficiency: A cost-effective alternative to iCloud’s paid storage plans, with flexible pricing based on actual usage.
- Python-Powered: Implemented in Python, demonstrating proficiency in scripting and cloud service integration.

## Prerequisites

- Python 3.x: Ensure you have Python installed on your machine.
- zure Account: You’ll need an Azure account to create a storage account and blob container.
- Azure Storage Blob Python SDK: Install this package using pip:

```bash
pip install azure-storage-blob
```

## Setup

1.	Transfer Photos to Your Computer: Connect your iPhone to your computer and transfer the photos you want to back up.
2.	Azure Blob Storage Configuration:
	- Create a storage account and a blob container in Azure.
	- Obtain the connection string for your Azure Storage account.

3.	Clone the Repository:

```bash
git clone https://github.com/josiah-mbao/azure-photo-uploader.git
cd azure-photo-uploader
```

4.	Configure the Script: Open the backup_photos.py script and update the following variables:
- connection_string: Your Azure Storage connection string.
- container_name: The name of your Azure Blob container.
- local_directory: The path to the directory containing your photos.

5.	Run the Script: Execute the script to start uploading your photos to Azure Blob Storage:

```bash
python backup_photos.py
```

## Usage

This script is designed to be run manually whenever you want to back up your photos. It can be extended to include additional features such as automatic backups, logging, and error handling.

## Future Enhancements

- Automation: Schedule the script to run automatically at regular intervals using cron jobs or task schedulers.
- Error Handling: Improve error handling to deal with network interruptions and other potential issues.
- User Interface: Develop a simple GUI or CLI to enhance user experience.
- Compression: Add an option to compress photos before uploading to save on storage costs.


Cost Savings

By utilizing Azure Blob Storage, this project not only resolves the issue of limited local storage but also provides a cost-effective alternative to traditional cloud storage services. Currently, I pay only $0.27 per month to store 25GB of photos, significantly reducing costs compared to iCloud’s paid plans. This efficient pricing model allows users to manage their photo storage without breaking the bank. ![Screenshot of Azure Costs](screenshot.png)

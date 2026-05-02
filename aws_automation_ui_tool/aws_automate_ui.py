import boto3
import botocore
import tkinter as tk
from tkinter import scrolledtext, messagebox
import uuid
import os

# -------- GLOBAL --------
bucket_name = f"boto3-ui-demo-{uuid.uuid4()}"
sample_file = "sample.txt"

# -------- FUNCTIONS --------
def log_output(message):
    output.insert(tk.END, message + "\n")
    output.see(tk.END)

def list_ec2():
    region = region_entry.get()
    log_output(f"\nListing EC2 instances in {region}...")
    ec2 = boto3.client('ec2', region_name=region)

    try:
        response = ec2.describe_instances()
        for res in response['Reservations']:
            for inst in res['Instances']:
                log_output(f"{inst['InstanceId']} - {inst['State']['Name']}")
    except Exception as e:
        log_output(f"Error: {e}")

def create_bucket():
    region = region_entry.get()
    log_output(f"\nCreating bucket: {bucket_name}")
    s3 = boto3.client('s3', region_name=region)

    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        log_output("Bucket created successfully")
    except Exception as e:
        log_output(f"Error: {e}")

def upload_file():
    log_output("\nUploading sample file...")

    with open(sample_file, "w") as f:
        f.write("Hello from Tkinter AWS Tool!")

    s3 = boto3.client('s3')

    try:
        s3.upload_file(sample_file, bucket_name, sample_file)
        log_output("File uploaded successfully")
    except Exception as e:
        log_output(f"Error: {e}")

def list_users():
    log_output("\nListing IAM users...")
    iam = boto3.client('iam')

    try:
        users = iam.list_users()
        for user in users['Users']:
            log_output(f"{user['UserName']} - {user['CreateDate']}")
    except Exception as e:
        log_output(f"Error: {e}")

# -------- UI SETUP --------
root = tk.Tk()
root.title("AWS Automation Tool (Boto3)")
root.geometry("700x500")

# Region input
tk.Label(root, text="AWS Region:").pack()
region_entry = tk.Entry(root)
region_entry.insert(0, "us-east-1")
region_entry.pack()

# Buttons
tk.Button(root, text="List EC2 Instances", command=list_ec2).pack(pady=5)
tk.Button(root, text="Create S3 Bucket", command=create_bucket).pack(pady=5)
tk.Button(root, text="Upload Sample File", command=upload_file).pack(pady=5)
tk.Button(root, text="List IAM Users", command=list_users).pack(pady=5)

# Output console
output = scrolledtext.ScrolledText(root, width=80, height=20)
output.pack(pady=10)

root.mainloop()
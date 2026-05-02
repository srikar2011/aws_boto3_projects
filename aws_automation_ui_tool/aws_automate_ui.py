from flask import Flask, render_template, request
import boto3
import uuid
import os

app = Flask(__name__)

BUCKET_NAME = f"boto3-web-demo-{uuid.uuid4()}"
SAMPLE_FILE = "sample.txt"

def create_sample_file():
    with open(SAMPLE_FILE, "w") as f:
        f.write("Hello from Flask AWS Tool!")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ec2", methods=["POST"])
def list_ec2():
    region = request.form.get("region")
    ec2 = boto3.client("ec2", region_name=region)

    output = []
    try:
        response = ec2.describe_instances()
        for res in response["Reservations"]:
            for inst in res["Instances"]:
                output.append(f"{inst['InstanceId']} - {inst['State']['Name']}")
    except Exception as e:
        output.append(str(e))

    return render_template("index.html", result=output)

@app.route("/create-bucket", methods=["POST"])
def create_bucket():
    region = request.form.get("region")
    s3 = boto3.client("s3", region_name=region)

    output = []
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=BUCKET_NAME)
        else:
            s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        output.append(f"Bucket created: {BUCKET_NAME}")
    except Exception as e:
        output.append(str(e))

    return render_template("index.html", result=output)

@app.route("/upload", methods=["POST"])
def upload():
    create_sample_file()
    s3 = boto3.client("s3")

    output = []
    try:
        s3.upload_file(SAMPLE_FILE, BUCKET_NAME, SAMPLE_FILE)
        output.append("File uploaded successfully")
    except Exception as e:
        output.append(str(e))

    return render_template("index.html", result=output)

@app.route("/iam", methods=["POST"])
def list_iam():
    iam = boto3.client("iam")
    output = []

    try:
        users = iam.list_users()
        for user in users["Users"]:
            output.append(f"{user['UserName']} - {user['CreateDate']}")
    except Exception as e:
        output.append(str(e))

    return render_template("index.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)
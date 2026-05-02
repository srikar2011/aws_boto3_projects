from flask import Flask, render_template, request
import boto3
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ---------------- EC2 ----------------
@app.route("/ec2", methods=["POST"])
def ec2():
    region = request.form.get("region")
    ec2 = boto3.client("ec2", region_name=region)

    data = []
    try:
        res = ec2.describe_instances()
        for r in res["Reservations"]:
            for i in r["Instances"]:
                data.append({
                    "id": i["InstanceId"],
                    "state": i["State"]["Name"],
                    "type": i["InstanceType"]
                })
    except Exception as e:
        data.append({"error": str(e)})

    return render_template("index.html", ec2=data)

# ---------------- S3 ----------------
@app.route("/s3", methods=["POST"])
def s3():
    s3 = boto3.client("s3")
    buckets = []

    try:
        res = s3.list_buckets()
        for b in res["Buckets"]:
            buckets.append(b["Name"])
    except Exception as e:
        buckets.append(str(e))

    return render_template("index.html", buckets=buckets)

@app.route("/create-bucket", methods=["POST"])
def create_bucket():
    region = request.form.get("region")
    name = f"pro-ui-{uuid.uuid4()}"
    s3 = boto3.client("s3", region_name=region)

    msg = ""
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=name)
        else:
            s3.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        msg = f"Created: {name}"
    except Exception as e:
        msg = str(e)

    return render_template("index.html", message=msg)

# ---------------- IAM ----------------
@app.route("/iam", methods=["POST"])
def iam():
    iam = boto3.client("iam")
    users = []

    try:
        res = iam.list_users()
        for u in res["Users"]:
            users.append(u["UserName"])
    except Exception as e:
        users.append(str(e))

    return render_template("index.html", users=users)

# ---------------- PRICING ----------------
@app.route("/pricing", methods=["POST"])
def pricing():
    pricing = boto3.client("pricing", region_name="us-east-1")

    data = []
    try:
        res = pricing.get_products(
            ServiceCode="AmazonEC2",
            MaxResults=5
        )
        for p in res["PriceList"]:
            data.append(str(p)[:200])  # trimmed
    except Exception as e:
        data.append(str(e))

    return render_template("index.html", pricing=data)

if __name__ == "__main__":
    app.run(debug=True)
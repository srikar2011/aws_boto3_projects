from flask import Flask, render_template, request, jsonify
import boto3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# -------- EC2 API --------
@app.route("/api/ec2")
def api_ec2():
    region = request.args.get("region", "us-east-1")
    ec2 = boto3.client("ec2", region_name=region)

    instances = []
    try:
        res = ec2.describe_instances()
        for r in res["Reservations"]:
            for i in r["Instances"]:
                instances.append({
                    "id": i["InstanceId"],
                    "state": i["State"]["Name"],
                    "type": i["InstanceType"]
                })
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify(instances)

# -------- IAM API --------
@app.route("/api/iam")
def api_iam():
    iam = boto3.client("iam")
    users = []

    try:
        res = iam.list_users()
        for u in res["Users"]:
            users.append(u["UserName"])
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
import json
import base64

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Detect trigger type
    if "httpMethod" in event:
        return handle_api_gateway(event)

    elif "Records" in event:
        source = event["Records"][0].get("eventSource", "")

        if "s3" in source:
            return handle_s3(event)

        elif "sns" in source:
            return handle_sns(event)

        elif "sqs" in source:
            return handle_sqs(event)

        elif "dynamodb" in source:
            return handle_dynamodb(event)

    elif "source" in event and event["source"] == "aws.events":
        return handle_eventbridge(event)

    return {
        "statusCode": 200,
        "body": json.dumps("Unknown event type")
    }


# -------- API GATEWAY --------
def handle_api_gateway(event):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from API Gateway Lambda!",
            "input": event.get("queryStringParameters")
        })
    }


# -------- S3 TRIGGER --------
def handle_s3(event):
    records = []
    for r in event["Records"]:
        bucket = r["s3"]["bucket"]["name"]
        key = r["s3"]["object"]["key"]
        records.append(f"{bucket}/{key}")

    return {
        "statusCode": 200,
        "body": json.dumps({"uploaded_files": records})
    }


# -------- SNS TRIGGER --------
def handle_sns(event):
    messages = []
    for r in event["Records"]:
        messages.append(r["Sns"]["Message"])

    print("SNS Messages:", messages)
    return {"statusCode": 200}


# -------- SQS TRIGGER --------
def handle_sqs(event):
    messages = []
    for r in event["Records"]:
        messages.append(r["body"])

    print("SQS Messages:", messages)
    return {"statusCode": 200}


# -------- DYNAMODB STREAM --------
def handle_dynamodb(event):
    records = []
    for r in event["Records"]:
        event_name = r["eventName"]
        records.append(event_name)

    print("DynamoDB Events:", records)
    return {"statusCode": 200}


# -------- EVENTBRIDGE --------
def handle_eventbridge(event):
    print("Scheduled Event Triggered:", event["time"])
    return {"statusCode": 200}
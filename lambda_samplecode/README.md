🧪 How to Test Each Trigger
🌐 1. API Gateway
Create HTTP API → integrate Lambda
Call via browser:
https://your-api-id.execute-api.region.amazonaws.com/?name=srikar
🪣 2. S3 Trigger
Create S3 bucket
Add trigger → “PUT object”
Upload file → Lambda logs will show bucket/key
🔔 3. SNS
Create SNS topic
Subscribe Lambda
Publish message
📬 4. SQS
Create queue
Add Lambda trigger
Send message → Lambda processes batch
🗃️ 5. DynamoDB Streams
Enable stream on table
Insert/update item
Lambda logs event
⏰ 6. EventBridge (Scheduler)
Create rule → schedule (rate(5 minutes))
Target → Lambda
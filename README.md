AWS Automation UI Tool (Python + Boto3)
A simple desktop application built with Python (Tkinter) and Boto3 to perform common AWS tasks through a graphical interface — no need to use CLI commands repeatedly.
________________________________________
FEATURES
•	List all EC2 instances in a selected region 
•	Create a unique S3 bucket 
•	Upload a sample file to S3 
•	Display all IAM users in the AWS account 
•	Simple GUI with real-time output console 
________________________________________
TECH STACK
•	Python 3.x 
•	Boto3 (AWS SDK for Python) 
•	Tkinter (built-in Python GUI library) 
________________________________________
PROJECT STRUCTURE
aws-ui-tool/
main.py # Main application file
sample.txt # Generated dynamically for upload
README.md
________________________________________
PREREQUISITES
1.	Install Python (>= 3.7) 
2.	Configure AWS CLI 
Run the following command and enter your credentials:
aws configure
You will need:
•	AWS Access Key 
•	AWS Secret Key 
•	Default Region 
•	Output format (json) 
3.	Install required package 
pip install boto3
________________________________________
HOW TO RUN
python main.py
________________________________________
HOW IT WORKS
1.	Enter AWS Region (default: us-east-1) 
2.	Click buttons to perform actions: 
•	List EC2 Instances
→ Fetches instance IDs and their current state 
•	Create S3 Bucket
→ Creates a globally unique S3 bucket 
•	Upload Sample File
→ Uploads a generated text file into the bucket 
•	List IAM Users
→ Displays IAM users and creation dates 
3.	Output will be displayed inside the application console 
________________________________________
REQUIRED IAM PERMISSIONS
Make sure your AWS IAM user or role has:
•	ec2:DescribeInstances 
•	s3:CreateBucket 
•	s3:PutObject 
•	iam:ListUsers 
________________________________________
NOTES
•	S3 bucket names must be globally unique (handled using UUID) 
•	IAM is a global service, so region selection does not apply 
•	Sample file is created temporarily during upload 
________________________________________
EXAMPLE OUTPUT
Listing EC2 instances in us-east-1...
i-1234567890abcdef0 - running
Creating bucket: boto3-ui-demo-xxxx
Bucket created successfully
Uploading sample file...
File uploaded successfully
Listing IAM users...
admin - 2023-05-10
developer - 2024-01-15
________________________________________
FUTURE ENHANCEMENTS
•	Region dropdown selector 
•	Table view for EC2 instances 
•	Delete S3 buckets and objects 
•	EC2 start/stop/terminate options 
•	Multi-account support 
•	Dark mode UI 
•	Improved logging and error handling 
________________________________________
CONTRIBUTING
Contributions are welcome. Feel free to fork the repository and submit a pull request.
________________________________________
LICENSE
This project is licensed under the MIT License.
________________________________________
ACKNOWLEDGEMENTS
•	AWS Boto3 Documentation 
•	Python Tkinter Library

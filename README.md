# AWS Lambda and CloudWatch Event Automation
This Python script automates the process of creating an AWS Lambda function that serves the main() function from work.py and setting up a CloudWatch Event trigger to execute the Lambda function on a schedule.

## Prerequisites
Before you can use this script, you'll need to:

Have an AWS account with the necessary permissions to create Lambda functions and CloudWatch Event rules.

Install the AWS SDK for Python (Boto3) using pip install boto3.

Set up your AWS credentials and region in your environment variables:

```bash
export AWS_ACCESS_KEY_ID=<your_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
export AWS_REGION=<your_region>
```
## Usage
Clone or download the work.py file and the create_lambda_function.py script to your local machine.

Open the create_lambda_function.py script in a text editor and replace the following placeholders with your own values:

<your_access_key_id>: Your AWS access key ID.
<your_secret_access_key>: Your AWS secret access key.
<your_region>: The AWS region where you want to create the Lambda function and CloudWatch Event rule.
<your_iam_role_arn>: The ARN of the IAM role that your Lambda function will assume when it runs.
Save the changes to the create_lambda_function.py script.

Run the create_lambda_function.py script using python create_lambda_function.py in your terminal.

Wait for the script to complete. It will create a new Lambda function that serves the main() function from work.py and set up a CloudWatch Event rule to execute the Lambda function on a schedule.

## Customization
If you want to customize the schedule for the CloudWatch Event rule, you can modify the schedule_expression parameter in the create_cloudwatch_event_rule() function in the create_lambda_function.py script. For example, to trigger the CloudWatch Event rule every 10 minutes, you can change the schedule_expression parameter to 'rate(10 minutes)'.

# API Request Anomaly Detector
This is a Python script that pings OpenAI API endpoint every 6 minutes, retrieves the latest analytics data, stores it in a database, and detects any anomalies in the timeseries data. If an anomaly is detected, it sends an email to a registered email address.

## Getting Started
To use this script, you will need the following:
1. A database to store the timeseries data. You can use any database of your choice like MySQL, PostgreSQL, SQLite, etc.
2. A registered email address to receive alerts.

## Setup

1. Dev Setup 
```bash
git clone https://github.com/your-username/api-request-anomaly-detector.git
python -m venv venv
source venv/bin/activate
pip install requests pandas sqlite3 smtplib
```
2. Edit the config.py file to set the following variables:
3. Deploy to AWS Lambda
```python
python deploy_to_aws_lambda.py
```

**THAT'S IT!**

The script will start pinging the API endpoint every 6 minutes and storing the data in the database. If an anomaly is detected, it will send an email to the registered email address.

## Contributing
If you find a bug or want to contribute to this project, please create a pull request or submit an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
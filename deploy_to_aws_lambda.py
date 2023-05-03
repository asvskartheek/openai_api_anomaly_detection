import boto3
import os
import zipfile
import io
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, IAM_ROLE_ARN, FUNCTION_NAME, HANDLER_FUNCTION_NAME, SCHEDULE_EXPRESSION


def create_lambda_package():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        zip_file.write('working_code.py')
    buffer.seek(0)
    return buffer.read()


def create_lambda_function():
    lambda_client = boto3.client('lambda')

    # Define the parameters for the new Lambda function
    role_arn = IAM_ROLE_ARN
    runtime = 'python3.8'
    handler = HANDLER_FUNCTION_NAME
    code = create_lambda_package()

    lambda_response = lambda_client.create_function(
        FunctionName=FUNCTION_NAME,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={'ZipFile': code},
    )

    return lambda_response['FunctionArn']


def create_cloudwatch_event_rule(lambda_function_arn):
    events_client = boto3.client('events')
    rule_name = 'my-cloudwatch-event-rule'
    schedule_expression = SCHEDULE_EXPRESSION
    events_client.put_rule(
        Name=rule_name,
        ScheduleExpression=schedule_expression,
    )
    target = {
        'Id': 'my-lambda-function-target',
        'Arn': lambda_function_arn,
    }

    events_client.put_targets(
        Rule=rule_name,
        Targets=[target],
    )


if __name__ == '__main__':
    os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
    os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
    os.environ['AWS_REGION'] = AWS_REGION

    lambda_function_arn = create_lambda_function()
    create_cloudwatch_event_rule(lambda_function_arn)
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ssm')
    
    variable = event['queryStringParameters']['device']
    print(variable)
    
    response = client.send_command(
    InstanceIds=[
        'mi-00d28f33b82b67f9f',
    ],
    DocumentName='AWS-RunShellScript',
    TimeoutSeconds=30,
    Parameters={
        'commands': [
            'python3 OuvrePortail.py ' + variable,
        ],
        'workingDirectory': [
            '/home/penta/IoT/MonetPortail',
        ],
        'executionTimeout': [
            '10',
        ],
    },
    ServiceRoleArn='arn:aws:iam::631131992221:role/service-role/AmazonEC2RunCommandRoleForManagedInstances',
)
    return {
        'statusCode': 200,
        'body': json.dumps("GG BG !")
    }

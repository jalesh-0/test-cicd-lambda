import json

def lambda_handler(event, context):
    # TODO implement
    print("Hello")
    print("Hello")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! , Now')
    }
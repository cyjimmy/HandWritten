import json
import boto3

lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            }
        }
    api_key = event['headers'].get("authorization", None)
    if api_key != 'vZJWqT2qaYaNOLACfsbju9MrSpnCHeTE9dxbMSqo':
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": "Unauthorized request."})
        }
    try:
        body = json.loads(event['body'])
        url = body['url']
        auth_payload = {'url': url}
        answer = lambda_client.invoke(
            FunctionName="handwritten",
            InvocationType="RequestResponse",
            Payload=json.dumps(auth_payload)
        )
        answer_payload = answer['Payload'].read().decode('utf-8')
        answer_json = json.loads(answer_payload)
        response = {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({'message': answer_json})
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
    return response

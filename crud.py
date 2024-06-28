import json
import boto3

dynamodb = boto3.resource('dynamodb')
#make sure you provided correct table name
table = dynamodb.Table('api-crud-db')

def lambda_handler(event, context):
    status_code = 200
    headers = {
        "Content-Type": "application/json"
    }
    body = None

    try:
        print("Received event:", json.dumps(event, indent=2))

        if event['routeKey'] == "DELETE /items/{id}":
            if 'pathParameters' in event and 'id' in event['pathParameters']:
                table.delete_item(
                    Key={
                        'id': event['pathParameters']['id']
                    }
                )
                body = f"Deleted item {event['pathParameters']['id']}"
            else:
                raise ValueError("Missing required path parameter 'id'")
        
        elif event['routeKey'] == "GET /items/{id}":
            if 'pathParameters' in event and 'id' in event['pathParameters']:
                response = table.get_item(
                    Key={
                        'id': event['pathParameters']['id']
                    }
                )
                body = response.get('Item', {})
            else:
                raise ValueError("Missing required path parameter 'id'")
        
        elif event['routeKey'] == "GET /items":
            response = table.scan()
            body = response.get('Items', [])
        
        elif event['routeKey'] == "PUT /items":
            if 'body' in event:
                try:
                    request_json = json.loads(event['body'])
                    if all(key in request_json for key in ('id', 'price', 'name')):
                        table.put_item(
                            Item={
                                'id': request_json['id'],
                                'price': request_json['price'],
                                'name': request_json['name']
                            }
                        )
                        body = f"Put item {request_json['id']}"
                    else:
                        raise ValueError("Missing one of the required keys: 'id', 'price', 'name'")
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON format in request body")
            else:
                raise ValueError("Missing request body")
        
        else:
            raise ValueError(f"Unsupported route: {event['routeKey']}")
    
    except Exception as e:
        print("Error processing request:", str(e))
        status_code = 400
        body = str(e)
    
    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': headers
    }

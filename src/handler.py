
import json
import os
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


s3 = boto3.client(
    's3',
    endpoint_url=os.getenv('LOCALSTACK_URL', 'http://localhost:4566'),
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)
BUCKET = os.getenv('NOTES_BUCKET', 'notes-bucket')

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def main(event, context):
    method = event.get('httpMethod')
    path = event.get('path', '')
    body = event.get('body')
    key = event.get('queryStringParameters', {}).get('id')

    logger.debug("EVENT RECEIVED: %s", event)
    route = event.get("routeKey") or f"{event.get('httpMethod')} {event.get('path', '')}"
    logger.debug("routeKey resolved to: %s", route)

    try:
        if method == 'POST' and path == '/notes':
            return create_note(json.loads(body))
        if method == 'GET' and path == '/notes':
            return list_notes()
        if method == 'GET' and path == '/notes/{id}' and key:
            return get_note(key)
        if method == 'PUT' and path == '/notes/{id}' and key:
            return update_note(key, json.loads(body))
        if method == 'DELETE' and path == '/notes/{id}' and key:
            return delete_note(key)
        return response(400, {"error": "Unsupported route or missing id"})
    except ClientError as e:
        return response(500, {"error": str(e)})

def create_note(data):
    note_id = data.get('id')
    if not note_id:
        return response(400, {"error": "Missing 'id' in body"})
    s3.put_object(Bucket=BUCKET, Key=note_id, Body=json.dumps(data))
    return response(201, {"message": "Note created", "id": note_id})

def get_note(note_id):
    obj = s3.get_object(Bucket=BUCKET, Key=note_id)
    content = obj['Body'].read().decode()
    return response(200, json.loads(content))

def list_notes():
    objs = s3.list_objects_v2(Bucket=BUCKET).get('Contents', [])
    ids = [o['Key'] for o in objs]
    return response(200, {"notes": ids})

def update_note(note_id, data):
    s3.put_object(Bucket=BUCKET, Key=note_id, Body=json.dumps(data))
    return response(200, {"message": "Note updated", "id": note_id})

def delete_note(note_id):
    s3.delete_object(Bucket=BUCKET, Key=note_id)
    return response(204, {})




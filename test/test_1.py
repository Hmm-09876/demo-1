from src import handler
import json, boto3


def test_create_note():
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name='us-east-1',
        config=boto3.session.Config(s3={'addressing_style': 'path'})
    )


    s3.create_bucket(Bucket='notes-bucket')


    event = {"httpMethod": "POST", "path": "/notes", 
            "body": json.dumps({"text": "Test note", "id": "note1"})}
    res = handler.main(event, None)


    print("DEBUG RESPONSE:", json.dumps(res, indent=2))


    assert res['statusCode'] == 201
    body = json.loads(res['body'])
    assert body['message'] == "Note created"
    assert body['id'] == "note1"



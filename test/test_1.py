from src import handler
import json

def test_create_note():
    event = {"httpMethod": "POST", "path": "/notes", 
            "body": json.dumps({"text": "Test note", "id": "note1"})}
    res = handler.main(event, None)
    print("DEBUG RESPONSE:", json.dumps(res, indent=2))
    assert res['statusCode'] == 200



from src import handler

def test_create_note():
    event = {"httpMethod": "POST", "body": '{\"text\": \"Test note\"}'}
    res = handler.main(event, None)
    assert res['statusCode'] == 200







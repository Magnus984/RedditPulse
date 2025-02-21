from tests import client

def test_get_integration_json():
    response = client.get("/integration.json")
    assert response.status_code == 200
    assert "data" in response.json()



def test_tick_endpoint():
    payload = {
        "channel_id": "0195051c-9c31-763b-b4f3-313dcaf0254f",
        "return_url": "https://ping.telex.im/v1/webhooks/0195051c-9c31-763b-b4f3-313dcaf0254f",
        "settings": [
            {
                "label": "Keywords",
                "type": "multi-select",
                "description": "Select keywords to be notified of",
                "required": True,
                "default": ["AI", "Machine Learning", "Deep Learning"]
            }
            ]
        }
    response = client.post("/tick", json=payload)
    assert response.status_code == 202


def test_invalid_endpoint():
    response = client.get("/nonexistent-endpoint")
    assert response.status_code == 404    
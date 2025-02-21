from fastapi import APIRouter, status, HTTPException, requests
from pydantic import BaseModel
from core.auth import reddit
import requests

router = APIRouter()


class Payload(BaseModel):
    channel_id: str
    return_url: str
    settings: list


@router.post("/tick", status_code=202)
def get_posts(payload: Payload):
    data = {
        "message": "There are hot topics now",
        "username": " Reddit Pulse Monitor",
        "event_name": "Trending Topics",
    }
    try:
        keywords = [keyword for k in payload.settings if k["label"] == "Keywords" for keyword in k["default"]]
        for post in reddit.subreddit("all").hot(limit=10):
            for keyword in keywords:
                if keyword.lower() in post.title.lower():
                    data.update(status="success")
                    response = requests.post(payload.return_url, json=data)
                    if (response.status_code == 202):
                        return {"status": "accepted"}
    
        data.update(message = "Wait for an hour", status="error")
        r = requests.post(payload.return_url, json=data)
        return {"status": "error"}
    except requests.exceptions.RequestException as e:
        return {
            "status": "error", "message": f"Request error: {e}"
            }
    except Exception as e:
        return {
            "status": "error", "message": f"Unexpected error: {e}"
            }

    
from fastapi import APIRouter
from fastapi import Request
from datetime import datetime

router = APIRouter()
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")

@router.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-18",
                "updated_at": formatted_date
                },
            "descriptions": {
                "app_description": "Fetches popular reddit posts hourly and sends a notification when specific topics that have been selected trend",
                "app_logo": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/af/14/6d/af146d83-130b-1a65-0255-ecd5c5e0e822/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/230x0w.webp",
                "app_name": "Reddit Pulse",
                "app_url": base_url,
                "background_color": "#fff"
                },
            "integration_category": "Monitoring & Logging",
            "integration_type": "interval",
            "is_active": False,
            "key_features": [
                "Sends a notification when specific topics trend on Reddit.",
                "Fetches popular Reddit posts hourly.",
                "Select keywords to be notified of.",
            ],
            "permissions": {
                "monitoring_user": {
                "always_online": True,
                "display_name": "Reddit Pulse"
                }
            },
            "settings": [
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "0 * * * *"
                },
                {
                    "label": "Keywords",
                    "type": "multi-select",
                    "description": "Select keywords to be notified of",
                    "required": True,
                    "options": ["AI", "Machine Learning", "Deep Learning"]
                }
            ],
            "tick_url": f"{base_url}/tick",
            "target_url": ""
        }
    }

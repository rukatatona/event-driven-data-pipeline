from datetime import datetime

def process_event(event):
    return {
        "user_id": event.get("user_id"),
        "event_type": event.get("event_type"),
        "event_date": event.get("timestamp")[:10],
        "processed_at": datetime.utcnow().isoformat()
    }

events = [
    {"user_id": 1, "event_type": "click", "timestamp": "2026-04-07T10:00:00"},
    {"user_id": 2, "event_type": "view", "timestamp": "2026-04-07T10:01:00"}
]

processed = [process_event(e) for e in events]

print(processed)

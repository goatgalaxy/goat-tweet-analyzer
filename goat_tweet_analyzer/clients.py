import json
import requests

from config impoter settings

class InternalTwitterApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def save_tweet_sentiment(self, pk, body, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = f"{base_url}/tweet/{pk}"
        data = json.dumps(body)
        requests.put(url, data=data, headers=headers)

internal_api_client = InternalTwitterApiClient(settings.API_URL)

import json
import requests

from goat_tweet_analyzer.config import settings

class InternalTwitterApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def save_tweet_sentiment(self, pk, body, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = f"{self.base_url}/tweet/{pk}"
        data = json.dumps(body)
        return requests.put(url, data=data, headers=headers)

internal_api_client = InternalTwitterApiClient(settings.API_URL)


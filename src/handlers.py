import logging

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger(__name__)


class ProcessTweetsHandler:
    def generate_payload(self, tweet):
        return {}
    
    def save_tweet(self, id, payload):
        pass
    
    def handle(self, message, *args, **kwargs):
        for tweet in message["tweets"]:
             payload = self.generate_payload(tweet)
             self.save_tweet(tweet["id"], payload)
        logger.info(f"Message: {message} processed sucessufully")
        return True

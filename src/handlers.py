import logging

logger = logging.getLogger(__name__)


class ProcessTweetsHandler:
    def generate_payload(self, tweet):
        return {}
    
    def save_tweet(self, tweet_id, payload):
        pass
    
    def handle(self, message, **kwargs):
        for tweet in message:
            payload = self.generate_payload(tweet)
            self.save_tweet(payload)
        logger.info(f"Message: {message} processed sucessufully")
        return True

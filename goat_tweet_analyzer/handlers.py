import logging

from goat_tweet_analyzer.analyzer import analyzer
from goat_tweet_analyzer.clients import internal_api_client

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger(__name__)


class ProcessTweetsHandler:
    def get_sentiment_value(self, message):
        result = analyzer.polarity_scores(message)
        return result["compound"]

    def generate_payload(self, sentiment):
        return {
            "sentiment": sentiment
        }

    def save_tweet(self, pk, body):
        internal_api_client.save_tweet_sentiment(pk, body)

    def handle(self, tweet, *args, **kwargs):
        sentiment = self.get_sentiment_value(tweet["message"])
        payload = self.generate_payload(sentiment)
        self.save_tweet(tweet["id"], payload)
        logger.info(f"Message: {tweet} processed successfully")
        return True

from loafer.ext.aws.routes import SNSQueueRoute

from goat_tweet_analyzer.handlers import ProcessTweetsHandler

from goat_tweet_analyzer.config import settings

from goat_tweet_analyzer.translators import GoatMessagesTranslator

provider_options = {
    "endpoint_url": settings.AWS_ENDPOINT_URL,
    "options": {"MaxNumberOfMessages": 10, "WaitTimeSeconds": int(settings.WAIT_TIME_SECONDS)},
}


routes = (
    SNSQueueRoute(
        provider_queue=settings.TWEET_QUEUE,
        provider_options=provider_options,
        handler=ProcessTweetsHandler(),
        message_translator=GoatMessagesTranslator(),
    ),
)
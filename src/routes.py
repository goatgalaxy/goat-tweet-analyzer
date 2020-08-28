from loafer.ext.aws.routes import SNSQueueRoute

from src.handlers import ProcessTweetsHandler

from src.config import settings

provider_options = {
    "endpoint_url": settings.AWS_ENDPOINT_URL,
    "options": {"MaxNumberOfMessages": 10, "WaitTimeSeconds": settings.WAIT_TIME_SECONDS},
}


routes = (
    SNSQueueRoute(
        provider_queue=settings.TWEET_QUEUE,
        provider_options=provider_options,
        handler=ProcessTweetsHandler(),
    ),
)
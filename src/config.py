from prettyconf import config

class Settings:
    API_URL = config("API_URL")
    TWEET_QUEUE = config("TWEET_QUEUE")
    WAIT_TIME_SECONDS = config("WAIT_TIME_SECONDS")

    AWS_DEFAULT_REGION = config("AWS_DEFAULT_REGION")
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL")

settings = Settings()

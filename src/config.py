from prettyconf import config

class Settings:
    self.API_URL = config.get("API_URL")
    self.TWEET_QUEUE = config.get("TWEET_QUEUE")
    self.WAIT_TIME_SECONDS = config.get("WAIT_TIME_SECONDS")

settings = Settings()

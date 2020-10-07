from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def getAnalyzer():
    if not analyzer:
        analyzer = SentimentIntensityAnalyzer()
    return analyzer

from twitter.client.client import IClient
from twitter.domain.tweet import Tweet


class TweetRepo:

    _client: IClient

    def __init__(self, client: IClient):
        self._client = client

    def get_tweets_by_hashtag(self, hashtag: str, limit: int = 30) -> [Tweet]:
        return self._client.search_tweets("#" + hashtag, limit)

    def get_tweets_by_username(self, username: str, limit: int = 30) -> [Tweet]:
        return self._client.search_tweets("from:" + username, limit)

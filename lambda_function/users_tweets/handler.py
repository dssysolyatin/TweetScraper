import json
from twitter.json.encoder import Encoder
from twitter.client.factory import Factory
from twitter.repository.tweetrepo import TweetRepo


class Handler:
    def __init__(self, repo: TweetRepo):
        self._repo = repo

    def handle(self, event: dict):
        tweets = self._repo.get_tweets_by_username(
            event['pathParameters']['username'],
            int(event['queryStringParameters']['limit'])
        )

        return {
            "statusCode": 200,
            "body": json.dumps(tweets, cls=Encoder),
        }


handler = Handler(TweetRepo(Factory().create()))


def handle(event: dict, _):
    return handler.handle(event)

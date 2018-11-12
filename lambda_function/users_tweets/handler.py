import json
from twitter.json.encoder import Encoder
from twitter.client.factory import Factory
from twitter.repository.tweetrepo import TweetRepo
from lambda_helper.api_gateway import ApiGateway


class Handler:
    def __init__(self, repo: TweetRepo, api_gateway_helper: ApiGateway):
        self._api_gateway_helper = api_gateway_helper
        self._repo = repo

    def handle(self, event: dict):
        tweets = self._repo.get_tweets_by_username(
            event['pathParameters']['username'],
            int(self._api_gateway_helper.query_parameter_from_event(event, 'limit', 30))
        )

        return {
            "statusCode": 200,
            "body": json.dumps(tweets, cls=Encoder),
        }


handler = Handler(TweetRepo(Factory().create()), ApiGateway())


def handle(event: dict, _):
    return handler.handle(event)

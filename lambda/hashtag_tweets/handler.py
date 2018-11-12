import json
from twitter.json.encoder import Encoder
from twitter.client.factory import Factory
from twitter.repository.tweetrepo import TweetRepo


def handle(event: dict, _):

    client_factory = Factory()
    client = client_factory.create()
    repo = TweetRepo(client)

    tweets = repo.get_tweets_by_hashtag(event['pathParameters']['hashtag'])

    return {
        "statusCode": 200,
        "body": json.dumps(tweets, cls=Encoder),
    }

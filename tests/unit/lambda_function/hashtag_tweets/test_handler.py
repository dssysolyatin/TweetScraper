import unittest
from lambda_function.hashtag_tweets.handler import Handler
from lambda_helper.api_gateway import ApiGateway
from unittest.mock import patch


class HandlerTestCase(unittest.TestCase):

    @patch("twitter.repository.tweetrepo.TweetRepo")
    def test_handle(self, mock_tweet_repo):
        mock_tweet_repo.get_tweets_by_hashtag.return_value = []
        handler = Handler(mock_tweet_repo, ApiGateway())

        handler.handle({
            "queryStringParameters": {
                "limit": 20
            },
            "pathParameters": {
                "hashtag": "AMD"
            }
        })

        mock_tweet_repo.get_tweets_by_hashtag.assert_called_once_with('AMD', 20)


import unittest
from lambda_function.users_tweets.handler import Handler
from unittest.mock import patch


class HandlerTestCase(unittest.TestCase):

    @patch("twitter.repository.tweetrepo.TweetRepo")
    def test_handle(self, mock_tweet_repo):
        mock_tweet_repo.get_tweets_by_username.return_value = []
        handler = Handler(mock_tweet_repo)

        handler.handle({
            "queryStringParameters": {
                "limit": 10
            },
            "pathParameters": {
                "username": "vk"
            }
        })

        mock_tweet_repo.get_tweets_by_username.assert_called_once_with('vk', 10)


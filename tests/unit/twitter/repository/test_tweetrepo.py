import unittest
from unittest.mock import patch
from twitter.repository.tweetrepo import TweetRepo


class TweetRepoTestCase(unittest.TestCase):

    @patch("twitter.client.client.IClient")
    def test_get_tweets_by_hashtag(self, client):
        tweetrepo = TweetRepo(client)

        tweetrepo.get_tweets_by_username('vk', 10)
        client.search_tweets.assert_called_with('from:vk', 10)

        tweetrepo.get_tweets_by_username('amazon')
        client.search_tweets.assert_called_with('from:amazon', 30)

    @patch("twitter.client.client.IClient")
    def test_get_tweets_by_username(self, client):
        tweetrepo = TweetRepo(client)

        tweetrepo.get_tweets_by_hashtag('vk', 10)
        client.search_tweets.assert_called_with('#vk', 10)

        tweetrepo.get_tweets_by_hashtag('amazon')
        client.search_tweets.assert_called_with('#amazon', 30)

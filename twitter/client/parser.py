import abc
from bs4 import BeautifulSoup
from twitter.domain.tweet import Tweet
from twitter.domain.account import Account


class IParser(abc.ABC):

    @abc.abstractmethod
    def parse(self, content: str) -> [Tweet]:
        """ Extract tweets from html content
        """
        pass


class Parser(IParser):

    def parse(self, content: str) -> [Tweet]:
        bs = BeautifulSoup(content, 'html.parser')
        bs_tweets = bs.find_all("li", attrs={"data-item-type": "tweet"})

        return [self._parse_tweet(bs_tweet) for bs_tweet in bs_tweets]

    def _parse_tweet(self, bs_tweet: BeautifulSoup) -> Tweet:
        tweet = Tweet()

        tweet.likes = self._parse_tweet_action_count(bs_tweet, "favorite")
        tweet.replies = self._parse_tweet_action_count(bs_tweet, "reply")
        tweet.retweets = self._parse_tweet_action_count(bs_tweet, "retweet")
        tweet.text = bs_tweet.find("div", {"class": "js-tweet-text-container"}).text.strip()
        tweet.hashtags = self._parse_hashtags(bs_tweet)
        tweet.date = bs_tweet.find("a", {"class": "tweet-timestamp"}).get('title')

        tweet.account = self._parse_tweet_account(bs_tweet)

        return tweet

    def _parse_hashtags(self, bs_tweet: BeautifulSoup) -> list:
        hashtags = bs_tweet.select("div.js-tweet-text-container a.twitter-hashtag")
        return [hashtag.text for hashtag in hashtags]

    def _parse_tweet_account(self, bs_tweet: BeautifulSoup) -> Account:
        bs_account = bs_tweet.find("a", attrs={"class": "js-account-group"})

        account = Account()
        account.id = int(bs_account.get("data-user-id"))
        account.href = bs_account.get("href")
        account.fullname = bs_account.find("strong", attrs={"class": "fullname"}).text

        return account

    def _parse_tweet_action_count(self, bs_tweet: BeautifulSoup, action_name: str) -> int:
        selector = f"span.ProfileTweet-action--{action_name} > span.ProfileTweet-actionCount"

        return int(bs_tweet.select(selector, limit=1)[0].get('data-tweet-stat-count'))

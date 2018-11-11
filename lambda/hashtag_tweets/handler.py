from twitter.client.factory import Factory
from twitter.repository.tweetrepo import TweetRepo

client_factory = Factory()
client = client_factory.create()
repo = TweetRepo(client)

tweets = repo.get_tweets_by_username("amazonsdadfwqefq2f")

for tweet in tweets:
    print(tweet.account.fullname)


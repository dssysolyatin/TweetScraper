from twitter.domain.account import Account

class Tweet:
    account: Account
    date: str
    hashtags: [str]
    likes: int
    replies: int
    retweets: int
    text: str

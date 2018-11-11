from twitter.domain.account import Account
from twitter.json.encoder import ISerializable


class Tweet(ISerializable):
    account: Account
    date: str
    hashtags: [str]
    likes: int
    replies: int
    retweets: int
    text: str

    def serialize(self) -> dict:
        return self.__dict__

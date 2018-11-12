import abc
from twitter.domain.tweet import Tweet
from twitter.client.search_pages_iterator import SearchPagesIterator
from twitter.client.transport_client import ITransportClient
from twitter.client.parser import IParser


class IClient(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def search_tweets(self, query: str, limit: int = 30) -> [Tweet]:
        pass


class Client(IClient):

    _transport: ITransportClient
    _parser: IParser

    def __init__(self, transport_client: ITransportClient, parser: IParser):
        self._transport = transport_client
        self._parser = parser

    def search_tweets(self, query: str, limit: int = 30) -> [Tweet]:
        search_pages_iterator = SearchPagesIterator(self._transport, query)

        tweets = []
        for search_page in search_pages_iterator:
            tweets.extend(self._parser.parse(search_page))

            if len(tweets) >= limit:
                break

        return tweets[:limit] if len(tweets) > limit else tweets



from twitter.client.transport_client import HttpTransportClient
from twitter.client.client import Client
from twitter.client.parser import Parser


class Factory:
    def create(self) -> Client:
        transport_client = HttpTransportClient()
        parser = Parser()

        return Client(transport_client, parser)


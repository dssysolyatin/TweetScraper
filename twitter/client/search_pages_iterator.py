import re
from collections.abc import Iterator
from twitter.client.transport_client import ITransportClient


class SearchPagesIterator(Iterator):

    _search_url: str
    _query: str
    _client: ITransportClient
    _has_more_items: bool
    _min_position: str

    def __init__(self, client: ITransportClient, query: str, search_url: str = '/i/search/timeline'):
        self._search_url = search_url
        self._query = query
        self._client = client
        self._has_more_items = True
        self._min_position = ''

    def __iter__(self):
        return self

    def __next__(self):

        if self._has_more_items is False:
            raise StopIteration()

        if not self._min_position:
            return self._first_search()

        r = self._client.get_page('/i/search/timeline', params={
            "q": self._query,
            "vertical": "default",
            "include_entities": 1,
            "include_available_features": 1,
            "reset_error_state": "false",
            "max_position": self._min_position
        })

        json = r.json()

        if not json["has_more_items"] and self._min_position == json["min_position"]:
            self._has_more_items = False

        return json["items_html"]

    def _first_search(self):
        r = self._client.get_page('/search', params={
            "q": self._query
        })

        m = re.search(r'data-min-position="([^"]*)"', r.text)

        if m is None:
            self._has_more_items = False
        else:
            self._min_position = m.group(1)

        return r.text

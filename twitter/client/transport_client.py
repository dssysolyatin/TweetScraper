import abc
import requests


class ITransportClient(abc.ABC):

    @abc.abstractmethod
    def get_page(self, url, params: dict = None) -> requests.Response:
        """ Gets a twitter page in html format
        """
        pass


class HttpTransportClient(ITransportClient):

    _base_url: str
    _timeout: int

    def __init__(self, timeout: float = 3.0, base_url: str = 'https://twitter.com'):
        self._base_url = base_url
        self._timeout = timeout

    def get_page(self, url: str, params: dict = None, headers: dict = None) -> requests.Response:
        headers = headers or {}

        return requests.get(
            self._base_url + url,
            params=params,
            timeout=self._timeout,
            headers={
                "accept-language": "en-US,en;q=0.9",
                # Google bot user-agent :)
                "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                **headers
            }
        )

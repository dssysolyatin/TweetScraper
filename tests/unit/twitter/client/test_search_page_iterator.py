import unittest
from unittest.mock import patch
from twitter.client.search_pages_iterator import SearchPagesIterator


class SearchPageIteratorTestCase(unittest.TestCase):

    @patch("requests.Response")
    @patch("twitter.client.transport_client.ITransportClient")
    def test_next(self, mock_transport_client, mock_response):
        mock_data_min_pos = 'cm+55m'
        mock_html = f"<div class=\"stream-container\" data-min-position=\"{mock_data_min_pos}\">test</div>"
        mock_json = {
            "min_position": "cm+55m-1",
            "has_more_items": False,
            "items_html": {}
        }

        mock_response.text = mock_html
        mock_transport_client.get_page.return_value = mock_response

        search_page_iterator = SearchPagesIterator(mock_transport_client, "#Amazon")
        search_page_iterator.__next__()

        args, kwargs = mock_transport_client.get_page.call_args

        self.assertEqual(args[0], '/search')
        self.assertEqual({'q': '#Amazon'}, kwargs["params"])
        self.assertEqual(mock_data_min_pos, search_page_iterator._min_position)
        self.assertEqual(True, search_page_iterator._has_more_items)

        mock_response.json.return_value = mock_json
        search_page_iterator.__next__()

        args, kwargs = mock_transport_client.get_page.call_args

        self.assertEqual(args[0], '/i/search/timeline')
        self.assertEqual('#Amazon', kwargs["params"]["q"])
        self.assertEqual(mock_json["min_position"], search_page_iterator._min_position)








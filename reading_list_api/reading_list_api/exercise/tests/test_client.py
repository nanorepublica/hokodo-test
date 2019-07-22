
from django.test import TestCase
import requests_mock

from ..client import book_client


class ClientTest(TestCase):

    @requests_mock.Mocker()
    def test_get(self, m):
        m.register_uri('GET', 'https://hokodo-frontend-interview.netlify.com/data.json', json={
            'books': [{}, {}]
        })
        data = book_client.get()
        self.assertEqual(data, {
            'books': [{}, {}]
        })

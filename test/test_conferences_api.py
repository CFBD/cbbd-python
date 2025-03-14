# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cbbd.api.conferences_api import ConferencesApi  # noqa: E501


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConferencesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_conference_history(self) -> None:
        """Test case for get_conference_history

        """
        pass

    def test_get_conferences(self) -> None:
        """Test case for get_conferences

        """
        pass


if __name__ == '__main__':
    unittest.main()

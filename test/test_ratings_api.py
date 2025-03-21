# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.20.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cbbd.api.ratings_api import RatingsApi  # noqa: E501


class TestRatingsApi(unittest.TestCase):
    """RatingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RatingsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_adjusted_efficiency(self) -> None:
        """Test case for get_adjusted_efficiency

        """
        pass

    def test_get_srs(self) -> None:
        """Test case for get_srs

        """
        pass


if __name__ == '__main__':
    unittest.main()

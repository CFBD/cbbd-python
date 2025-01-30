# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.4.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cbbd.api.lines_api import LinesApi  # noqa: E501


class TestLinesApi(unittest.TestCase):
    """LinesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LinesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_lines(self) -> None:
        """Test case for get_lines

        """
        pass

    def test_get_providers(self) -> None:
        """Test case for get_providers

        """
        pass


if __name__ == '__main__':
    unittest.main()

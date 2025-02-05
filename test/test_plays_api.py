# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.6.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cbbd.api.plays_api import PlaysApi  # noqa: E501


class TestPlaysApi(unittest.TestCase):
    """PlaysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaysApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_play_types(self) -> None:
        """Test case for get_play_types

        """
        pass

    def test_get_plays(self) -> None:
        """Test case for get_plays

        """
        pass

    def test_get_plays_by_date(self) -> None:
        """Test case for get_plays_by_date

        """
        pass

    def test_get_plays_by_player_id(self) -> None:
        """Test case for get_plays_by_player_id

        """
        pass

    def test_get_plays_by_team(self) -> None:
        """Test case for get_plays_by_team

        """
        pass


if __name__ == '__main__':
    unittest.main()

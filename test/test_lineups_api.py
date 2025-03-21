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

from cbbd.api.lineups_api import LineupsApi  # noqa: E501


class TestLineupsApi(unittest.TestCase):
    """LineupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LineupsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_lineup_stats_by_game(self) -> None:
        """Test case for get_lineup_stats_by_game

        """
        pass

    def test_get_lineups_by_team_season(self) -> None:
        """Test case for get_lineups_by_team_season

        """
        pass


if __name__ == '__main__':
    unittest.main()

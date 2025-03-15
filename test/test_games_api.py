# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cbbd.api.games_api import GamesApi  # noqa: E501


class TestGamesApi(unittest.TestCase):
    """GamesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GamesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_broadcasts(self) -> None:
        """Test case for get_broadcasts

        """
        pass

    def test_get_game_players(self) -> None:
        """Test case for get_game_players

        """
        pass

    def test_get_game_teams(self) -> None:
        """Test case for get_game_teams

        """
        pass

    def test_get_games(self) -> None:
        """Test case for get_games

        """
        pass


if __name__ == '__main__':
    unittest.main()

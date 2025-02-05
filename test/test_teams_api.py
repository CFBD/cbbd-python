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

from cbbd.api.teams_api import TeamsApi  # noqa: E501


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TeamsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_team_roster(self) -> None:
        """Test case for get_team_roster

        """
        pass

    def test_get_teams(self) -> None:
        """Test case for get_teams

        """
        pass


if __name__ == '__main__':
    unittest.main()

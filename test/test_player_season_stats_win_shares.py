# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.11.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.player_season_stats_win_shares import PlayerSeasonStatsWinShares  # noqa: E501

class TestPlayerSeasonStatsWinShares(unittest.TestCase):
    """PlayerSeasonStatsWinShares unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerSeasonStatsWinShares:
        """Test PlayerSeasonStatsWinShares
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerSeasonStatsWinShares`
        """
        model = PlayerSeasonStatsWinShares()  # noqa: E501
        if include_optional:
            return PlayerSeasonStatsWinShares(
                total_per40 = 1.337,
                total = 1.337,
                defensive = 1.337,
                offensive = 1.337
            )
        else:
            return PlayerSeasonStatsWinShares(
                total_per40 = 1.337,
                total = 1.337,
                defensive = 1.337,
                offensive = 1.337,
        )
        """

    def testPlayerSeasonStatsWinShares(self):
        """Test PlayerSeasonStatsWinShares"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

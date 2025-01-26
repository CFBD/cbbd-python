# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.1.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.game_box_score_team_stats_points import GameBoxScoreTeamStatsPoints  # noqa: E501

class TestGameBoxScoreTeamStatsPoints(unittest.TestCase):
    """GameBoxScoreTeamStatsPoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxScoreTeamStatsPoints:
        """Test GameBoxScoreTeamStatsPoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxScoreTeamStatsPoints`
        """
        model = GameBoxScoreTeamStatsPoints()  # noqa: E501
        if include_optional:
            return GameBoxScoreTeamStatsPoints(
                fast_break = 1.337,
                off_turnovers = 1.337,
                in_paint = 1.337,
                by_period = [
                    1.337
                    ],
                largest_lead = 1.337,
                total = 1.337
            )
        else:
            return GameBoxScoreTeamStatsPoints(
                fast_break = 1.337,
                off_turnovers = 1.337,
                in_paint = 1.337,
                by_period = [
                    1.337
                    ],
                largest_lead = 1.337,
                total = 1.337,
        )
        """

    def testGameBoxScoreTeamStatsPoints(self):
        """Test GameBoxScoreTeamStatsPoints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

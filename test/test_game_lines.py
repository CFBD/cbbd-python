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
import datetime

from cbbd.models.game_lines import GameLines  # noqa: E501

class TestGameLines(unittest.TestCase):
    """GameLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameLines:
        """Test GameLines
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameLines`
        """
        model = GameLines()  # noqa: E501
        if include_optional:
            return GameLines(
                game_id = 56,
                season = 56,
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                home_team_id = 56,
                home_team = '',
                home_conference = '',
                home_score = 1.337,
                away_team_id = 56,
                away_team = '',
                away_conference = '',
                away_score = 1.337,
                lines = [
                    cbbd.models.game_line_info.GameLineInfo(
                        provider = '', 
                        spread = 1.337, 
                        over_under = 1.337, 
                        home_moneyline = 1.337, 
                        away_moneyline = 1.337, 
                        spread_open = 1.337, 
                        over_under_open = 1.337, )
                    ]
            )
        else:
            return GameLines(
                game_id = 56,
                season = 56,
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                home_team_id = 56,
                home_team = '',
                home_conference = '',
                home_score = 1.337,
                away_team_id = 56,
                away_team = '',
                away_conference = '',
                away_score = 1.337,
                lines = [
                    cbbd.models.game_line_info.GameLineInfo(
                        provider = '', 
                        spread = 1.337, 
                        over_under = 1.337, 
                        home_moneyline = 1.337, 
                        away_moneyline = 1.337, 
                        spread_open = 1.337, 
                        over_under_open = 1.337, )
                    ],
        )
        """

    def testGameLines(self):
        """Test GameLines"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

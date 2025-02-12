# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.11.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.game_info import GameInfo  # noqa: E501

class TestGameInfo(unittest.TestCase):
    """GameInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameInfo:
        """Test GameInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameInfo`
        """
        model = GameInfo()  # noqa: E501
        if include_optional:
            return GameInfo(
                id = 56,
                source_id = '',
                season_label = '',
                season = 56,
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                neutral_site = True,
                conference_game = True,
                game_type = '',
                status = 'scheduled',
                attendance = 56,
                home_team_id = 56,
                home_team = '',
                home_conference_id = 56,
                home_conference = '',
                home_points = 56,
                home_period_points = [
                    56
                    ],
                home_winner = True,
                away_team_id = 56,
                away_team = '',
                away_conference_id = 56,
                away_conference = '',
                away_points = 56,
                away_period_points = [
                    56
                    ],
                away_winner = True,
                excitement = 1.337,
                venue_id = 56,
                venue = '',
                city = '',
                state = ''
            )
        else:
            return GameInfo(
                id = 56,
                source_id = '',
                season_label = '',
                season = 56,
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                neutral_site = True,
                conference_game = True,
                game_type = '',
                status = 'scheduled',
                attendance = 56,
                home_team_id = 56,
                home_team = '',
                home_conference_id = 56,
                home_conference = '',
                home_points = 56,
                home_period_points = [
                    56
                    ],
                home_winner = True,
                away_team_id = 56,
                away_team = '',
                away_conference_id = 56,
                away_conference = '',
                away_points = 56,
                away_period_points = [
                    56
                    ],
                away_winner = True,
                excitement = 1.337,
                venue_id = 56,
                venue = '',
                city = '',
                state = '',
        )
        """

    def testGameInfo(self):
        """Test GameInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

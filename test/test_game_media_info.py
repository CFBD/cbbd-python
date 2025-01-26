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

from cbbd.models.game_media_info import GameMediaInfo  # noqa: E501

class TestGameMediaInfo(unittest.TestCase):
    """GameMediaInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameMediaInfo:
        """Test GameMediaInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameMediaInfo`
        """
        model = GameMediaInfo()  # noqa: E501
        if include_optional:
            return GameMediaInfo(
                game_id = 56,
                season = 56,
                season_label = '',
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                home_team_id = 56,
                home_team = '',
                home_conference = '',
                away_team_id = 56,
                away_team = '',
                away_conference = '',
                neutral_site = True,
                conference_game = True,
                game_type = '',
                notes = '',
                broadcasts = [
                    cbbd.models.game_media_info_broadcasts_inner.GameMediaInfo_broadcasts_inner(
                        broadcast_name = '', 
                        broadcast_type = '', )
                    ]
            )
        else:
            return GameMediaInfo(
                game_id = 56,
                season = 56,
                season_label = '',
                season_type = 'postseason',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                home_team_id = 56,
                home_team = '',
                home_conference = '',
                away_team_id = 56,
                away_team = '',
                away_conference = '',
                neutral_site = True,
                conference_game = True,
                game_type = '',
                notes = '',
                broadcasts = [
                    cbbd.models.game_media_info_broadcasts_inner.GameMediaInfo_broadcasts_inner(
                        broadcast_name = '', 
                        broadcast_type = '', )
                    ],
        )
        """

    def testGameMediaInfo(self):
        """Test GameMediaInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

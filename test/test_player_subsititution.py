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
import datetime

from cbbd.models.player_subsititution import PlayerSubsititution  # noqa: E501

class TestPlayerSubsititution(unittest.TestCase):
    """PlayerSubsititution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerSubsititution:
        """Test PlayerSubsititution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerSubsititution`
        """
        model = PlayerSubsititution()  # noqa: E501
        if include_optional:
            return PlayerSubsititution(
                game_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                team_id = 56,
                team = '',
                conference = '',
                athlete_id = 56,
                athlete = '',
                position = '',
                opponent_id = 56,
                opponent = '',
                opponent_conference = '',
                sub_in = cbbd.models.player_subsititution_sub_in.PlayerSubsititution_subIn(
                    opponent_points = 56, 
                    team_points = 56, 
                    seconds_remaining = 56, 
                    period = 56, ),
                sub_out = cbbd.models.player_subsititution_sub_in.PlayerSubsititution_subIn(
                    opponent_points = 56, 
                    team_points = 56, 
                    seconds_remaining = 56, 
                    period = 56, )
            )
        else:
            return PlayerSubsititution(
                game_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                team_id = 56,
                team = '',
                conference = '',
                athlete_id = 56,
                athlete = '',
                position = '',
                opponent_id = 56,
                opponent = '',
                opponent_conference = '',
                sub_in = cbbd.models.player_subsititution_sub_in.PlayerSubsititution_subIn(
                    opponent_points = 56, 
                    team_points = 56, 
                    seconds_remaining = 56, 
                    period = 56, ),
                sub_out = cbbd.models.player_subsititution_sub_in.PlayerSubsititution_subIn(
                    opponent_points = 56, 
                    team_points = 56, 
                    seconds_remaining = 56, 
                    period = 56, ),
        )
        """

    def testPlayerSubsititution(self):
        """Test PlayerSubsititution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

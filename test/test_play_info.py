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

from cbbd.models.play_info import PlayInfo  # noqa: E501

class TestPlayInfo(unittest.TestCase):
    """PlayInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayInfo:
        """Test PlayInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayInfo`
        """
        model = PlayInfo()  # noqa: E501
        if include_optional:
            return PlayInfo(
                id = 56,
                source_id = '',
                game_id = 56,
                game_source_id = '',
                game_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                season = 1.337,
                season_type = 'postseason',
                game_type = '',
                tournament = '',
                play_type = '',
                is_home_team = True,
                team_id = 56,
                team = '',
                conference = '',
                team_seed = 1.337,
                opponent_id = 56,
                opponent = '',
                opponent_conference = '',
                opponent_seed = 1.337,
                period = 56,
                clock = '',
                seconds_remaining = 56,
                home_score = 56,
                away_score = 56,
                home_win_probability = 1.337,
                scoring_play = True,
                shooting_play = True,
                score_value = 1.337,
                wallclock = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                play_text = '',
                participants = [
                    cbbd.models.play_info_participants_inner.PlayInfo_participants_inner(
                        name = '', 
                        id = 56, )
                    ],
                on_floor = [
                    cbbd.models.play_info_on_floor_inner.PlayInfo_onFloor_inner(
                        team = '', 
                        name = '', 
                        id = 56, )
                    ],
                shot_info = cbbd.models.shot_info.ShotInfo(
                    shooter = cbbd.models.shot_info_shooter.ShotInfo_shooter(
                        name = '', 
                        id = 56, ), 
                    made = True, 
                    range = 'rim', 
                    assisted = True, 
                    assisted_by = cbbd.models.shot_info_shooter.ShotInfo_shooter(
                        name = '', 
                        id = 56, ), 
                    location = cbbd.models.shot_info_location.ShotInfo_location(
                        y = 1.337, 
                        x = 1.337, ), )
            )
        else:
            return PlayInfo(
                id = 56,
                source_id = '',
                game_id = 56,
                game_source_id = '',
                game_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                season = 1.337,
                season_type = 'postseason',
                game_type = '',
                tournament = '',
                play_type = '',
                is_home_team = True,
                team_id = 56,
                team = '',
                conference = '',
                team_seed = 1.337,
                opponent_id = 56,
                opponent = '',
                opponent_conference = '',
                opponent_seed = 1.337,
                period = 56,
                clock = '',
                seconds_remaining = 56,
                home_score = 56,
                away_score = 56,
                home_win_probability = 1.337,
                scoring_play = True,
                shooting_play = True,
                score_value = 1.337,
                wallclock = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                play_text = '',
                participants = [
                    cbbd.models.play_info_participants_inner.PlayInfo_participants_inner(
                        name = '', 
                        id = 56, )
                    ],
                on_floor = [
                    cbbd.models.play_info_on_floor_inner.PlayInfo_onFloor_inner(
                        team = '', 
                        name = '', 
                        id = 56, )
                    ],
                shot_info = cbbd.models.shot_info.ShotInfo(
                    shooter = cbbd.models.shot_info_shooter.ShotInfo_shooter(
                        name = '', 
                        id = 56, ), 
                    made = True, 
                    range = 'rim', 
                    assisted = True, 
                    assisted_by = cbbd.models.shot_info_shooter.ShotInfo_shooter(
                        name = '', 
                        id = 56, ), 
                    location = cbbd.models.shot_info_location.ShotInfo_location(
                        y = 1.337, 
                        x = 1.337, ), ),
        )
        """

    def testPlayInfo(self):
        """Test PlayInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.5.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.game_box_score_players_players_inner import GameBoxScorePlayersPlayersInner  # noqa: E501

class TestGameBoxScorePlayersPlayersInner(unittest.TestCase):
    """GameBoxScorePlayersPlayersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxScorePlayersPlayersInner:
        """Test GameBoxScorePlayersPlayersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxScorePlayersPlayersInner`
        """
        model = GameBoxScorePlayersPlayersInner()  # noqa: E501
        if include_optional:
            return GameBoxScorePlayersPlayersInner(
                rebounds = cbbd.models.team_season_unit_stats_rebounds.TeamSeasonUnitStats_rebounds(
                    total = 1.337, 
                    defensive = 1.337, 
                    offensive = 1.337, ),
                free_throws = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                three_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                two_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                offensive_rebound_pct = 1.337,
                free_throw_rate = 1.337,
                assists_turnover_ratio = 1.337,
                game_score = 1.337,
                true_shooting_pct = 1.337,
                effective_field_goal_pct = 1.337,
                net_rating = 1.337,
                defensive_rating = 1.337,
                offensive_rating = 1.337,
                usage = 1.337,
                blocks = 1.337,
                steals = 1.337,
                assists = 1.337,
                fouls = 1.337,
                turnovers = 1.337,
                points = 1.337,
                minutes = 1.337,
                ejected = True,
                starter = True,
                position = '',
                name = '',
                athlete_source_id = '',
                athlete_id = 56
            )
        else:
            return GameBoxScorePlayersPlayersInner(
                rebounds = cbbd.models.team_season_unit_stats_rebounds.TeamSeasonUnitStats_rebounds(
                    total = 1.337, 
                    defensive = 1.337, 
                    offensive = 1.337, ),
                free_throws = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                three_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                two_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                offensive_rebound_pct = 1.337,
                free_throw_rate = 1.337,
                assists_turnover_ratio = 1.337,
                game_score = 1.337,
                true_shooting_pct = 1.337,
                effective_field_goal_pct = 1.337,
                net_rating = 1.337,
                defensive_rating = 1.337,
                offensive_rating = 1.337,
                usage = 1.337,
                blocks = 1.337,
                steals = 1.337,
                assists = 1.337,
                fouls = 1.337,
                turnovers = 1.337,
                points = 1.337,
                minutes = 1.337,
                ejected = True,
                starter = True,
                position = '',
                name = '',
                athlete_source_id = '',
                athlete_id = 56,
        )
        """

    def testGameBoxScorePlayersPlayersInner(self):
        """Test GameBoxScorePlayersPlayersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

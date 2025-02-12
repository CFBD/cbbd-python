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

from cbbd.models.team_season_unit_stats import TeamSeasonUnitStats  # noqa: E501

class TestTeamSeasonUnitStats(unittest.TestCase):
    """TeamSeasonUnitStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamSeasonUnitStats:
        """Test TeamSeasonUnitStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamSeasonUnitStats`
        """
        model = TeamSeasonUnitStats()  # noqa: E501
        if include_optional:
            return TeamSeasonUnitStats(
                field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                two_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                three_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                free_throws = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                rebounds = cbbd.models.team_season_unit_stats_rebounds.TeamSeasonUnitStats_rebounds(
                    total = 1.337, 
                    defensive = 1.337, 
                    offensive = 1.337, ),
                turnovers = cbbd.models.team_season_unit_stats_turnovers.TeamSeasonUnitStats_turnovers(
                    team_total = 1.337, 
                    total = 1.337, ),
                fouls = cbbd.models.team_season_unit_stats_fouls.TeamSeasonUnitStats_fouls(
                    flagrant = 1.337, 
                    technical = 1.337, 
                    total = 1.337, ),
                points = cbbd.models.team_season_unit_stats_points.TeamSeasonUnitStats_points(
                    fast_break = 1.337, 
                    off_turnovers = 1.337, 
                    in_paint = 1.337, 
                    total = 1.337, ),
                four_factors = cbbd.models.team_season_unit_stats_four_factors.TeamSeasonUnitStats_fourFactors(
                    free_throw_rate = 1.337, 
                    offensive_rebound_pct = 1.337, 
                    turnover_ratio = 1.337, 
                    effective_field_goal_pct = 1.337, ),
                assists = 1.337,
                blocks = 1.337,
                steals = 1.337,
                possessions = 1.337,
                rating = 1.337,
                true_shooting = 1.337
            )
        else:
            return TeamSeasonUnitStats(
                field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                two_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                three_point_field_goals = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                free_throws = cbbd.models.team_season_unit_stats_field_goals.TeamSeasonUnitStats_fieldGoals(
                    pct = 1.337, 
                    attempted = 1.337, 
                    made = 1.337, ),
                rebounds = cbbd.models.team_season_unit_stats_rebounds.TeamSeasonUnitStats_rebounds(
                    total = 1.337, 
                    defensive = 1.337, 
                    offensive = 1.337, ),
                turnovers = cbbd.models.team_season_unit_stats_turnovers.TeamSeasonUnitStats_turnovers(
                    team_total = 1.337, 
                    total = 1.337, ),
                fouls = cbbd.models.team_season_unit_stats_fouls.TeamSeasonUnitStats_fouls(
                    flagrant = 1.337, 
                    technical = 1.337, 
                    total = 1.337, ),
                points = cbbd.models.team_season_unit_stats_points.TeamSeasonUnitStats_points(
                    fast_break = 1.337, 
                    off_turnovers = 1.337, 
                    in_paint = 1.337, 
                    total = 1.337, ),
                four_factors = cbbd.models.team_season_unit_stats_four_factors.TeamSeasonUnitStats_fourFactors(
                    free_throw_rate = 1.337, 
                    offensive_rebound_pct = 1.337, 
                    turnover_ratio = 1.337, 
                    effective_field_goal_pct = 1.337, ),
                assists = 1.337,
                blocks = 1.337,
                steals = 1.337,
                possessions = 1.337,
                rating = 1.337,
                true_shooting = 1.337,
        )
        """

    def testTeamSeasonUnitStats(self):
        """Test TeamSeasonUnitStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

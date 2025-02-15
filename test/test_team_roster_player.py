# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.12.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.team_roster_player import TeamRosterPlayer  # noqa: E501

class TestTeamRosterPlayer(unittest.TestCase):
    """TeamRosterPlayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamRosterPlayer:
        """Test TeamRosterPlayer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamRosterPlayer`
        """
        model = TeamRosterPlayer()  # noqa: E501
        if include_optional:
            return TeamRosterPlayer(
                id = 56,
                source_id = '',
                name = '',
                first_name = '',
                last_name = '',
                jersey = '',
                position = '',
                height = 1.337,
                weight = 1.337,
                hometown = cbbd.models.team_roster_player_hometown.TeamRosterPlayer_hometown(
                    country = '', 
                    state = '', 
                    city = '', ),
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                start_season = 1.337,
                end_season = 1.337
            )
        else:
            return TeamRosterPlayer(
                id = 56,
                source_id = '',
                name = '',
                first_name = '',
                last_name = '',
                jersey = '',
                position = '',
                height = 1.337,
                weight = 1.337,
                hometown = cbbd.models.team_roster_player_hometown.TeamRosterPlayer_hometown(
                    country = '', 
                    state = '', 
                    city = '', ),
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                start_season = 1.337,
                end_season = 1.337,
        )
        """

    def testTeamRosterPlayer(self):
        """Test TeamRosterPlayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

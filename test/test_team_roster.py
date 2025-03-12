# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.18.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.team_roster import TeamRoster  # noqa: E501

class TestTeamRoster(unittest.TestCase):
    """TeamRoster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamRoster:
        """Test TeamRoster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamRoster`
        """
        model = TeamRoster()  # noqa: E501
        if include_optional:
            return TeamRoster(
                team_id = 56,
                team_source_id = '',
                team = '',
                conference = '',
                season = 1.337,
                players = [
                    cbbd.models.team_roster_player.TeamRosterPlayer(
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
                            county_fips = '', 
                            longitude = 1.337, 
                            latitude = 1.337, 
                            country = '', 
                            state = '', 
                            city = '', ), 
                        date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        start_season = 1.337, 
                        end_season = 1.337, )
                    ]
            )
        else:
            return TeamRoster(
                team_id = 56,
                team_source_id = '',
                team = '',
                conference = '',
                season = 1.337,
                players = [
                    cbbd.models.team_roster_player.TeamRosterPlayer(
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
                            county_fips = '', 
                            longitude = 1.337, 
                            latitude = 1.337, 
                            country = '', 
                            state = '', 
                            city = '', ), 
                        date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        start_season = 1.337, 
                        end_season = 1.337, )
                    ],
        )
        """

    def testTeamRoster(self):
        """Test TeamRoster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.13.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.team_info import TeamInfo  # noqa: E501

class TestTeamInfo(unittest.TestCase):
    """TeamInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamInfo:
        """Test TeamInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamInfo`
        """
        model = TeamInfo()  # noqa: E501
        if include_optional:
            return TeamInfo(
                id = 56,
                source_id = '',
                school = '',
                mascot = '',
                abbreviation = '',
                display_name = '',
                short_display_name = '',
                primary_color = '',
                secondary_color = '',
                current_venue_id = 56,
                current_venue = '',
                current_city = '',
                current_state = '',
                conference_id = 56,
                conference = ''
            )
        else:
            return TeamInfo(
                id = 56,
                source_id = '',
                school = '',
                mascot = '',
                abbreviation = '',
                display_name = '',
                short_display_name = '',
                primary_color = '',
                secondary_color = '',
                current_venue_id = 56,
                current_venue = '',
                current_city = '',
                current_state = '',
                conference_id = 56,
                conference = '',
        )
        """

    def testTeamInfo(self):
        """Test TeamInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

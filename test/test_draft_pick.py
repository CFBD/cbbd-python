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

from cbbd.models.draft_pick import DraftPick  # noqa: E501

class TestDraftPick(unittest.TestCase):
    """DraftPick unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DraftPick:
        """Test DraftPick
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DraftPick`
        """
        model = DraftPick()  # noqa: E501
        if include_optional:
            return DraftPick(
                athlete_id = 56,
                source_team_id = 56,
                source_team_location = '',
                source_team_name = '',
                source_team_league_affiliation = '',
                source_team_college_id = 1.337,
                draft_team_id = 1.337,
                draft_team = '',
                year = 56,
                overall = 56,
                round = 56,
                pick = 56,
                name = '',
                overall_rank = 56,
                position_rank = 56,
                height = 56,
                weight = 56
            )
        else:
            return DraftPick(
                athlete_id = 56,
                source_team_id = 56,
                source_team_location = '',
                source_team_name = '',
                source_team_league_affiliation = '',
                source_team_college_id = 1.337,
                draft_team_id = 1.337,
                draft_team = '',
                year = 56,
                overall = 56,
                round = 56,
                pick = 56,
                name = '',
                overall_rank = 56,
                position_rank = 56,
                height = 56,
                weight = 56,
        )
        """

    def testDraftPick(self):
        """Test DraftPick"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

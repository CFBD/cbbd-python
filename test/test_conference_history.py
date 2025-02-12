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

from cbbd.models.conference_history import ConferenceHistory  # noqa: E501

class TestConferenceHistory(unittest.TestCase):
    """ConferenceHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceHistory:
        """Test ConferenceHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceHistory`
        """
        model = ConferenceHistory()  # noqa: E501
        if include_optional:
            return ConferenceHistory(
                id = 56,
                source_id = '',
                name = '',
                abbreviation = '',
                short_name = '',
                teams = [
                    cbbd.models.conference_history_teams_inner.ConferenceHistory_teams_inner(
                        end_season = 56, 
                        start_season = 56, 
                        mascot = '', 
                        school = '', 
                        source_id = '', 
                        id = 56, )
                    ]
            )
        else:
            return ConferenceHistory(
                id = 56,
                source_id = '',
                name = '',
                abbreviation = '',
                short_name = '',
                teams = [
                    cbbd.models.conference_history_teams_inner.ConferenceHistory_teams_inner(
                        end_season = 56, 
                        start_season = 56, 
                        mascot = '', 
                        school = '', 
                        source_id = '', 
                        id = 56, )
                    ],
        )
        """

    def testConferenceHistory(self):
        """Test ConferenceHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

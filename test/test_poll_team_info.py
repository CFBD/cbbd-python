# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.9.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.poll_team_info import PollTeamInfo  # noqa: E501

class TestPollTeamInfo(unittest.TestCase):
    """PollTeamInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PollTeamInfo:
        """Test PollTeamInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PollTeamInfo`
        """
        model = PollTeamInfo()  # noqa: E501
        if include_optional:
            return PollTeamInfo(
                season = 56,
                season_type = 'postseason',
                week = 56,
                poll_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                poll_type = '',
                team_id = 1.337,
                team = '',
                conference = '',
                ranking = 1.337,
                points = 1.337,
                first_place_votes = 1.337
            )
        else:
            return PollTeamInfo(
                season = 56,
                season_type = 'postseason',
                week = 56,
                poll_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                poll_type = '',
                team_id = 1.337,
                team = '',
                conference = '',
                ranking = 1.337,
                points = 1.337,
                first_place_votes = 1.337,
        )
        """

    def testPollTeamInfo(self):
        """Test PollTeamInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

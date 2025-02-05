# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.adjusted_efficiency_info import AdjustedEfficiencyInfo  # noqa: E501

class TestAdjustedEfficiencyInfo(unittest.TestCase):
    """AdjustedEfficiencyInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdjustedEfficiencyInfo:
        """Test AdjustedEfficiencyInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdjustedEfficiencyInfo`
        """
        model = AdjustedEfficiencyInfo()  # noqa: E501
        if include_optional:
            return AdjustedEfficiencyInfo(
                season = 56,
                team_id = 56,
                team = '',
                conference = '',
                offensive_rating = 1.337,
                defensive_rating = 1.337,
                net_rating = 1.337
            )
        else:
            return AdjustedEfficiencyInfo(
                season = 56,
                team_id = 56,
                team = '',
                conference = '',
                offensive_rating = 1.337,
                defensive_rating = 1.337,
                net_rating = 1.337,
        )
        """

    def testAdjustedEfficiencyInfo(self):
        """Test AdjustedEfficiencyInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

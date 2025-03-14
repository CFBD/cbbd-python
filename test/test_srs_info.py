# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.srs_info import SrsInfo  # noqa: E501

class TestSrsInfo(unittest.TestCase):
    """SrsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SrsInfo:
        """Test SrsInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SrsInfo`
        """
        model = SrsInfo()  # noqa: E501
        if include_optional:
            return SrsInfo(
                season = 56,
                team_id = 56,
                team = '',
                conference = '',
                rating = 1.337
            )
        else:
            return SrsInfo(
                season = 56,
                team_id = 56,
                team = '',
                conference = '',
                rating = 1.337,
        )
        """

    def testSrsInfo(self):
        """Test SrsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

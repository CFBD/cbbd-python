# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.18.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.shot_info_location import ShotInfoLocation  # noqa: E501

class TestShotInfoLocation(unittest.TestCase):
    """ShotInfoLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShotInfoLocation:
        """Test ShotInfoLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShotInfoLocation`
        """
        model = ShotInfoLocation()  # noqa: E501
        if include_optional:
            return ShotInfoLocation(
                y = 1.337,
                x = 1.337
            )
        else:
            return ShotInfoLocation(
                y = 1.337,
                x = 1.337,
        )
        """

    def testShotInfoLocation(self):
        """Test ShotInfoLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

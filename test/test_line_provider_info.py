# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.11.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.line_provider_info import LineProviderInfo  # noqa: E501

class TestLineProviderInfo(unittest.TestCase):
    """LineProviderInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineProviderInfo:
        """Test LineProviderInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineProviderInfo`
        """
        model = LineProviderInfo()  # noqa: E501
        if include_optional:
            return LineProviderInfo(
                id = 56,
                name = ''
            )
        else:
            return LineProviderInfo(
                id = 56,
                name = '',
        )
        """

    def testLineProviderInfo(self):
        """Test LineProviderInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

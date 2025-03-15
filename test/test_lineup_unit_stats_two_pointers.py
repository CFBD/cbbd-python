# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cbbd.models.lineup_unit_stats_two_pointers import LineupUnitStatsTwoPointers  # noqa: E501

class TestLineupUnitStatsTwoPointers(unittest.TestCase):
    """LineupUnitStatsTwoPointers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineupUnitStatsTwoPointers:
        """Test LineupUnitStatsTwoPointers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineupUnitStatsTwoPointers`
        """
        model = LineupUnitStatsTwoPointers()  # noqa: E501
        if include_optional:
            return LineupUnitStatsTwoPointers(
                made = 56,
                attempted = 56,
                pct = 1.337,
                jumpers = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                layups = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                dunks = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                tip_ins = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, )
            )
        else:
            return LineupUnitStatsTwoPointers(
                made = 56,
                attempted = 56,
                pct = 1.337,
                jumpers = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                layups = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                dunks = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
                tip_ins = cbbd.models.shooting_stats.ShootingStats(
                    made = 56, 
                    attempted = 56, 
                    pct = 1.337, ),
        )
        """

    def testLineupUnitStatsTwoPointers(self):
        """Test LineupUnitStatsTwoPointers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

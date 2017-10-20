# coding: utf-8

"""
    stylelens-detect

    This is a API document for Object Detection on fashion items\"

    OpenAPI spec version: 0.0.1
    Contact: devops@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_detect
from stylelens_detect.rest import ApiException
from stylelens_detect.apis.detect_api import DetectApi


class TestDetectApi(unittest.TestCase):
    """ DetectApi unit test stubs """

    def setUp(self):
        self.api = stylelens_detect.apis.detect_api.DetectApi()

    def tearDown(self):
        pass

    def test_detect_objects(self):
        """
        Test case for detect_objects

        Query to detect obejects in the image you sent
        """
        pass


if __name__ == '__main__':
    unittest.main()

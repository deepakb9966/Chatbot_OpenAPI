# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.predicted_message200_response import PredictedMessage200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_predicted_message(self):
        """Test case for predicted_message

        get the predicted message
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/predict',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

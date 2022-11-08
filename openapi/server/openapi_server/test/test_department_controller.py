# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.predict_request import PredictRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDepartmentController(BaseTestCase):
    """DepartmentController integration test stubs"""

    def test_predict(self):
        """Test case for predict

        Enter a message to predict the intent
        """
        predict_request = openapi_server.PredictRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/predict',
            method='POST',
            headers=headers,
            data=json.dumps(predict_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

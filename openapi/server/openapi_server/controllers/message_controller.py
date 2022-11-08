import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from flask import jsonify
from openapi_server.models.predict_request import PredictRequest  # noqa: E501
from openapi_server.models.predicted_message200_response import PredictedMessage200Response  # noqa: E501
from openapi_server import util
from openapi_server.app import predict_intent


def predict(predict_request=None):  # noqa: E501
    """Enter a message to predict the intent

    Enter a message to predict the intent # noqa: E501

    :param predict_request: Enter message
    :type predict_request: dict | bytes

    :rtype: Union[PredictedMessage200Response, Tuple[PredictedMessage200Response, int], Tuple[PredictedMessage200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        predict_request = PredictRequest.from_dict(connexion.request.get_json())  # noqa: E501
    print(type(predict_request.message))
    print((predict_intent(predict_request.message)))
    return jsonify(predict_intent(predict_request.message))
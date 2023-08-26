"""test Cases:
TC#1 - verify the status code, headers.
TC#2 - Verify the body -> Booking ID.
TC#3 - verify the JSON schema is valid."""

import json
import pytest
from src.constants.api_constants import base_url, url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import create_booking_payload
from src.helpers.utils import common_header
from src.helpers.common_verifications import verify_key, verify_http_code

class TestIntegration(object):

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), None, common_header(), create_booking_payload(), False)
        print(response)
        #response_data = response.json()
        verify_http_code(response, 200)
        verify_key(response,"bookingid")

    # def test_create_booking_tc2(self):
    #     assert True == False
    #
    # def test_create_booking_tc3(self):
    #     assert True == True

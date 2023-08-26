# Verify the https status code:

def verify_http_code(response_data, expected_data):
    assert response_data.status_code == int(expected_data), "Expected HTTP status :" + expected_data


# Any key, should not be null or empty.

def verify_key(response_data, key):
    assert len(response_data) != 0, "key is non Empty :" + key
    assert response_data[key] > 0, "key should be grater than 0 :" + key

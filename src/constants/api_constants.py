# Add your constants here.
# Keep the urls in different functions. As, like this we can run the functions with different environment urls.

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_booking(booking_id):
    return "https://restful-booker.herokuapp.com/" + booking_id

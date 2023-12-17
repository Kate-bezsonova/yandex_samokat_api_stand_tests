import sender_stand_request

def test_order_get_succes():
    str_order_track = str(sender_stand_request.create_new_order().json()["track"])
    order_response = sender_stand_request.get_order_by_track(str_order_track)
    assert order_response.status_code == 200
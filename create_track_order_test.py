import data
import sender_stand_request


def get_order_by_track():
    order_body = data.order_body
    order_response = sender_stand_request.post_new_order(order_body)
    return order_response.json()["track"]


def positive_assert(order_track):
    track_order = get_order_by_track(order_track)
    track_response = sender_stand_request.get_search_order_by_track()

    assert track_response.status_code == 200
    assert track_response.json()["track"] == order_track
    print(track_response.json())

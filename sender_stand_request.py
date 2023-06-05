import configuration
import requests
import data


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


order_response = post_new_order(data.order_body);
print(order_response.status_code)
print(order_response.json())


def post_track(order_track, track):
    headers_dict = data.order_body.copy()
    headers_dict["track"] = track;
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                        json=order_track)


def post_track_order(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=order_track)


track_response = post_track_order(data.order_track);
print(track_response.status_code)
print(track_response.json())

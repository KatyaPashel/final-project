import configuration
import requests
import data


# Пашель Катя, 5-я когорта — Финальный проект. Инженер по тестированию плюс

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


order_response = post_new_order(data.order_body);
print(order_response.status_code)
print(order_response.json())


def get_track_order():
    order_body = data.order_body
    response_order = post_new_order(data.order_body)
    return response_order.json()["track"]


def get_search_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_TRACK + get_track_order()["track"])


print(order_response.status_code)
print(order_response.json())

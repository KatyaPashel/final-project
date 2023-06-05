import sender_stand_request
import data

# Функция для получения track
def get_track():
    order_body = data.order_body
    order_response = sender_stand_request.post_new_order(order_body)
    return order_response.json()["track"]



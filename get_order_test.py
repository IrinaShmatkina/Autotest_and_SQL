# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def get_track_number():
    order_body = data.order_body.copy()
    track = sender_stand_request.post_create_order(order_body).json().get("track")
    track_body = data.track_body.copy()
    track_body["t"] = track
    return track_body

def test_positive_get_order_by_track():
    track = get_track_number()
    assert sender_stand_request.get_order_by_track(track).status_code == 200





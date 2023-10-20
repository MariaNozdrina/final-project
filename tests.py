import sender_stand_request
import data

#Проверка статуса кода

def test_get_order_by_track():
    track = sender_stand_request.post_new_order(data.user_body).json()['track']
    response = sender_stand_request.get_order_by_track(track)
    assert  response.status_code == 200

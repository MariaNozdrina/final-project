import configuration
import requests
import  data

#Создание заказа + получение трекера
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREARING_AN_ORDER,
                         json=body)

 # Получение заказа по треку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER + str(track))


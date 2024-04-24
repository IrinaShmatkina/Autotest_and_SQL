
import configuration
import requests
import data

def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)

def get_order_by_track(parametrs):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=parametrs)


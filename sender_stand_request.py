import configuration
import requests
import data

def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                                   json=data.order_body,
                                   headers=data.headers)
def get_order_by_track(order_track):
    NEW_GET_ORDER_BY_TRACK = configuration.GET_ORDER_BY_TRACK + order_track
    return requests.get(configuration.URL_SERVICE + NEW_GET_ORDER_BY_TRACK)
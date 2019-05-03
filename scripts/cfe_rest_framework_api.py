import json
import requests
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "Pokemon.png")


def do_img(method='get', data={}, is__json=True, img_path=None):
    headers = {}
    if is__json:
        headers['content-types'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image':image
            }
            r = requests.request(method, ENDPOINT , data=data, files=file_data)
    else:
        r = requests.request(method, ENDPOINT , data=data)

    print(r.text)
    return r



do_img(method='post', data={'user':1, 'content':""}, is__json=False, img_path=image_path)


def do(method='get', data={}, is__json=True):
    headers = {}
    if is__json:
        headers['content-types'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT , data=data, headers=headers)
    print(r.text)
    return r


#do(data='id' : 12})

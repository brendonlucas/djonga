import requests
from django.test import TestCase


# Create your tests here.


def main():
    r = requests.post('http://127.0.0.1:8181/api-token-auth2/', data={"username": 'lucas', "password": '12345678'})
    print(r.status_code)
    print(r.text)

    #
    # ro = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    # print(ro.status_code)
    # print(ro.text)
    #
    # token = r.json()["token"]
    # print(token)
    # b = requests.get('http://127.0.0.1:8000/users/', headers={"Authorization": "Token " + str(token)})
    # print(b.text)


if __name__ == '__main__':
    main()

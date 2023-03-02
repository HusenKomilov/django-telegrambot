import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1'


def create_user(username, name, user_id):
    url = f"{BASE_URL}/users/"
    post = requests.post(url=url, data={
        'username': username,
        'name': name,
        'user_id': user_id
    })


def create_feedback(user_id, body):
    url = f"{BASE_URL}/feedbacks/"
    if body and user_id:
        post = requests.post(url=url, data={
            'user_id': user_id,
            'body': body
        })
        return "Adminga jo'natildi fikringiz uchun raxmat"
    else:
        return "Amal oxiriga yetmadi"

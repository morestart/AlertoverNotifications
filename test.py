import requests

data={
        "source": "s-9a80727e-7a24-4f04-b806-9d11fb91",
        "receiver": "u-ecb018e5-d0fd-4ab2-a351-437e9dc5",
        "content": "hello world",
        "title": "hello"
    }
requests.post(
    "https://api.alertover.com/v1/alert",
    data=data
)
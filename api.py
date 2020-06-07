import requests
from requests.exceptions import HTTPError


class Api:
    def __init__(self, id):
        self.id = id
        self.method = "https://api.vk.com/method/"
        self.user = "users.get?user_ids="
        self.fhotos = "photos.getAlbums?owner_id="
        self.albums = "&album_ids=title"
        self.friends = "friends.get?user_id="
        self.fields = "&fields=nickname"
        self.token = "&v=5.107&access_token=c5955299c5955299c595529924c5e72fd8cc595c59552999b481ea4a5e5e0d9b055d64f"
        self.request()

    def request(self):
        try:
            user = requests.get(f'{self.method}{self.user}{self.id}{self.token}')
            info = user.json()['response'][0]
            self.id = info['id']
            print("User:")
            print(info["first_name"], info['last_name'], '\n')
        except HTTPError as error:
            print(error)

        try:
            fhotos = requests.get(f'{self.method}{self.fhotos}{self.id}{self.albums}{self.token}')
            print("Albums:")
            info = fhotos.json()["response"]["items"]
            for elem in info:
                print(elem['title'])
            print('\n')
        except HTTPError as error:
            print(error)

        try:
            friends = requests.get(f'{self.method}{self.friends}{self.id}{self.fields}{self.token}')
            print("Friends:")
            info = friends.json()["response"]["items"]
            for elem in info:
                print(elem["first_name"], elem['last_name'])
        except HTTPError as error:
            print(error)


if __name__ == '__main__':
    while True:
        print("Введите id пользователя")
        request = input()
        ex = Api(request)


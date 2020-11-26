import requests


class Doge:
    base_url = "https://dog.ceo/api"

    def all_breeds(self):
        return requests.get(f"{self.base_url}/breeds/list/all").json()

    def random_images(self, num):
        return requests.get(f"{self.base_url}/breeds/image/random/{num}").json()

    def sub_breeds(self, name):
        return requests.get(f"{self.base_url}/breed/{name}/list").json()

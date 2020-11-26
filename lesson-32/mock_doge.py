import requests


class Doge:
    base_url = "https://dog.ceo/api"

    def all_breeds(self):
        return requests.get(f"{self.base_url}/breeds/list/all").json()

import requests


class SportsEquipmentClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_item(self, name, quantity):
        url = f"{self.base_url}/item/"
        payload = {"name": name, "quantity": quantity}
        response = requests.post(url, json=payload)
        return response.json()

    def update_item(self, item_id, quantity):
        url = f"{self.base_url}/update/{item_id}/"
        payload = {"quantity": quantity}
        response = requests.put(url, json=payload)
        return response.json()

    def get_items(self):
        url = f"{self.base_url}/items/"
        response = requests.get(url)
        return response.json()


if __name__ == "__main__":
    client = SportsEquipmentClient("http://localhost:8000")
    print(client.create_item("football", 10))
    print(client.get_items())
    print(client.update_item(1, 100))
    print(client.get_items())

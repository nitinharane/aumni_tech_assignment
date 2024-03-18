import json
import time
from endpoints.SportsEquipmentClient import SportsEquipmentClient


def check_and_save_empty_items():
    try:
        client = SportsEquipmentClient("http://localhost:8000")
        data = client.get_items()
        empty_items_dict = {item["name"]: item["quantity"] for item in data if item["quantity"] == 0}
        with open(f"empty_items_{int(time.time())}.json", "w") as file:
            json.dump(empty_items_dict, file)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        check_and_save_empty_items()
        time.sleep(60)

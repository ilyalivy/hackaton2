import requests
import random

headers = {
    "Authorization": "Token 9c8b06d329136da358c2d00e76946b0111ce2c48",
    "Content-Type": "application/json"
}
def get_info_from_api(api_url):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        info = response.json()
        return info
    else:
        print("Error occurred while retrieving data from the API.")
        return None
random_number = random.randint(1,500)
data = get_info_from_api(f'https://food2fork.ca/api/recipe/get/?id={random_number}')

recipe= (data['title'], data['source_url'])
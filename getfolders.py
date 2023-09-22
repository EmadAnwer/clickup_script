import requests

space_id = "YOUR_space_id_PARAMETER"
url = "https://api.clickup.com/api/v2/space/" + space_id + "/folder"

query = {
    "archived": "false"
}

headers = {"Authorization": "YOUR_API_KEY"}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)

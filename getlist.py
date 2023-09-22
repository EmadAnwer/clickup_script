import requests

folder_id = "YOUR_folder_id_PARAMETER"
url = "https://api.clickup.com/api/v2/folder/" + folder_id + "/list"

query = {
  "archived": "false"
}

headers = {"Authorization": "YOUR_API_KEY"}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)

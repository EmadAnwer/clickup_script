import requests

team_id = "YOUR_team_id_PARAMETER"
url = "https://api.clickup.com/api/v2/team/" + team_id + "/space"

query = {
  "archived": "false"
}

headers = {"Authorization": "YOUR_API_KEY"}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)

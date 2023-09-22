import requests
import time
import datetime
# api config
list_id = "YOUR_list_id_PARAMETER"
url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"
query = {
    "team_id": "YOUR_team_id_PARAMETER"
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_KEY"
}
# stat date.utc this date is +1 day
start_date = datetime.datetime.strptime("9/23/23", "%m/%d/%y")
friday_in_milliseconds = int(round(start_date.timestamp() * 1000))
end_date = start_date
# team members ids
member_ids = [12, 13, 14, 15, 15]  # add your member ids here
# pairs of members to create tasks for
pairs_list = [(0, 1), (2, 3),  (1, 4), (2, 4),
              (0, 3),  (1, 2), (3, 4), (0, 2), (1, 3),
              (0, 4),]

for p in pairs_list:
    m1 = member_ids[p[0]]
    m2 = member_ids[p[1]]
    print(m1, m2)
    payload = {
        "name": "New Task from python script",
        "assignees": [
                m1, m2
        ],
        "due_date": friday_in_milliseconds,
        "start_date": friday_in_milliseconds,
        "notify_all": True,
    }
    response = requests.post(url, json=payload, headers=headers, params=query)
    data = response.json()
    print(data)
    end_date = end_date + datetime.timedelta(days=7)
    friday_in_milliseconds = int(round(end_date.timestamp() * 1000))

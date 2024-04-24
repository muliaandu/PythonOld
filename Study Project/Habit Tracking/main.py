import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "testingtoken"
USERNAME = "robinpixela"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# response.raise_for_status()
# print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now().strftime("%Y%m%d")

# graph_update = {
#     "date": today,
#     "quantity": "100",
# }

# response = requests.post(url=graph_update_endpoint, headers=headers, json=graph_update)
# response.raise_for_status()
# print(response.text)

graph_delete_bydate_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"
# response = requests.delete(url=graph_delete_bydate_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)

graph_update_bydate_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

graph_update = {
    "quantity": "1000"
}

response = requests.put(url=graph_update_bydate_endpoint, headers=headers, json=graph_update)
response.raise_for_status()
print(response.text)
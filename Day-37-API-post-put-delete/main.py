import requests
from datetime import datetime
from secret import secret

base_url = "https://pixe.la"

#! USER CREATION
# create_user_endpoint = "/v1/users"

# user_params = {
#     "token": secret.PIXELA_TOKEN,
#     "username": secret.username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=base_url+create_user_endpoint, json=user_params)
# print(response.text)

#!CREATE A GRAPH DEFINITION

# create_graph_endpoint = f"/v1/users/{secret.username}/graphs"

# headers = {
#     "X-USER-TOKEN": secret.PIXELA_TOKEN
# }

# graph_config = {
#     "id": "graph1",
#     "name": "Walking graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu"
# }

# response2 = requests.post(
#     url=base_url+create_graph_endpoint, json=graph_config, headers=headers)
# print(response2.text)


#!ADD PIXEL TO GRAPH
add_pixel_url = f"/v1/users/{secret.username}/graphs/graph1"

headers = {
    "X-USER-TOKEN": secret.PIXELA_TOKEN
}

today = datetime.now().strftime("%Y%m%d")
# print(today)
pixel_info = {
    "date": today,
    "quantity": "7.92",
}

# response3 = requests.post(
#     url=base_url+add_pixel_url, json=pixel_info, headers=headers)
# print(response3.text)


#! PUT AND DELETE REQUESTS

# PUT
modify_pixel_url = f"/v1/users/{secret.username}/graphs/graph1/{today}"

headers = {
    "X-USER-TOKEN": secret.PIXELA_TOKEN
}

pixel_update = {
    "quantity": "3.02",
}

response4 = requests.put(url=base_url+modify_pixel_url,
                         json=pixel_update, headers=headers)


# Delete

response5 = requests.delete(url=base_url+modify_pixel_url, headers=headers)

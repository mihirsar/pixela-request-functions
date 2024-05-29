import requests
from datetime import datetime

## Creation of user

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "mihirsar"
TOKEN = "ugr328t2bewuivbuvb"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
    }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


## Creation of graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
 
def create_graph():

    graph_config = {
    "id": GRAPH_ID,
    "name": "SuryaNamaskar",
    "unit": "reps",
    "type": "int",
    "color": "momiji", # momiji is red
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)


today = datetime.now() # todays date details
## posting a pixel
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
def post_pixel(reps):
    """posts pixel"""
    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": f"{reps}"
    }
    response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
    # print(response.text)

## modify pixel
def update_pixel(dateToModify, reps):
    """updates pixel takes input as yyyymmdd format"""
    update_pixel_endpoint = f"{pixel_post_endpoint}/{dateToModify}"
    updated_pixel_config = {
        "date": f"{dateToModify}",
        "quantity": f"{reps}"
    }
    response = requests.put(url=update_pixel_endpoint, json=updated_pixel_config, headers=headers)
    # print(response.text)

## delete pixel 
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
def delete_pixel(dateToDelete):
    del_pixel_endpoint = f"{pixel_post_endpoint}/{dateToDelete}"
    response = requests.delete(url=del_pixel_endpoint, headers=headers)


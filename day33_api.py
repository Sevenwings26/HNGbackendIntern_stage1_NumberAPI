# """
#     endponts:::
#     http://api.open-notify.org/iss-now.json
#     https://api.kanye.rest/
# """

import requests


# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # instead of writing the errors, use this...
# # httpstatuses.io  - to learn the types of http error responses...   
# response.raise_for_status()

# data = response.json()
# # print(data)

# # Note: Since it is json (dictionary), you can get the values by the key. 
# print(data["iss_position"]["latitude"])

# # task     
# # check the directory: "kanye-quotes-start"


# 4th February, 2025 
# Task: Detect sunny or sunset time in a particular location 
#Use -  https://sunrise-sunset.org/api

#   Location - IBADAN
Lat = 51.507351
Long =  -0.127758

parameters = {
    "lat": Lat,
    "lng": Long,
    "formatted":0,
}
response = requests.get(url="https://sunrise-sunset.org/api", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

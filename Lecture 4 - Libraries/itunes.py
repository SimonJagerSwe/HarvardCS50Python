########## ITUNES API ##########
# import json   # Only needed for the json.dumps function
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))  # Not pretty enough

object = response.json()
for result in object["results"]:
    print(result["trackName"])
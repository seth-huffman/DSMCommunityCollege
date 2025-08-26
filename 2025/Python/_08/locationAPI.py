import requests
from datetime import datetime

# Use the API documentation at this site to build your API request
link = requests.get("http://api.open-notify.org/iss-now.json")
link.raise_for_status()
data = link.json()

# Find out the current location of the ISS and print it to the console
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
print(f"Location: {latitude} + {longitude}" )

# Find out the names of the current residents of the ISS and print it to the consolE.
link2 = requests.get("http://api.open-notify.org/astros.json")
link2.raise_for_status()
data2 = link2.json()

# Your outputs should be formatted to answer the questions.  This needs to be beyond just printing the json to the console. Outputting only JSON code will result in no points.
residents = [p["name"] for p in data2["people"] if p["craft"] == "ISS"]

print(f"Current residents of the ISS:")
for name in residents:
    print(f"- {name}")






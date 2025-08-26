import requests

# Use either the API you researched, one your fellow students researched, or a completely different one
link = "https://api.nasa.gov/planetary/apod"

# Make an API call from within Python requesting data with specified parameters
parameters = { "api_key": "DEMO_KEY", "count": 1 }
request = requests.get(link, params=parameters)

# Output the downloaded data to the console
print(request.json())

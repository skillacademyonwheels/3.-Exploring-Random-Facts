import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

response = requests.get(url)


if response.status_code == 200:
  facts = response.json()
  print(facts["text"])
else:
  print("Unable to retrieve")


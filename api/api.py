import requests

r = requests.get("https://demo.api-platform.com/books")
print(r.text)
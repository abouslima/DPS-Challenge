import requests

headers = {"Content-Type": "application/json"}

response = requests.post("http://18.117.128.71:5000/api/predictions", headers=headers,
                         json={"year": "2021", "month": "6"})

print(response.text)

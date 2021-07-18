import requests

json_data = {"github": "https://github.com/DigitalProductschool/website", "email": "name@example.com",
             "url": "https://digitalproductschool.io/", "notes": "I deployed using ..."}

headers = {"Content-Type": "application/json", "Authorization": "Basic Key"}

# https://dps-challenge.netlify.app/.netlify/functions/api/challenge
response = requests.post("http://18.117.128.71:5000/api/predictions", headers=headers,
                         json=json_data)

print(response.text)

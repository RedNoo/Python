import argparse
import configparser
import requests
import json

endpoints =  configparser.ConfigParser()
endpoints.read("endpoints.ini", encoding="utf-8")

login_endpoint = endpoints.get("Auth", "login")
print(login_endpoint)

parser = argparse.ArgumentParser(description='Login info parser')
parser.add_argument('username')
parser.add_argument('password')
args = parser.parse_args()



data = {
  "usernameOrEmail": args.username,
  "password": args.password
}

response = requests.post(login_endpoint, json=data)
login_response = json.loads(( response.text))

user_info = login_response.get('userInfo')





print(user_info.get('id'))

import requests
from configparser import ConfigParser

def getArticles():
    # Initiating and reading config values
    print("Loading configuration from file...")
    try:
        config = ConfigParser()
        config.read("config.ini")

        CLIENT_ID = config.get("auth.info", "client_id")
        USERNAME = config.get("auth.info", "username")
        SECRET_KEY = config.get("auth.info", "secret_key")
        PASSWORD = config.get("auth.info", "password")
    except:
        print("ERROR")

    print("SUCCESS")


    

    #acquire request header
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD
    }
    headers = {"User-Agent": "MyApi/0.0.1"}

    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    TOKEN = res.json()["access_token"]

    headers["Authorization"] = f'bearer {TOKEN}'




    #acquire data
    res = requests.get("https://oauth.reddit.com/r/worldnews/top/?t=day", headers=headers)

    artciles = []
    for post in res.json()["data"]["children"]:
        artciles.append(post["data"]["title"].lower())

    return artciles

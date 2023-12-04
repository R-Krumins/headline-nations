import requests
from configparser import ConfigParser
import logging

def getArticles():
    global header
    if header is None:
        header = acquireHeader()
    
    try:
        logger.info("Requesting daily top posts from r/worldnews...")
        res = requests.get("https://oauth.reddit.com/r/worldnews/top/?t=day", headers=header)
        logger.info("SUCCESS")
    except:
        logger.exception("ERROR")

    articles = []
    for post in res.json()["data"]["children"]:
        articles.append(post["data"]["title"].lower())

    logging.debug(articles)

    return articles

def acquireHeader():
    logger.info("Building header.")
    #access token will be added to the headers and then functin will return it
    header = {"User-Agent": "MyApi/0.0.1"}
    
    # reading config
    try:
        logger.info("Reading config file...")

        config = ConfigParser()
        config.read("config.ini")

        CLIENT_ID = config.get("auth.info", "client_id")
        USERNAME = config.get("auth.info", "username")
        SECRET_KEY = config.get("auth.info", "secret_key")
        PASSWORD = config.get("auth.info", "password")

        logger.info("SUCCESS")
    except:
        logger.exception("ERROR")


    #acquire access token
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD
    }
    try:
        logger.info("Acquiring access token for reddit API...")
        res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=header)
        TOKEN = res.json()["access_token"]
        logger.info("SUCCESS")
    except:
        logger.exception("ERROR")

    #add access token to headers
    header["Authorization"] = f'bearer {TOKEN}'
    logger.info("Header built.")
    logger.debug(f'Header: {header}')

    return header
    


header = None
logger = logging.getLogger(__name__)
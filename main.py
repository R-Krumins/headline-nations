import logging
import logging.config
import yaml
from datetime import datetime

#setup logging
with open("log-config.yaml") as stream:
    logConfig = yaml.safe_load(stream)

logging.config.dictConfig(logConfig)
logger = logging.getLogger(__name__)

#imports modules that have logging
import reddit
import db



#start main sequence
logger.info("Iniating new sequence.")

countriesFile = open("countries.txt", "r")
countries = countriesFile.read().split("\n")

articles = reddit.getArticles()

#Getting todays date
dt = datetime.now()
today = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)


# #search articles for country names and populate db
# for article in articles:
#     for country in countries:
#         if country in article:
#             db.insertIntoMentions(today, country, article)






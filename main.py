import reddit
import db
from datetime import datetime



countriesFile = open("countries.txt", "r")
countries = countriesFile.read().split("\n")

articles = reddit.getArticles()

#Getting todays date
dt = datetime.now()
today = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)


#search articles for country names and populate db
for article in articles:
    for country in countries:
        if country in article:
            db.insertIntoMentions(today, country, article)






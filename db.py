import mysql.connector
from configparser import ConfigParser


def insertIntoMentions(datetime, country, article):
    query = "INSERT INTO mentions (date, country, article) VALUES (%s, %s, %s)"
    cursor.execute(query, (datetime, country, article))
    connection.commit()




#establish connection with DB
config = ConfigParser()
config.read("config.ini")

host = config.get("db", "host")
database = config.get("db", "database")
user = config.get("db", "user")
passwd = config.get("db", "passwd")

connection = mysql.connector.connect(host=host,database=database, user=user, passwd=passwd)
cursor = connection.cursor()

print(connection)

import os
import requests
import mysql.connector

from configparser import ConfigParser

print("Configuration file test")
# Testing if configuration file exists on disk in the current working directory
print("----------")
print("Checking if config file exists -->")
assert os.path.isfile("config.ini") == True
print("OK")
print("----------")

# Opening the configuration file
config = ConfigParser()
config.read('config.ini')

# Checking if all reddit related config options are present in the config file
print("Checking if config has NASA related options -->")
assert config.has_option('auth.info', 'client_id') == True
assert config.has_option('auth.info', 'secret_key') == True
assert config.has_option('auth.info', 'username') == True
assert config.has_option('auth.info', 'password') == True
print("OK")
print("----------")

# Checking if all MYSQL related config options are present in the config file
print("Checking if config has MYSQL related options -->")
assert config.has_option('db', 'host') == True
assert config.has_option('db', 'database') == True
assert config.has_option('db', 'user') == True
assert config.has_option('db', 'passwd') == True
print("OK")
print("----------")

# Checking if possible to connect to nasa with the existing config options
print("Checking if it is possible to connect to reddit API with the given config options -->")

header = {"User-Agent": "MyApi/0.0.1"}
CLIENT_ID = config.get("auth.info", "client_id")
USERNAME = config.get("auth.info", "username")
SECRET_KEY = config.get("auth.info", "secret_key")
PASSWORD = config.get("auth.info", "password")
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {"grant_type": "password","username": USERNAME,"password": PASSWORD}
res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=header)
TOKEN = res.json()["access_token"]
header["Authorization"] = f'bearer {TOKEN}'
r = requests.get("https://oauth.reddit.com/r/worldnews/top/?t=day", headers=header)
assert r.status_code == 200
print("OK")
print("----------")

# Checking if possible to connect to MySQL with the existing config options
print("Checking if it is possible to connect to MYSQL with the given config options -->")
mysql_config_mysql_host = config.get('db', 'host')
mysql_config_mysql_db = config.get('db', 'database')
mysql_config_mysql_user = config.get('db', 'user')
mysql_config_mysql_pass = config.get('db', 'passwd')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("----------")

# Checking if logging is setup correctly
print("Checking if log config file exists log-config.yaml -->")
assert os.path.isfile("log-config.yaml") == True
print("OK")
print("----------")

print("Checking if log destination directory exists -->")
assert os.path.isdir("logs") == True
print("OK")
print("----------")


#check if migration is setup
print("Checking if migration source directory exists -->")
assert os.path.isdir("migrations") == True
print("OK")
print("----------")

#all is okay
print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")
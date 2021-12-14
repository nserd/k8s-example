from os import environ 

POD_IP = environ.get('POD_IP')
LOG_LEVEL = environ.get('LOG_LEVEL')

DB_HOST = environ.get('DB_HOST')
DB_USER = environ.get('DB_USER')
DB_PASS = environ.get('DB_PASS')

API_KEY = environ.get('API_KEY')

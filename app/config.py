# flake8: noqa
from os import environ as env

DEBUG = True
SECRET_KEY = "FKO2-F0OJ-O]j4fgj"
SQLALCHEMY_DATABASE_URI = "postgres://zbpteqgeidivic:aaaf458bf0fb775f29b0c185294b86a1d469e59c4d33937d0c7363bc93e7eb7a@ec2-46-137-84-173.eu-west-1.compute.amazonaws.com:5432/dbpbc9up1bs3d2"
SQLALCHEMY_TRACK_MODIFICATIONS = True
RESTPLUS_MASK_SWAGGER = False
JWT_SECRET_KEY = "hn9grzAnEQBsEE9E"
LOG_TO_STDOUT = env.get('LOG_TO_STDOUT')

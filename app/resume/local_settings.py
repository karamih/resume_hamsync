from datetime import timedelta

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-7%et0jd4!+kg5(q+o(g+gl13*7q)#!*4t(-ox#v6++1+8pqf*g"

DEBUG = True

ALLOWED_HOSTS = []

NAME = 'resume'
USER = 'postgres'
PASS = 'apex'
HOST = 'localhost'
PORT = '5432'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

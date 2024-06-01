import environ
from typing import Any
from pathlib import Path


class MainEnv:

    DEBUG: bool
    SECRET_KEY: str
    DATABASE_URL: Any
    ALLOWED_HOSTS: list

    def __init__(self) -> None:
        self.__env = environ.Env(
            DEBUG=(bool, True),
            SECRET_KEY=(
                str, 'django-insecure-=!+2=2-^&gw71@%xfj&)%3&jn8b^u-t^8r-i^!y5rms7+tu50g'),
            DATABASE_URL=(str, 'sqlite:///db.sqlite3'),
            ALLOWED_HOSTS=(list, ['127.0.0.1', 'localhost'])
        )
        environ.Env.read_env()
        self.DEBUG = self.__env('DEBUG')
        self.SECRET_KEY = self.__env('SECRET_KEY')
        self.DATABASE_URL = self.__env.db()
        self.ALLOWED_HOSTS = self.__env.list('ALLOWED_HOSTS')

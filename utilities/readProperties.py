import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir + '\\configurations\\config.ini'))


class ReadConfig:
    @staticmethod
    def getapplicationurl():
        username = config.get('commonInfo', 'UrlWomen')
        return username
import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password
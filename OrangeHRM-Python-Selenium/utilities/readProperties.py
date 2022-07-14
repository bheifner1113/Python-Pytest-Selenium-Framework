import configparser

config=configparser.RawConfigParser()
config.read(".\\configFiles\\config.ini")
#config.read(".\\OrangeHRM-Python-Selenium\\configFiles\\config.ini")


class ReadConfig():
    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
    @staticmethod
    def getInvalidUsername():
        invalidUsername = config.get('common info', 'invalidUsername')
        return  invalidUsername
    @staticmethod
    def getInvalidPassword():
        invalidPassword = config.get('common info', 'invalidPassword')
        return  invalidPassword
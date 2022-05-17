import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail=config.get('common info', 'userEmail')
        return useremail

    @staticmethod
    def getPassword():
        pasword=config.get('common info', 'password')
        return pasword
import logging


# class Loggen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="D:\\My Files\\Class\\Notes\\Sagar Sir\\Selenium\\N_NopCommerceProject\\Logs\\AutomationLog.log",
#                             format="%(asctime)s %(levelname)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


class Loggen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger


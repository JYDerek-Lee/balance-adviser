import data.yahoo_finance as yf
import src.logger as logger


def make_instance():
    logger.write_info_log("Test Yahoo finance test")
    yfnce = yf.YahooFinance()


handler = logger.initLogging("Temp.log",
                             True)
make_instance()
logger.write_info_log("aaaaaaaa")
logger.releaseLogging(handler)

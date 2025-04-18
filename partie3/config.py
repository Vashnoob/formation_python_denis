import logging

#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#https://docs.python.org/3/library/logging.html#logrecord-attributes

FORMAT = "%(levelname)s LINE:%(lineno)d %(asctime)s %(message)s"

logging.basicConfig(filename='reports/systemereservation.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format=FORMAT)

flogger = logging.getLogger("FILE_LOGGER")
flogger.setLevel(logging.WARN)
file_handler = logging.FileHandler("reports/errors_warning.log")
file_handler.setFormatter(logging.Formatter(fmt=FORMAT))
flogger.addHandler(file_handler)

logger = logging.getLogger("BASE_LOGGER")
logger.setLevel(logging.DEBUG)
screen_handler = logging.StreamHandler()
screen_handler.setFormatter(logging.Formatter(fmt=FORMAT))
logger.addHandler(file_handler)

# logger<- N handler<- 1 formatter
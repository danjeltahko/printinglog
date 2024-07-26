from printinglog.printinglog import Logger

simple_logger = Logger(format="simple")
simple_logger.info("info log")
simple_logger.error("error log")
simple_logger.warning("warning log")
simple_logger.debug("debug log")

logging_logger = Logger(format="logging")
logging_logger.info("info log")
logging_logger.error("error log")
logging_logger.warning("warning log")
logging_logger.debug("debug log")

detailed_logger = Logger(format="detailed")
detailed_logger.info("info log")
detailed_logger.error("error log")
detailed_logger.warning("warning log")
detailed_logger.debug("debug log")

long_logger = Logger(format="long")
long_logger.info("info log")
long_logger.error("error log")
long_logger.warning("warning log")
long_logger.debug("debug log")

"""
python -m unittest discover tests
"""

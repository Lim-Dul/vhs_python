import logging, sys


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.debug("Debug Hello")
logging.info("Info Hello")

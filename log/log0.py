import logging

logging.basicConfig(level=logging.DEBUG, filename=r'./demo.log', filemode='a')

logger = logging.getLogger('applog')
print(logger.level)
print(logger)

logger.setLevel(logging.DEBUG)
print(logger.level)
print(logger)
print(type(logger))

print(logger.name)

logging.debug("qwe")

# consoleHandler = logging.StreamHandler()

# formatter = 

# logging.Formatter("%(asctime)s")

# consoleHandler.setFormatter(formatter)
import logging

#1.记录器
logger = logging.getLogger('dq.zz.applog')
logger.setLevel(logging.INFO)

#2.处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING)

#没有给handler指定日志级别，将使用logger的级别
fileHandler = logging.FileHandler(filename='appdemo.log')

#formatter模式
formatter = logging.Formatter()

#给处理器设置格式，可以给不同处理器设置不同格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

#给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#定义一个过滤器，参数是给一个定义的命名空间，如果logger是以dq.zz开头，就认为是正确的
flt = logging.Filter("dq.zz")

#关联过滤器
logger.addFilter(flt)

#打印日志代码
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")

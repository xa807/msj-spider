import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler


# 日志
logger = logging.getLogger('msj-spider')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt='[%(asctime)s %(name)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
io_handler = StreamHandler()
io_handler.setLevel(logging.DEBUG)
io_handler.setFormatter(formatter)

file_handler = TimedRotatingFileHandler('msj-spider.log',
                                        encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(io_handler)
logger.addHandler(file_handler)


# UA池
ua_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/74.0.3729.131 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 '
    'Safari/605.1.15',
]



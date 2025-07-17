import logging    

# в консоль
# logging.basicConfig(level=logging.DEBUG) 

# в файл
logging.basicConfig(level=logging.DEBUG, filename='my_log.log',
                format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('111')
logging.info('222')
logging.warning('333')
logging.error('444')
logging.critical('55')

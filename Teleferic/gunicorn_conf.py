# Gunicorn configuration file
import multiprocessing

bind = '0.0.0.0:8000'
multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
errorlog = '-'
accesslog = '-'
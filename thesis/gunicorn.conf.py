"""
Gunicorn settings and config file, reference:
https://docs.gunicorn.org/en/stable/settings.html
https://docs.gunicorn.org/en/stable/configure.html#configuration-file
"""

import multiprocessing

workers = multiprocessing.cpu_count()
bind = "0.0.0.0:8000"
loglevel = "info"

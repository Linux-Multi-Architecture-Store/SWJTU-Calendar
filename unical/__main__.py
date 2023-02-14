# Let's get this party started!
import logging
import os
from unical.main import Logger
from wsgiref.simple_server import make_server
from unical.srv import router
import falcon
import pathlib
import time
import snowflake.client

time_tuple = time.localtime(time.time())
log_name = "{}-{}-{}-{}-{}-{}.log".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5])
path = pathlib.Path.home()
path = os.path.join(path, ".config", "unical", "logs")
os.makedirs(path, exist_ok=True)
logger = Logger(os.path.join(path, log_name), logging.ERROR, logging.DEBUG)
print("Logs are save in {}".format(os.path.join(path, log_name)))

# 默认使用本地服务器
snowflake.client.setup("localhost", 8910)

# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()

router(app, logger)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        logger.war('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()

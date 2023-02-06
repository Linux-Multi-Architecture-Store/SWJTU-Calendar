# Let's get this party started!
from wsgiref.simple_server import make_server

from unical.srv import router

import falcon

# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()

router(app)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()

from unical.main.utils.web import get_cookie
import falcon
import json


class GetCookie(object):

    def __init__(self, logger=None):
        self.logger = logger

    def on_get(self, request, response):
        # print(request.params['name'])
        self.logger.war("This method is unsafe! May cause the leak of your password!")
        cookie = get_cookie(request.params['username'], request.params['password'])

        found_JSESSIONID = False
        for each in cookie:
            if each['name'] == 'JSESSIONID':
                found_JSESSIONID = True
                break
        if not found_JSESSIONID:
            response.status = falcon.HTTP_200
            response.text = "No JSESSIONID found!"
            return

        json_cookie = json.dumps(cookie[0])
        response.text = json_cookie
        response.status = falcon.HTTP_200

import falcon
import json
import asyncio
from unical.srv.Worker.RegisterWorker import RegistUser

class RegisterService(object):
    def __init__(self, logger):
        self.logger = logger

    def on_get(self, req, res):
        """Handles GET requests"""
        result = asyncio.run(RegistUser(req.params['username'], req.params['password'], self.logger))
        res.status = falcon.HTTP_200
        res.text = result
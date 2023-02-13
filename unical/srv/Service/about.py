import falcon
from unical.infos import APP_VERSION

class AboutService:
    def __init__(self, logger=None):
        self.logger = logger

    def on_get(self, request, response):
        """Handles GET requests"""
        response.status = falcon.HTTP_200  # This is the default status
        response.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        response.text = (
            f"""
            This is the University Calendar API.
            Version {APP_VERSION}
            
            Copyright (c) 2022 - Now Yinan Qin.
            """
        )

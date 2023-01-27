import falcon


class AboutService:
    def on_get(self, request, response):
        """Handles GET requests"""
        response.status = falcon.HTTP_200  # This is the default status
        response.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        response.text = (
            """
            This is the University Calendar API.
            Version 2.0.0-beta1
            
            Copyright (c) 2022 - Now Yinan Qin.
            """
        )

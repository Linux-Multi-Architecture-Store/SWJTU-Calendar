"""
All the router should be defined in this file.
"""
from unical.srv.Service import AboutService
from unical.srv.Service import GetCookie


def router(app, logger) -> None:
    """
    All the router should be defined in this file.
    :param logger:
    """
    app.add_route('/about', AboutService(logger))
    app.add_route('/api/get_cookie', GetCookie(logger))

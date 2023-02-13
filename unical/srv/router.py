"""
All the router should be defined in this file.
"""
from unical.srv.Service import AboutService


def router(app, logger) -> None:
    """
    All the router should be defined in this file.
    :param logger:
    """
    app.add_route('/about', AboutService(logger))

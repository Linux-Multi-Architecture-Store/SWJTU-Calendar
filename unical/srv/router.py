"""
All the router should be defined in this file.
"""
from unical.srv.Service import AboutService


def router(app) -> None:
    """
    All the router should be defined in this file.
    """
    app.add_route('/things', AboutService())

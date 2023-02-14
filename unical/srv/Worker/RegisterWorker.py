from unical.main.database import Database


async def RegistUser(username, password, logger):
    db = Database(logger=logger).initialize_database()
    
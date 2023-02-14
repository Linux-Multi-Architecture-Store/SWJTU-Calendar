from unical.main.database import Database
import snowflake.client


async def RegistUser(username, password, logger):
    db = Database(logger=logger)
    db.initialize_database()
    sql = f"""SELECT * FROM U_user_info WHERE name = '{username}';"""
    sql_result = db.query_database(sql)

    if len(sql_result) == 0:
        # 未注册，现在注册！
        uuid = snowflake.client.get_guid()
        sql = [f"""INSERT INTO U_user_info (uid, name, password) VALUES ('{uuid}', '{username}', '{password}');"""]
        db.insert_database(sql)

        return True
    elif len(sql_result) >= 1:
        return False
        
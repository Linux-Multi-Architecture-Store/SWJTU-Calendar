import logging
from sqlite3.dbapi2 import Connection
from ..utils.utils import VersionNumber
from unical.infos import DATA_COMPATIBILITY_VERSION


def init_table(conn: Connection):
    conn.execute("PRAGMA foreign_keys = false;")
    conn.execute("""
    CREATE TABLE IF NOT	EXISTS "U_system_info" (
      "name" TEXT,
      "value" TEXT
    );
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS "U_user_info" (
      "uid" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "name" TEXT,
      "password" TEXT
    );
    """)
    conn.execute("""UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'U_user_info';
""")

    # Store the data compability info
    # conn.execute("""INSERT INTO "main"."U_system_info"("name", "value") VALUES ('DATA_COMPATIBILITY_VERSION', '0.0.1-alpha1')""")
    temp = conn.execute("""SELECT * FROM U_system_info WHERE name = 'DATA_COMPATIBILITY_VERSION';""")
    temp = temp.fetchone()

    if temp is None:
        conn.execute(f"""INSERT INTO "main"."U_system_info"("name", "value") VALUES ('DATA_COMPATIBILITY_VERSION', '{DATA_COMPATIBILITY_VERSION.version}')""")
    else:
        db_version = VersionNumber(temp[1])
        version_to_install = DATA_COMPATIBILITY_VERSION

        if db_version.major_version != version_to_install.major_version:
            raise Exception(f"""The installed dataset is not of compatibility with the verion supported.
            Expect version {version_to_install.major_version}, but {db_version.major_version} detected.""")
        elif db_version <= version_to_install:
            conn.execute(f"""UPDATE U_system_info SET value = '{version_to_install.version}' WHERE name = 'DATA_COMPATIBILITY_VERSION'""")
        else:
            logging.warning(f"The installed version of dataset {db_version.version} is higher than the program version {version_to_install.version}")
            
    conn.execute("PRAGMA foreign_keys = true;")

    conn.commit()
    conn.close()

    return True

def execute_sqls(conn: Connection, sql: list = None):
    conn.execute("PRAGMA foreign_keys = false;")
    for each in sql:    
        conn.execute(each)
    conn.execute("PRAGMA foreign_keys = true;")
    conn.commit()
    conn.close()

    return True

def execute_query(conn: Connection, query):
    temp = conn.execute(query)
    return temp.fetchall()

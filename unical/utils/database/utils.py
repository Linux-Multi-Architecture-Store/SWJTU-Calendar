from sqlite3.dbapi2 import Connection


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
    conn.execute("""INSERT INTO "main"."U_system_info"("name", "value") VALUES ('DATA_COMPABILITY_VERSION', '0.0.1-alpha1')""")

    conn.execute("PRAGMA foreign_keys = true;")

    conn.commit()
    conn.close()

    return True

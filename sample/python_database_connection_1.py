import config
import MySQLdb
import MySQLdb.cursors as mc

import contextlib
DictCursor = mc.DictCursor
SSCursor = mc.SSCursor
SSDictCursor = mc.SSDictCursor
Cursor = mc.Cursor

@contextlib.contextmanager
def connection(cursorclass=Cursor,
               host=config.HOST, user=config.USER,
               passwd=config.PASS, dbname=config.MYDB,
               driver=MySQLdb):
    connection = driver.connect(
            host=host, user=user, passwd=passwd, db=dbname,
            cursorclass=cursorclass)
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()

@contextlib.contextmanager
def cursor(cursorclass=Cursor, host=config.HOST, user=config.USER,
           passwd=config.PASS, dbname=config.MYDB):
    with connection(cursorclass, host, user, passwd, dbname) as conn:
        cursor = conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()


with cursor(SSDictCursor) as cur:
    print(cur)
    connection_sql =cur.connection
    print(connection_sql)
    sql = 'select * from table'
    cur.execute(sql)
    for row in cur:
        print(row)

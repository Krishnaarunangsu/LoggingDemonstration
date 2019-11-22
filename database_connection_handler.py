import pymysql

class Database:
    def __init__(self, name):
        self._conn = pymysql.connect(**name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        """

        :rtype: object
        """
        count = self.cursor.execute(sql, params or ())
        print(f'Count:{count}')
        return self.fetchall(), count


db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 3306,                       # port
            'user':"root",                      # username
            'password':"abz00ba",                   # password
            'db':"arunangsukrishna",                        # database
            'charset':'utf8'                    # charset encoding
            }

sql = "SELECT * FROM tutorials_tbl"

with Database(db_config) as test:
    res, count = test.query(sql)
    print(res)
    print(res[0])
    print(len(res))
    print(f'Row Count:{count}')
    print(f'Element in a row:{len(res[0])}')
    print(res[0][0])
    print(res[0][1])
    print(res[0][2])
    print(res[0][3])
    for x in res[0]:
        print(x)


#  https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class/38078544

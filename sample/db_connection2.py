import pymysql
from contextlib import contextmanager


# Using ContextManager Design
@contextmanager
class DatabaseTest(object):
    def __init__(self, db_local):
        print(db_local)
        self.db_local = db_local
        self.db_conn = None
        self.db_cursor = None
        self.resultset = None
        print(self.db_local)

    def __enter__(self) -> object:
        # This ensure, whenever an object is created using "with"
        # this magic method is called, where you can create the connection.
        print('Comimg')
        self.db_conn = pymysql.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor()

    def __exit__(self, exception_type: object, exception_val: object, trace: object) -> object:
        """

        :rtype:
        """
        # once the with block is over, the __exit__ method would be called
        # with that, you close the connection
        try:
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully

    def get_row(self, sql: object, data: object = None) -> object:
        self.db_cursor.execute(sql)
        self.resultset = self.db_cursor.fetchall()
        return self.resultset

db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 3306,                       # port
            'user':"root",                      # username
            'password':"abz00ba",                   # password
            'db':"arunangsukrishna",                        # database
            'charset':'utf8'                    # charset encoding
            }


sql = "SELECT * FROM tutorials_tbl"

with DatabaseTest(db_config) as test:
    resultSet = test.get_row(sql)
    print(resultSet)

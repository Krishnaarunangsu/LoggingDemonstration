import pymysql


class Database:
    connection = None
    resultset = None

    def __init__(self, db_local, sql):
        print("Instantiating!")
        self.db_local = db_local
        self.sql = sql



    def __enter__(self) -> object:
        if self.connection is not None:
            return self.connection

        print(f'Comimg with db properties:{self.db_local} & \nsql:{self.sql}')
        self.connection = pymysql.connect(**self.db_local)
        print(self.connection)

        # If the connection is successful
        if self.connection is not None:
            self.db_cursor = self.connection.cursor()
            print(self.db_cursor.execute(sql))
            self.resultset = self.db_cursor.fetchall()
            print(self.resultset)
        return self.resultset
        #return self.db_cursor
        # return self.connection

    def __exit__(self, exception_type: object, exception_val: object, trace: object) -> object:
        """
        Once the with block is over, the __exit__ method would be called
        with that, you close the connection

        :rtype: object
        :param exception_type:
        :param exception_val:
        :param trace:
        :return:
        """
        try:
            print(f'In exit:{self.db_cursor}')
            print(f'In exit:{self.connection}')
            self.db_cursor.close()
            self.connection.close()

           # self.db_cursor.close()

        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully


db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 3306,                       # port
            'user':"root",                      # username
            'password':"abz00ba",                   # password
            'db':"arunangsukrishna",                        # database
            'charset':'utf8'                    # charset encoding
            }

sql = "SELECT * FROM tutorials_tbl"
test: object
with Database(db_config, sql) as test:
    print('Done!!!..')

import pymysql
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from typing import Dict, List, Any, Union, Hashable, Tuple
import yaml
import sample.db_configuration as db_conf



#  https://stackoverflow.com/questions/775296/mysql-parameterized-queries
#  https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/
#  https://repl.it/repls/OfficialBlueUmbrellabird
#  https://stackoverflow.com/questions/53185081/error-1210-incorrect-number-of-arguments-executing-prepared-statement
class DatabaseConnectionHelper(object):
    def __init__(self, db_local):
        """
        Initializes the class
        :param db_local:
        :return
        """
        self.db_local = db_local
        self.db_conn = pymysql.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor()
        # self.db_conn = mysql.connector.connect(**self.db_local)
        # self.db_cursor = self.db_conn.cursor(prepared=True)  # this will return MySQLCursorPrepared object
        self.resultset = None

    def __enter__(self):
        """
        This ensures, whenever an object is created using "with"
        this magic method is called, where you can create the connection.

        :return:
        """
        # self.db_conn = pymysql.connect(**self.db_local)
        # con = pyodbc.connect('DRIVER={SQL Server};SERVER=Prod1\SQL2008R2;DATABASE=SDE;UID=sa;PWD=sa')
        # self.db_cursor = self.db_conn.cursor()
        return self

    def __exit__(self, exception_type: object, exception_val: object, trace: object) -> object:
        """
        Once the with block is over, the __exit__ method would be called
        with that, you close the connection

        :rtype:
        :param exception_type:
        :param exception_val:
        :param trace:
        :return:
        """
        try:
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully

    def get_row(self, sql: object, data: object = None) -> object:
        print(sql)
        print(data)
       # c.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))
        # self.db_cursor.execute("SELECT TUTORIAL_TITLE FROM TUTORIALS_TBL WHERE TUTORIAL_AUTHOR= %s",(data))
        self.db_cursor.execute(sql,(data))
        self.resultset = self.db_cursor.fetchall()
        return self.resultset


# Load the Database Configuration parameters from the YAML Configuration file
config: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = yaml.load(open('../resources/config.yml'))
db_name: Union[List[Any], Any] = config['DB_NAME']
db_user_name = config['DB_USER']
db_user_password: Union[List[Any], Any] = config['DB_USER_PASSWORD']
db_url = config['DB_HOST']
db_port = config['DB_PORT']
db_charset = config['DB_CHARSET']


print('Database name: {}'.format(db_name))
print('Database user: {}'.format(db_user_name))
print('Database password: {}'.format(db_user_password))
print('Database url: {}'.format(db_url))

# Build the Database Configuration object to open a Database connection
db_config =  {
            'host': db_url,                 # database host
            'port': db_port,                       # port
            'user': db_user_name,                      # username
            'password': db_user_password,                   # password
            'db': db_name,                        # database
            'charset': db_charset                    # charset encoding
            }



# max = 50
# min = 10
name: str = "Sanjay"

# data: Tuple[int, int] = max, min
# data: Tuple[str]= name
data = (name)

# Pass the db_config in the Database Connection class
with DatabaseConnectionHelper(db_config) as test:
    print(test)
    resultSet = test.get_row(db_conf.prepared_statement,data)
    print(resultSet[0])

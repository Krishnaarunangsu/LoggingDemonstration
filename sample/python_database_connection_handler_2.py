import pymysql
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from typing import Dict, List, Any, Union, Hashable, Tuple
import yaml
import sample.db_configuration as db_conf




class DatabaseConnectionHelper(object):

    # Load the Database Configuration parameters from the YAML Configuration file
    config: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = yaml.load(open('../resources/config.yml'))

    db_name: Union[List[Any], Any] = config['DB_NAME']
    db_user_name = config['DB_USER']
    db_user_password: Union[List[Any], Any] = config['DB_USER_PASSWORD']
    db_url = config['DB_HOST']
    db_port = config['DB_PORT']
    db_charset = config['DB_CHARSET']


    # Build the Database Configuration object to open a Database connection
    db_config =  {
            'host': db_url,                 # database host
            'port': db_port,                       # port
            'user': db_user_name,                      # username
            'password': db_user_password,                   # password
            'db': db_name,                        # database
            'charset': db_charset                    # charset encoding
            }
    print('Database name: {}'.format(db_name))
    print('Database user: {}'.format(db_user_name))
    print('Database password: {}'.format(db_user_password))
    print('Database url: {}'.format(db_url))


    def __init__(self):
        """
        Initializes the class
        :param db_local:
        :return
        """
        # self.db_local = db_local
        print('In  __init__')
        self.db_conn = pymysql.connect(**self.db_config)
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
        print('In  __enter__')
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
        print('In  __exit__')
        try:
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully


def get_row(database_connection: DatabaseConnectionHelper, sql: object, data: object = None) -> object:
    """
    get the row data from the database
    :param database_connection:
    :param sql:
    :param data:
    :return:
    """
    print('In get_row')
    print(f'SQL:{sql}')
    print(f'DATA:{data}')
    print(f'OBJECT:{database_connection}')
    database_connection.db_cursor.execute(sql,(data))
    database_connection.resultset = database_connection.db_cursor.fetchall()
    return database_connection.resultset



name: str = "Sanjay"

data = (name)

# Pass the db_config in the Database Connection class
with DatabaseConnectionHelper() as test:
    print(test)
    database_connection = test.__enter__()
    print(f'Cursor:{database_connection.db_cursor}')
    print(f'Resultset:{database_connection.resultset}')
    # resultSet = get_row(database_connection, db_conf.prepared_statement,data)
    resultSet= get_row(database_connection, db_conf.prepared_statement,data)
    print(resultSet[0])

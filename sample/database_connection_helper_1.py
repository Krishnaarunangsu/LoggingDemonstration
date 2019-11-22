# This class Opens a Connection to the Database and closes it
import pymysql
from typing import Dict, List, Any, Union, Hashable
import yaml


def get_db_conn_properties(self):
    """

    :param self:
    :return:
    """

    # Load the Database Configuration parameters from the YAML Configuration file
    config: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = yaml.load(open('resources/config.yml'))
    db_name: Union[List[Any], Any] = config['DB_NAME']
    db_user_name = config['DB_USER']
    db_user_password: Union[List[Any], Any] = config['DB_USER_PASSWORD']
    db_url = config['DB_HOST']
    db_port = config['DB_PORT']
    db_charset = config['DB_CHARSET']

    # print the values
    print('Database name: {}'.format(db_name))
    print('Database user: {}'.format(db_user_name))
    print('Database password: {}'.format(db_user_password))
    print('Database url: {}'.format(db_url))

    return db_url, db_port, db_user_name, db_user_password, db_name, db_charset


#Class Definition
class DatabaseConnectionHelper:
    def __init__(self):
        """
        Initializes the class
        :return
        """
        self.db_conn = None
        self.db_cursor = None
        self.result_set = None

    # @property
    def __enter__(self) -> object:
        """
        This ensures, whenever an object is created using "with"
        this magic method is called, where you can create the connection.

        :return:
        """
        # db_url, db_port, db_user_name, db_user_password, db_name, db_charset = DatabaseConnectionHelper.get_db_conn_properties()
        db_url, db_port, db_user_name, db_user_password, db_name, db_charset = get_db_conn_properties()
        # Build the Database Configuration object to open a Database connection
        db_config: Dict[str, Union[List[Any], Any]] =  {
            'host': db_url,                 # database host
            'port': db_port,                # port
            'user': db_user_name,           # username
            'password': db_user_password,   # password
            'db': db_name,                  # database
            'charset': db_charset           # charset encoding
            }
        self.db_conn = pymysql.connect(db_config)
        # con = pyodbc.connect('DRIVER={SQL Server};SERVER=Prod1\SQL2008R2;DATABASE=SDE;UID=sa;PWD=sa')

        # If the connection is successful
        if self.db_conn is not None:
            self.db_cursor = self.db_conn.cursor()
        return self.db_cursor

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
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully

    def get_db_conn_properties(self):
        """

        :return:
        """
        config: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = yaml.load(open('resources/config.yml'))
        db_name: Union[List[Any], Any] = config['DB_NAME']
        db_user_name = config['DB_USER']
        db_user_password: Union[List[Any], Any] = config['DB_USER_PASSWORD']
        db_url = config['DB_HOST']
        db_port = config['DB_PORT']
        db_charset = config['DB_CHARSET']





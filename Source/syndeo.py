import pyodbc

class Driver():

    # == Attributes ===
    SQL_SERVER_ODBC_18 = "ODBC Driver 18 for SQL Server"
    SQL_SERVER_ODBC_17 = "ODBC Driver 17 for SQL Server"
    SQL_SERVER_ODBC_13_1 = "ODBC Driver 13.1 for SQL Server"
    SQL_SERVER_ODBC_13 = "ODBC Driver 13 for SQL Server"
    SQL_SERVER_ODBC_11 = "ODBC Driver 11 for SQL Server"
    MYSQL_ODBC_8_2 = "MySQL ODBC 8.2 Driver"
    MYSQL_ODBC_3_51 = "MySQL ODBC 3.51 Driver"

class Connetion():

    def __init__(self, driver : str, database : str, username=None, password=None, server="localhost", trust=False, timeout=10) -> None:

        # === Attributes ===
        self.__driver = driver
        self.__database = database
        self.__username = username
        self.__password = password
        self.__server = server
        self.__trust = "yes" if (trust) else "no"
        self.__timeout = timeout
        self.__connection = None
        self.__cursor = None

    # == MAIN methods ===

    def Open(self) -> None:
        """ Opens the connection with the database. """
        self.__connection = pyodbc.connect(driver=self.__driver, database=self.__database,
            UID=self.__username, PWD=self.__password, server=self.__server, trusted_connection=self.__trust, timeout=int(self.__timeout))

        if (self.__connection):
            self.__cursor = self.__connection.cursor()

    def Close(self) -> None:
        """ Closes the connection with the database. """
        if (self.__connection):
            self.__cursor = None
            self.__connection.close()
            self.__connection = None

    def Query(self, command : str) -> tuple:
        """ Gets data from the database as a tuple. """
        self.__cursor.execute(command)
        return self.__cursor.fetchall()

    def Script(self, command : str) -> None:
        """ Make changes in the database. """
        self.__cursor.execute(command)
        self.__cursor.commit()

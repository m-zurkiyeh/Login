import mariadb
from cryptography.fernet import Fernet


HOST = "localhost"
PORT = 3306
USER = "malik"
PASSWORD = "malik"
DATABASE = "mysql"


key = Fernet.generate_key()

fernet = Fernet(key)


conn_settings = {
    "host": HOST,
    "port": PORT,
    "user": USER,
    "password": PASSWORD,
    "database": DATABASE,
}
"""The dictionary used as a template to connect to the database"""


class db_manager:
    """
    The sole purpose of this class is to handle everything
    related databases as well as processing of parameters
    """

    def __init__(self):
        """sumary_line

        Keyword arguments:
        self -- class instancec
        Return: void
        """

        self.conn = mariadb.connect(**conn_settings)
        self.mycursor = self.conn.cursor()

    def add_to_table(self, email, fname, lname, passwd):
        """
        Displays a table containing all of the user created in the database in a JSON-esque fashion

        Params:
        self: the instance
        Returns:
            user_list: variable containing all of the users comprised in a single list
        """

        self.email = email
        self.fname = fname
        self.lname = lname
        self.passwd = fernet.encrypt(
            passwd.encode()
        )  # encrpts the password variable, turning into a long line of garbled text (Think mojibake minus the special characters and only in english letters)

        # Executes the query
        self.mycursor.execute(
            """INSERT INTO users (email,fname,lname,password)
                              VALUES (%s,%s,%s,%s)""",
            (self.email, self.fname, self.lname, self.passwd),
        )
        self.conn.commit()

    def show_table(self):
        """
        Displays a table containing all of the user created in the database in a JSON-esque fashion

        Params:
        self: the instance
        Returns:
            user_list: variable containing all of the users comprised in a single list
        """

        user_list = ()
        query = self.mycursor.execute("select id,email,fname,lname from users")
        user_list = list(user_list)
        for x in self.mycursor:
            user_list.append(x)
        for x in user_list:
            print(x)
        user_list = tuple(user_list)
        return user_list

    def get_user_by_id(self, user_id):
        """

        Returns the user based on the user_id provided
        Args:
            self (self): instance
            user_id (int): the user's id

        Returns:
            self.mycursor.fetchone(): the selected user obtained from the executed query

        """

        self.user_id = user_id
        self.mycursor.execute(
            "SELECT * FROM users WHERE id =%d", [self.user_id]
        )  # Gets all users using SELECT * query
        return self.mycursor.fetchone()

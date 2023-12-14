import mariadb
from cryptography.fernet import Fernet
import re


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


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
""" The variable used as a template for emails """


class db_manager:

    """
    The sole purpose of this class is to handle everything
    related databases as well as processing of parameters
    """

    def __init__(self):
        """
        Connects to the database and activates
        the cursor upon initializing an object of type db_manager

        Keyword arguments:
        self -- class' instance
        Return: void
        """

        try:
            self.conn = mariadb.connect(**conn_settings)
        except Exception:
            print("An error has occurred while attempting to connect to the database.\nPlease try again")
            exit()
        
        self.mycursor = self.conn.cursor()

    def add_to_table(self, email, fname, lname, passwd):
        """
        Displays a table containing all of the user created in
        the database in a JSON-esque fashion

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
        )  # encrpts the password variable, turning into a long line of garbled text (Think mojibake minus the special characters and only in english letters but it's really not)

        self.mycursor.execute(
            """SELECT EXISTS(SELECT * FROM users where email = %s and fname = %s and lname = %s)""",
            (self.email, self.fname, self.lname),
        )

        print(self.mycursor.fetchone()[0])

        # Executes the query
        self.mycursor.execute(
            """INSERT INTO users (email,fname,lname,password)
                              VALUES (%s,%s,%s,%s)""",
            (self.email, self.fname, self.lname, self.passwd),
        )
        self.conn.commit()

    def show_table(self):
        """

        Displays a table containing all of the user created in the database
        in a JSON-esque fashion

        Args:
            self (self): the class' instance

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
        )  # Gets all users using SELECT * query where id = the provided id
        return self.mycursor.fetchone()

    def check_email(self, email):
        """
        
        Checks the provided email if it matches according to the regex

        Args:
            self (self): the class' own instance
            email (str): the provided string value for the email

        Returns:
            re.fullmatch: The find result in boolean

        """

        self.email = str(email)
        return re.fullmatch(regex, self.email)

    def check_if_already_exists(self, email, fname, lname) -> bool:
        """

        Checks the table if the user with the information provided already exists

        Args:
            self (self): the class' own instance
            email (str): the provided string value for the email
            fname (str): the provided string value for the first name
            lname (str): the provided string value for the last name

        Returns:
            True if user already exists otherwise False

        """
        self.email = email
        self.fname = fname
        self.lname = lname

        # This specific query returns a tuple of str
        self.mycursor.execute("""SELECT EXISTS(SELECT * FROM users where email = %s and fname = %s and lname = %s)""",(self.email, self.fname, self.lname),)  

        does_exist = self.mycursor.fetchone()[0]  # Gets the first and only index of the tuple

        return True if does_exist == 1 else False  # Returns a bool value via a ternary operator

    def reset_id_increment(self):
        """
        Resets the id column of the table that has the AUTO_INCREMENT attribute attached to it

        Args:
            self (self): the class' own instance

        Returns:
            void
        """
        self.mycursor.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    def update_user():
        pass

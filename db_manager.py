import mariadb
from cryptography.fernet import Fernet
import re
import os


HOST = "localhost"
PORT = 3306
USER = "<user>"
PASSWORD = "<password>"
DATABASE = "user_db"


CONNECTION_SETTINGS = {
    "host": HOST,
    "port": PORT,
    "user": USER,
    "password": PASSWORD,
    "database": DATABASE,
}

key = Fernet.generate_key()

fernet = Fernet(key)

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

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
            self.conn = mariadb.connect(**CONNECTION_SETTINGS)
        except mariadb.Error as e:
            print("An error has occurred while connecting to the database.\nPlease check the inputted credentials and try again.")
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
        self.passwd = passwd

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

    def show_table(self) -> tuple:
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

    def get_full_name(self,email) -> tuple:
        
        """

        Returns the user's full name based on the email

        Args:
            self (self): the class' instance
            email:

        Returns:
            user_list: variable containing all of the users comprised in a single list

        """
        
        
        self.email = email
        self.mycursor.execute("""SELECT fname, lname FROM users WHERE email = %s""",(str(self.email),),)  
        return self.mycursor.fetchone()
    
        
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

    def check_email(self, email) -> bool:
        """
        
        Checks the provided email if it matches according to the regex

        Args:
            self (self): the class' own instance
            email (str): the provided string value for the email

        Returns:
            re.fullmatch: The find result in boolean

        """

        self.email = str(email)
        return bool(re.fullmatch(regex, self.email))

    def already_exists(self, email, fname, lname) -> bool:
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
        self.mycursor.execute("""SELECT EXISTS(SELECT * FROM users WHERE email = %s AND fname = %s AND lname = %s)""",(self.email, self.fname, self.lname),)  

        already_exists = self.mycursor.fetchone()[0]  # Gets the first and only index of the tuple

        return True if already_exists == 1 else False  # Returns a bool value via a ternary operator


    def check_email_exists(self,email) -> bool :
        
        self.email = email

        # This specific query returns a tuple of str
        self.mycursor.execute("""SELECT EXISTS(SELECT * FROM users WHERE email = %s)""",(self.email),)  

        already_exists = self.mycursor.fetchone()[0]  # Gets the first and only index of the tuple

        return True if already_exists == 1 else False  # Returns a bool value via a ternary operator


    def exists(self,email,passwd) -> bool:
        self.email = email
        self.passwd = passwd
        
        self.mycursor.execute("""SELECT EXISTS(SELECT * FROM users WHERE email = %s AND password = %s)""",(self.email, self.passwd),)
        
        return True if self.mycursor.fetchone()[0] == 1 else False
    

    def check_password_name(self,first_name,last_name,password) -> bool :
        """

        Args:
            self (self): the class' own instance
            password (str): the password str
        
        Returns:
            True if first name and/or last name is found in the password, otherwise return false
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        no_name_in_passwd = first_name.casefold() in password.casefold() or last_name.casefold() in password.casefold()

        return True if no_name_in_passwd else False
    
    def check_password_uppercase(self,password) -> bool:
        """
        Checks if the password has at least one uppercase character

        Args:
            self: the class's instance
            password (str): the password str
        
        Returns:
            bool: True if an uppercase letter exists in the password 
        """

        self.password = password

        return bool(re.search(r'[A-Z]',password))
    
    def check_password_number(self,password) -> bool:
        """
        Checks if the password has at least one number

        Args:
            self: the class' instance
            password (str) : the password str

        Returns:
            bool: True if a number exists in the password
        """

        self.password = password

        return bool(re.search(r'\d',password))

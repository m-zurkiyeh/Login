import mariadb
from cryptography.fernet import Fernet


HOST = "localhost"
PORT = 3306
USER = "malik"
PASSWORD = "malik"
DATABASE = "mysql"


key = Fernet.generate_key()

fernet = Fernet(key)




#The dictionary used as a template to connect to the database
conn_settings = {
     "host":HOST,
     "port":PORT,
     "user":USER,
     "password":PASSWORD,
     "database":DATABASE
}

class db_manager:
    """The sole purpose of this class is to handle everything related databases"""
    
    def __init__(self):
        """sumary_line
        
        Keyword arguments:
        self -- class instancec
        Return: void
        """
        
        self.conn = mariadb.connect(**conn_settings)
        self.mycursor = self.conn.cursor()
    
    def add_to_table(self,email,name,user_id):
        """sumary_line
        
        Keyword arguments:
        self -- description
        Return: return_description
        """
        
        self.email=email
        self.name=name
        self.user_id=int(user_id)
        params = (self.user_id,self.name,self.email)

        self.mycursor.execute("""INSERT INTO users (id,NAME,email)
                              VALUES (%d,%s,%s)""",params)
        self.conn.commit()
        pass
    
    def show_table(self):
        user_list = ()
        query = self.mycursor.execute("SELECT * FROM users")
        user_list = list(user_list) 
        for x in self.mycursor: user_list.append(x)
        for x in user_list : print(x)
        user_list = tuple(user_list)
        return user_list
    
    def get_user_by_id(self,user_id):
        """
        

        Args:
            self (self): instance
            user_id (int): the user's id

        Returns:
            _type_: self.mycursor.fetchone()
        """
        self.user_id = user_id
        self.mycursor.execute("SELECT * FROM users WHERE id =%d",[self.user_id])
        return self.mycursor.fetchone()
        

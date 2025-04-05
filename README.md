![Static Badge](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Static Badge](https://img.shields.io/badge/MySQL-15.1-blue?logo=mysql)
![Static Badge](https://img.shields.io/badge/Flask-3.0.0-blue?logo=flask)
![Static Badge](https://img.shields.io/badge/HTML-grey?logo=html5)
![Static Badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript)
![Static Badge](https://img.shields.io/badge/CSS-grey?logo=css3)
![Static Badge](https://img.shields.io/badge/Jinja-grey?logo=jinja)
![Static Badge](https://img.shields.io/badge/MariaDB-grey?logo=mariadb)

A RESTful API simulating a Login Page written in Python using the Flask Framework to handle HTML routing, in addition to storing user information using a MariaDB database

# About
<div align="center">
    <img src="static/imgs/signup.png">
</div>


## Requirements
1. Python 
2. MariaDB Connector for Python 
    - A C compiler, preferably GCC
    - OpenSSl 


## Installation
[Windows](#Windows) (Coming Soon)  
[Linux](#Linux)



## Windows (WIP)

>[!IMPORTANT]
> Instructions for windows installation are incomplete at the moment, more instructions will be coming soon

1. Install MariaDB using [this link](https://mariadb.com/downloads/community/), make sure to select MS Windows (64-bit) as the OS if you are using Windows

2. To specifically use MariaDB in the terminal and not mysql, copy the paths to MariaDB Connector C 64-bit\lib\ and lib\plugin and MariaDB 'version number'\bin and add them to the Path system environment variable. They should look like this:

<div align="center">
<img src= static/imgs/paths.png>
</div>

</br>





## Linux

1. Grant the setup.sh file execute permission by entering:
```console
$ chmod +x setup.sh
```

Then run the script as root **(Not optional)**

```console
sudo ./setup.sh
```




**Keep in mind that the location of the specified paths will vary depending on where they are installed**

5. Create the database and table using the provided .sql file, 
``` console
$ mysql -u root -p < users.sql
```

6. Create a user with all privileges, by entering the following commands:
``` sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```

**'username' and 'password' can be of your choosing**


7. Exit MariaDB and sign in to the database with the new credentials
``` console
$ sudo mysql -u username -p -h localhost user_db
```
----

### How to Run

First, go to the db_manager.py file and change these 2 constants to your recently created credentials:
```python
USER = "<user>"
PASSWORD = "<password>"
```

Then simply run this command:
``` console
$ python3 main.py
```
The app will be running at the address: http://127.0.0.1:5000/


### Accessing the database
To display the users:
``` sql
select email,fname,lname from users;
```

### References

[^1]: [Install Python](https://www.python.org/downloads/)

[^2]: [Installing Python for WSL](https://wiki.usask.ca/display/MESH/Installing+Python+and+the+Windows+Subsystem+for+Linux)

[^3]: [Install MariaDB Connector/Python](https://mariadb.com/docs/server/connect/programming-languages/python/install/)


>[!WARNING]
> It is best to use dummy information as the user input will be stored in the local database. 


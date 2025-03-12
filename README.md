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


## Prerequisites
1. Python **(3.11 ) HIGHLY RECOMMENDED**
2. MariaDB Connector for Python 
    - A C compiler, preferably GCC
    - OpenSSl 
3. Windows Subsystem for Linux


## Installation
**Please note that this RESTful with the Prerequisites installed in WSL. The installation methods for Windows or Powershell may vary**


1. Update the package index using this command:

``` console
$ sudo apt update && upgrade
```

2. Run the following Commands:
``` console
sudo apt install gcc
sudo apt install openssl
sudo apt install python3-dev
```
These will install the necessary packages for MariaDB to work


3. Install MariaDB using [this link](https://mariadb.com/downloads/community/), make sure to select MS Windows (64-bit) as the OS if you are using Windows

4. To specifically use MariaDB in the terminal and not mysql, copy the paths to MariaDB Connector C 64-bit\lib\ and lib\plugin and MariaDB 'version number'\bin and add them to the Path system environment variable. They should look like this:

<div align="center">
<img src= static/imgs/paths.png>
</div>

</br>

**Keep in mind that the location of the specified paths will vary depending on where they are installed**

5. Create the database and table using the provided .sql file, 
``` console
$ mysql -u root -p < users.sql
```

6. Create a user, by entering the following commands:
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

Simply run:
``` console
$ python3 main.py
```
The app will be running at the address: http://127.0.0.1:5000/


### Accessing the database
To display the users:
``` sql
select email,fname,lname from users;
```
**You can include id and password but the id auto increments everytime a user is created and the passwords are encrypted and will be shown as a series of characters**

### TODO:
- [ ] Implement admin authentications (Not Essential)


### References

[^1]: [Install Python](https://www.python.org/downloads/)

[^2]: [Installing Python for WSL](https://wiki.usask.ca/display/MESH/Installing+Python+and+the+Windows+Subsystem+for+Linux)

[^3]: [Install MariaDB Connector/Python](https://mariadb.com/docs/server/connect/programming-languages/python/install/)


**VERY IMPORTANT: Although it will be on your own server and not published online and the user can be easily deleted, it is advisable not to enter your actual personal information, to test the login api, use dummy information**


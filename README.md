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

1. Install Python using [this link](https://www.python.org/downloads/). [^1] 

2. Update the package index using this command:

``` console
$ sudo apt update && upgrade
```

3. Install Python to the WSL terminal by entering the command: [^2]
``` console
$ sudo apt install python3 python3-pip
``` 


4. Install a C compiler as it is essential for the connector to work, for instructions purposes, install GCC via the command: [^3]

``` console
$ sudo apt install gcc
```

5. The second requirement is a TLS library such as OpenSSL. To install it, enter the command: [^3]

``` console
$ sudo apt install openssl
```

6. The python development files is the third and last requirement for the the MariaDB Connector/Python. Install it using this command: [^3]

``` console
$ sudo apt install python3-dev
```

7. Install MariaDB using [this link](https://mariadb.com/downloads/community/), make sure to select MS Windows (64-bit) as the OS if you are using Windows

8. To specifically use MariaDB in the terminal and not mysql, copy the paths to MariaDB Connector C 64-bit\lib\ and lib\plugin and MariaDB 'version number'\bin and add them to the Path system environment variable. They should look like this:

<div align="center">
<img src= static/imgs/paths.png>
</div>

</br>

**Keep in mind that the location of the specified paths will vary depending on where they are installed**

9. Start MariaDB by entering 
``` console
$ sudo mysql
```

10. Create a user, by entering the following commands:
``` sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
```

**For purposes of the project, create a user named 'user' with the password 'user'**

11. Create a database by entering the command:
``` sql
CREATE DATABASE db;
```
**For purposes of the project, create a database named 'mysql'**

12. Create the users table using the command:
``` sql
create table users (id int NOT NULL AUTO_INCREMENT, email varchar(255), fname varchar(255), lname varchar(255), password varchar(255), PRIMARY KEY(id));
```

13. Sign in to mariadb with the created user and the created database
``` console
$ sudo mysql -u user -p -h localhost mysql
```
----

### How to Run

Simply run:
``` console
$ python3 main.py
```
Then go to the link http://127.0.0.1:5000/signup


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


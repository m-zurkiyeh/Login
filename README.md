![Static Badge](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Static Badge](https://img.shields.io/badge/MySQL-15.1-blue?logo=mysql)
![Static Badge](https://img.shields.io/badge/Flask-3.0.0-blue?logo=flask)
![Static Badge](https://img.shields.io/badge/HTML-grey?logo=html5)
![Static Badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript)
![Static Badge](https://img.shields.io/badge/CSS-grey?logo=css3)
![Static Badge](https://img.shields.io/badge/Jinja-grey?logo=jinja)
![Static Badge](https://img.shields.io/badge/MariaDB-grey?logo=mariadb)


<div align="center">
    <img src="static/imgs/signup.png">
</div>

## Table of Contents
- [About](#About)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [How To Run](#How-To-Run)

## About
A RESTful API simulating a Login Page written in Python using the Flask Framework to handle HTML routing, in addition to storing user information using a MariaDB database


## Requirements
1. Python 
2. MariaDB
    - C Connector ([Windows](https://mariadb.com/downloads/connectors/connectors-data-access/c-connector/))
    - Python Connector([Windows and Linux](https://mariadb.com/docs/server/connect/programming-languages/python/install/#Install_from_PyPI))
3. Chocolatey (Windows)
4. A [user](#User) created in SQL (**RECOMMENDED**)


## Installation
[Windows](#Windows) <br>
[Linux](#Linux) <br>
[Docker](#Docker)



### Windows (Chocolatey)

>[!IMPORTANT]
> Instructions for windows installation are incomplete at the moment, more instructions will be coming soon

1. Install MariaDB using [this link](https://mariadb.com/downloads/community/), make sure to select MS Windows (64-bit) as the OS if you are using Windows

2. Install the necessary packages using the command:
``` choco install packages.config ``` 


3. To specifically use MariaDB in the terminal and not mysql, copy the paths to MariaDB Connector C 64-bit\lib\ and lib\plugin and MariaDB 'version number'\bin and add them to the Path system environment variable. They should look like this:

<div align="center">
<img src= static/imgs/paths.png>
</div>

</br>





### Linux

>[!NOTE]
>Make sure you are in a venv before proceeding further 


1. Grant the setup.sh file execute permission by entering:
```console
$ chmod +x setup.sh
```

2. Run the script as root **(Not Optional)**

```console
sudo ./setup.sh
```

**Keep in mind that the location of the specified paths will vary depending on where they are installed**

3. Create the database and table using the provided .sql file, 
``` console
$ mysql -u root -p < users.sql
```
<br>

## How-to-Run

### Before running the program


### User (Non Docker)

1. Login to MariaDB as root using the command:
```
mysql -u root -p
```

2. Create a user with access to the user database, by entering the following commands:
``` sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON user_db.* TO 'username'@'localhost';
```

**'username' and 'password' can be of your choosing**

----



Create a .env file in the same directory as the other files with the following populated environment variables
```python
DB_PORT = 3306
DB_NAME= "user_db"
DB_USERNAME
DB_PASSWORD
ROOT_PASSWORD # (Not necessarily needed, unless you plan on running the application in Docker)
```

### Linux

Run this command:

```console
$ python3 app.py
```

>[!NOTE]
> While a flask secret key is mentioned in the coded, a flask secret key will be generated and added as a variable in env called FLASK_SECRET_KEY for the program to use at runtime




### Docker

1. Build the image using this command:
```console
docker-compose up --build -d
```
**2 containers, login-db-1 and login-app-1 will be created by default**

2. Check if the containers are successfully running using:
```console
docker ps -a
```

3. View the application output using:
```console
docker logs login-app-1
```

The app will be running at the address: http://127.0.0.1:5000/





### Accessing the database

#### Docker
1. Enter the database container through this command:
```console
docker exec -it login-db-1 bash
```

2. Login to the database with the user and password info located in your .env file:
```console
mariadb -u <env username> -p <env password>
```
<br>

#### Windows and Linux

To display the users:
``` sql
select email,fname,lname from users;
```

<br>

**To Terminate the application, CTRL+C for Windows and Linux, and "docker compose down " for docker**

### References

[^1]: [Install Python](https://www.python.org/downloads/)

[^2]: [Installing Python for WSL](https://wiki.usask.ca/display/MESH/Installing+Python+and+the+Windows+Subsystem+for+Linux)

[^3]: [Install MariaDB Connector/Python](https://mariadb.com/docs/server/connect/programming-languages/python/install/)


>[!WARNING]
> It is best to use dummy information as the user input will be stored in the local database. 


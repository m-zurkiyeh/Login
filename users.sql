CREATE DATABASE IF NOT EXISTS user_db;
use user_db

CREATE TABLE IF NOT EXISTS users (
  id int NOT NULL AUTO_INCREMENT,
  email varchar(255),
  fname varchar(255),
  lname varchar(255),
  password varchar(255),
  PRIMARY KEY(id)
);
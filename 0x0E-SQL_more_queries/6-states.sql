-- creates database hbtn_0d_usa and table states with auto-gen primary key id INT and name VARCHAR(256) NOT NULL
-- DROP DATABASE IF EXISTS <database>;
DROP DATABASE IF EXISTS hbtn_0d_usa;
-- CREATE DATABASE <database>;
CREATE DATABASE hbtn_0d_usa;
-- USE <database>;
USE hbtn_0d_usa;
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS states;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE states (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);

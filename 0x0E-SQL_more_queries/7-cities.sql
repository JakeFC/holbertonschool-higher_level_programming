-- creates database hbtn_0d_usa and table cities with auto-gen primary key id INT, name VARCHAR(256) that can't be null,
-- and state_id INT that can't be null and must be a foreign key reference to id of states table
-- CREATE DATABASE IF NOT EXISTS <database>;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- USE <database>;
USE hbtn_0d_usa;
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS cities;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE cities (id INT PRIMARY KEY AUTO_INCREMENT, state_id INT,
name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));

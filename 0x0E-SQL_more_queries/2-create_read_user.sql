-- creates database hbtn_0d_2 and user user_0d_2 with select privileges in db and password user_0d_2_pwd
-- DROP USER IF EXISTS <'username'@'hostname'>;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
-- CREATE USER <'username'@'hostname'> IDENTIFIED BY <'password'>;
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- CREATE DATABASE IF NOT EXISTS <database_name>;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- GRANT SELECT ON <database.table> TO <accountname>;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

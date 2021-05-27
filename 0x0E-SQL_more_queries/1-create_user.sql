-- creates the MySQL server user user_0d_1 with all privileges and password user_0d_1_pwd
--  DROP USER IF EXISTS <'username'@'hostname'>;
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- CREATE USER <'username'@'hostname'> IDENTIFIED BY <'password'>;
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- GRANT ALL ON <privilege_level> TO <account_name>;
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';

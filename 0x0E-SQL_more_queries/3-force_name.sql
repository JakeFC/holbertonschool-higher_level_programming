-- creates a table force_name with id and a name that can't be null
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS force_name;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE force_name (id INT, name VARCHAR(256) NOT NULL);

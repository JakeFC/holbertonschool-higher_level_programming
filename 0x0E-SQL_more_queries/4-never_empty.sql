-- creates a table id_not_null with id default value 1 and name
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS id_not_null;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE id_not_null (id INT DEFAULT 1, name VARCHAR(256));

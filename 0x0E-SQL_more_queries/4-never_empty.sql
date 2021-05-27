-- creates a table id_not_null with id that can't be null and name
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS id_not_null;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE id_not_null (id INT NOT NULL, name VARCHAR(256));

-- creates a table unique_id with unique id default value 1 and name
-- DROP TABLE IF EXISTS <table>;
DROP TABLE IF EXISTS unique_id;
-- CREATE TABLE <table> (VALUES);
CREATE TABLE unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));

-- lists all cities in hbtn_0d_usa as id, name, state.name sorted by cities.id
-- SELECT <values>
SELECT cities.id, cities.name, states.name
-- FROM <table> LEFT JOIN <table>
FROM cities INNER JOIN states
-- ON <condition>
ON cities.state_id = states.id
-- ORDER BY <value>
ORDER BY cities.id;

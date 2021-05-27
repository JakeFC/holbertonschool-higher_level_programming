-- lists all cities of California in hbtn_0d_usa
-- SELECT <value>[, <value>]
SELECT id, name
-- FROM <table>
FROM cities
-- WHERE <value> =
WHERE state_id =
  -- (SELECT <value>
  (SELECT id
  -- FROM <table>
  FROM states
  -- WHERE <condition>)
  WHERE name = 'California')

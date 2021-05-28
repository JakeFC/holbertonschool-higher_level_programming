-- lists all genres not linked to Dexter
-- SELECT <value>
SELECT name
-- FROM <table> INNER JOIN <table>
FROM tv_genres
-- WHERE <condition>
WHERE name NOT IN
-- (SELECT <value>
(SELECT name
-- FROM <table> INNER JOIN <table>
FROM tv_shows s INNER JOIN tv_show_genres gs
-- ON <condition>
ON s.id = gs.show_id
-- INNER JOIN <table>
INNER JOIN tv_genres g
-- ON <condition>
ON gs.genre_id = g.id
-- WHERE <condition>
WHERE s.title = 'Dexter')
-- ORDER BY <value>
ORDER BY name;

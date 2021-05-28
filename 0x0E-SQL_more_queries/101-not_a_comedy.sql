-- lists all non-Comedy shows
-- SELECT <value>
SELECT title
-- FROM <table>
FROM tv_shows
-- WHERE <conditions>
WHERE title NOT IN
-- SELECT <value>
(SELECT title
-- FROM <table> INNER JOIN <table>
FROM tv_shows s INNER JOIN tv_show_genres gs
-- ON <condition>
ON s.id = gs.show_id
-- INNER JOIN <table>
INNER JOIN tv_genres g
-- ON <condition>
ON gs.genre_id = g.id
-- WHERE <condition>
WHERE g.name = 'Comedy')
-- ORDER BY <value>
ORDER BY title;

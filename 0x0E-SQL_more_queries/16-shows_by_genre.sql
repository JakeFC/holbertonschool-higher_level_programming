-- lists all shows and all genres linked to them
-- SELECT <value>
SELECT title, name
-- FROM <table> INNER JOIN <table>
FROM tv_shows s LEFT JOIN tv_show_genres gs
-- ON <condition>
ON s.id = gs.show_id
-- INNER JOIN <table>
LEFT JOIN tv_genres g
-- ON <condition>
ON gs.genre_id = g.id
-- ORDER BY <value>
ORDER BY title, name;

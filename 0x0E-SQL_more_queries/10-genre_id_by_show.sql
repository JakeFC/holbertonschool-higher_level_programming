-- lists all shows with at least 1 genre linked
-- SELECT <values>
SELECT title, genre_id
-- FROM <table> JOIN <table>
FROM tv_shows s INNER JOIN tv_show_genres g
-- ON <condition>
ON s.id = g.show_id
-- ORDER BY <values>
ORDER BY s.title, g.genre_id

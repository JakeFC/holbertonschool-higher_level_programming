-- lists all shows as (and ordered by) title, genre_id
-- SELECT <values>
SELECT title, genre_id
-- FROM <table> LEFT JOIN <table
FROM tv_shows s LEFT JOIN tv_show_genres g
-- ON <condition>
ON s.id = g.show_id
-- ORDER BY <values>
ORDER BY s.title, g.genre_id

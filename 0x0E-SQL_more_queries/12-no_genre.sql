-- lists all shows as (and ordered by) title, genre_id that have no genre_id
-- SELECT <values>
SELECT title, genre_id
-- FROM <table> LEFT JOIN <table
FROM tv_shows s LEFT JOIN tv_show_genres g
-- ON <condition>
ON s.id = g.show_id
-- WHERE <condition>
WHERE g.genre_id IS NULL
-- ORDER BY <values>
ORDER BY s.title, g.genre_id;

-- lists all genres and number of linked shows each, as long as there is at least 1, by descending number
-- SELECT <values> AS <alias>
SELECT name AS genre, COUNT(*) AS number_of_shows
-- FROM <table> INNER JOIN <table>
FROM tv_genres g INNER JOIN tv_show_genres sg
-- ON <condition>
ON sg.genre_id = g.id
-- GROUP BY <value>
GROUP BY genre
-- ORDER BY <value>
ORDER BY number_of_shows DESC;

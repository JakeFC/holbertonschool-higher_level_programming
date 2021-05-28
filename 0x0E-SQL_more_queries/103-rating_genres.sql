-- lists all genres by rating
-- SELECT <value>, <value> AS <alias>
SELECT name, SUM(rate) AS rating
-- FROM <table> INNER JOIN <table>
FROM tv_genres g INNER JOIN tv_show_genres sg
-- ON <condition>
ON g.id = sg.genre_id
-- INNER JOIN <table>
INNER JOIN tv_show_ratings r
-- ON <condition>
ON sg.show_id = r.show_id
-- GROUP BY <value>
GROUP BY name
-- ORDER BY <value> DESC
ORDER BY rating DESC;

-- lists all shows by rating
-- SELECT <value>, <value> AS <alias>
SELECT title, SUM(rate) AS rating
-- FROM <table> INNER JOIN <table>
FROM tv_shows s INNER JOIN tv_show_ratings r
-- ON <condition>
ON s.id = r.show_id
-- GROUP BY <value>
GROUP BY title
-- ORDER BY <value> DESC
ORDER BY rating DESC;

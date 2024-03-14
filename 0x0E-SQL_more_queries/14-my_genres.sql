-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- 
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
	AND tv_shows.title = "Dexter"
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.name;

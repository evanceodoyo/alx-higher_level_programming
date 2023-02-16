-- lists all records where name is not null and orders the results
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

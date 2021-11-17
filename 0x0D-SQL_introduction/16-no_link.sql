-- list all of the second_table
-- Dont list rows without name value
SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL
ORDER BY score DESC;

-- create a user with all privileges
-- @localhost
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';

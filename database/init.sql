CREATE DATABASE IF NOT EXISTS linktree_db;
USE linktree_db;

CREATE TABLE IF NOT EXISTS user_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    facebook_user VARCHAR(100),
    instagram_user VARCHAR(100),
    x_user VARCHAR(100),
    linkedin_user VARCHAR(100),
    github_user VARCHAR(100),
    blog VARCHAR(255),
    author VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Poblar datos iniciales
INSERT INTO user_info (name, lastname, facebook_user, instagram_user, x_user, linkedin_user, github_user, blog, author) 
VALUES ('Frida', 'Kahlo', 'fridaKahlo10', 'fridaKahlo10', 'kahloFrida', 'fridaKahlo10', 'kahloFridaGit', 'https://fridakahlo.com', 'Frida Kahlo');

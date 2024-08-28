CREATE DATABASE IF NOT EXISTS console_notes;
use console_notes;

CREATE TABLE users(
    id  int(255) auto_increment not null,
    name    varchar(100),
    surname varchar(255),
    email   varchar(255) not null,
    password    varchar(255) not null,
    dates    date not null
CONSTRAINT pk_users PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notes(
    id int(255) auto_increment not null,
    user_id int(100) not null,
    title varchar(255) not null,
    description  MEDIUMTEXT,
    creationDate date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_user_note FOREIGN KEY(user_id) REFERENCES users(id)
) ENGINE=InnoDb;
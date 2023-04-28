CREATE USER manager WITH PASSWORD 'manager';

CREATE DATABASE data;
ALTER DATABASE data OWNER TO manager;
GRANT ALL PRIVILEGES ON DATABASE data TO manager;

\c data;

CREATE TABLE registros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL
);

ALTER TABLE registros OWNER TO manager;
GRANT ALL PRIVILEGES ON TABLE registros TO manager;

INSERT INTO registros (nome, idade) VALUES ('João', 20);
INSERT INTO registros (nome, idade) VALUES ('Maria', 30);
INSERT INTO registros (nome, idade) VALUES ('José', 40);
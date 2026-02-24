BEGIN TRANSACTION;
CREATE TABLE Category (
    idCategory SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE City (
    cityName VARCHAR(255) PRIMARY KEY,
    region VARCHAR(255) NOT NULL
);

CREATE TABLE ExportType (
    idExportType SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
COMMIT;

INSERT INTO exporttype (name) 
factoryeconsumer-# VALUES ('JsonExporter'), ('CsvExporter');
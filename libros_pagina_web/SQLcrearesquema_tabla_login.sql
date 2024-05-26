USE [SampleDB]
GO
CREATE SCHEMA pruebas_arduino
GO
CREATE TABLE pruebas_arduino.test
    (fecha DATETIME PRIMARY KEY,
    ubicacion VARCHAR(10),
    temperatura FLOAT,
    humedad FLOAT,
    )
CREATE LOGIN sensor1
WITH PASSWORD = 'sultan.2022'

CREATE LOGIN sensor2
WITH PASSWORD = 'abcd.123'

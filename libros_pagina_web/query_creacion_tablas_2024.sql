USE BD_PLANTAS_2024
GO
CREATE TABLE [Planta] (
  id_planta int IDENTITY(1,1) PRIMARY KEY,
  nombre_cientifico varchar(255) NOT NULL,
  nombre_comun varchar(255) NOT NULL,
  otros_nombres varchar(255),
  descripcion varchar (255),
);
CREATE TABLE [Enfermedad] (
  id_enfermedad int IDENTITY(1,1) PRIMARY KEY,
  nombre varchar(255) NOT NULL,
  descripcion_enf varchar(255),
  sintomas varchar (255)

);
CREATE TABLE [usos] (
  id_uso int IDENTITY(1,1) PRIMARY KEY,
  id_planta int NOT NULL,
  id_enfermedad int NOT NULL,
  descripcion_uso varchar(255),
  beneficio VARCHAR(255),
  FOREIGN KEY (id_planta) REFERENCES Planta(id_planta) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_enfermedad) REFERENCES Enfermedad(id_enfermedad) ON DELETE CASCADE ON UPDATE CASCADE,
);

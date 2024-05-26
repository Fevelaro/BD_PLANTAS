CREATE TABLE [Flower] (
  [Flower ID] int,
  [Flower size] int,
  [Flower colour] varchar(15),
  [Flower shape] varchar(20),
  [Uso ID FL] int,
  PRIMARY KEY ([Flower ID])
);
CREATE TABLE [Leaf] (
  [Leaf ID] int,
  [Leaf size] int,
  [Leaf colour] varchar(15),
  [Laef shape] varchar(20),
  [Uso ID LE] int,
  PRIMARY KEY ([Leaf ID])
);
CREATE TABLE [Fruit] (
  [Fruit ID] int,
  [Fruit size] int,
  [Fruit colour] varchar(15),
  [Fruit shape] varchar(20),
  [Uso ID FR] int,
  PRIMARY KEY ([Fruit ID])
);
CREATE TABLE [Stem] (
  [Stem ID] int,
  [Stem size] int,
  [Stem colour] varchar(15),
  [Stem shape] varchar(20),
  [Uso ID ST] int,
  PRIMARY KEY ([Stem ID])
);

CREATE TABLE [Loc] (
  [Loc ID] int,
  [Zone] varchar(20),
  [Forest] varchar(20),
  PRIMARY KEY ([Loc ID])
);

CREATE TABLE [Plant] (
  [Plant ID] int,
  [N_cient] varchar(30),
  [N_com1] varchar(15),
  [N_com2] varchar(15),
  [N_com3] varchar(15),
  [Otro] varchar(50),
  [Loc ID PL] int,
  [Stem ID PL] int,
  [Leaf ID PL] int,
  [Fruit ID PL] int,
  [Flower ID PL] int,
  [Uso ID PL] int,
  PRIMARY KEY ([Plant ID])
);

CREATE TABLE [Uso Medicinal] (
  [Uso ID] int,
  [Síntoma] varchar,
  [Enfermedad] varchar,
  [Recipe] varchar,
  [Stem ID UM] int,
  [Leaf ID UM] int,
  [Fruit ID UM] int,
  [Flower ID UM] int,
  PRIMARY KEY ([Uso ID])
);
--Foraneas de tabla Plant
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Loc_id FOREIGN KEY ([Loc ID PL])
      REFERENCES dbo.Loc ([Loc ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Stem_id FOREIGN KEY ([Stem ID PL])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Leaf_id FOREIGN KEY ([Leaf ID PL])
      REFERENCES dbo.Leaf ([Leaf ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Fruit_id FOREIGN KEY ([Fruit ID PL])
      REFERENCES dbo.Fruit ([Fruit ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Flower_id FOREIGN KEY ([Flower ID PL])
      REFERENCES dbo.Flower ([Flower ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
ALTER TABLE dbo.Plant
   ADD CONSTRAINT FK_Uso_id FOREIGN KEY ([Uso ID PL])
      REFERENCES dbo.[Uso Medicinal] ([Uso ID])
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
-- Foráneas tabla Uso Medicinal
ALTER TABLE dbo.[Uso Medicinal]
   ADD CONSTRAINT FK_Leaf_UM FOREIGN KEY ([Leaf ID UM])
      REFERENCES dbo.Leaf ([Leaf ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.[Uso Medicinal]
   ADD CONSTRAINT FK_Fruit_UM FOREIGN KEY ([Fruit ID UM])
      REFERENCES dbo.Fruit ([Fruit ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.[Uso Medicinal]
   ADD CONSTRAINT FK_Flower_UM FOREIGN KEY ([Flower ID UM])
      REFERENCES dbo.Flower ([Flower ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.[Uso Medicinal]
   ADD CONSTRAINT FK_Stem_UM FOREIGN KEY ([Stem ID UM])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
--Foráneas de partes de planta
ALTER TABLE dbo.Stem
   ADD CONSTRAINT FK_Uso_ST FOREIGN KEY ([Uso ID ST])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.Leaf
   ADD CONSTRAINT FK_Uso_LE FOREIGN KEY ([Uso ID LE])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.Flower
   ADD CONSTRAINT FK_Uso_FL FOREIGN KEY ([Uso ID FL])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
ALTER TABLE dbo.Fruit
   ADD CONSTRAINT FK_Uso_FR FOREIGN KEY ([Uso ID FR])
      REFERENCES dbo.Stem ([Stem ID])
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
;
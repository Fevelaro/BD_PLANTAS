ALTER TABLE dbo.[Flower]
   ADD CONSTRAINT FK_Uso_id_FL FOREIGN KEY ([Uso ID])
      REFERENCES dbo.[Uso Medicinal] ([Uso ID])
;
ALTER TABLE dbo.[Fruit]
   ADD CONSTRAINT FK_Uso_id_FR FOREIGN KEY ([Uso ID])
      REFERENCES dbo.[Uso Medicinal] ([Uso ID])
;
ALTER TABLE dbo.[Stem]
   ADD CONSTRAINT FK_Uso_id_ST FOREIGN KEY ([Uso ID])
      REFERENCES dbo.[Uso Medicinal] ([Uso ID])
;
ALTER TABLE dbo.[Leaf]
   ADD CONSTRAINT FK_Uso_id_LE FOREIGN KEY ([Uso ID])
      REFERENCES dbo.[Uso Medicinal] ([Uso ID])
;
-- Drop a table called 'dbo.Flower' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[dbo.Flower]', 'U') IS NOT NULL
DROP TABLE [dbo].[dbo.Flower]
GO
INSERT INTO dbo.Flower([Flower ID],[Flower size],[Flower colour],[Flower shape]) VALUES(100,30,'r','o')
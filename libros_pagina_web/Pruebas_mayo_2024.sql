use BD_2024_21mayo
--GO
--SELECT * FROM production.brands
SELECT
    customer_id,
    first_name,
    email,
    phone,
    state
FROM
    [sales].[customers]
WHERE state= 'NY' 
OR state = 'TX'

ORDER BY first_name ASC
    
GO
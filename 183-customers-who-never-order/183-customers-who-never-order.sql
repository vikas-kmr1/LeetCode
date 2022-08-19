# Write your MySQL query statement below
SELECT CUSTOMERS.NAME AS CUSTOMERS
    FROM CUSTOMERS
        WHERE CUSTOMERS.ID 
            NOT IN 
                (
                    SELECT ORDERS.CUSTOMERID 
                    FROM ORDERS
                )
            




# # Write your MySQL query statement below

SELECT 
    C.NAME AS CUSTOMERS
FROM 
    CUSTOMERS C LEFT JOIN ORDERS O
ON
    C.ID = O.CUSTOMERID
WHERE O.CUSTOMERID IS NULL;
            



# SELECT 
#     C.NAME AS CUSTOMERS
# FROM
#     CUSTOMERS C
# WHERE
#     C.ID NOT IN
#          ( SELECT 
#                 O.CUSTOMERID
#             FROM
#                 ORDERS O
#          );
    




# SELECT CUSTOMERS.NAME AS CUSTOMERS
#     FROM CUSTOMERS
#         WHERE CUSTOMERS.ID 
#             NOT IN 
#                 (
#                     SELECT ORDERS.CUSTOMERID 
#                     FROM ORDERS
#                 )
            




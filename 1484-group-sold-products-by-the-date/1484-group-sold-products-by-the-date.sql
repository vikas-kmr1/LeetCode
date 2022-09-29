# Write your MySQL query statement below
SELECT
    A.SELL_DATE, COUNT( 
                        DISTINCT(A.PRODUCT)
                      ) AS NUM_SOLD,
                 
                 GROUP_CONCAT(
                                DISTINCT(A.PRODUCT)
                             ) AS PRODUCTS
                
FROM 
    ACTIVITIES A
GROUP BY 
    A.SELL_DATE
ORDER BY
    A.SELL_DATE;
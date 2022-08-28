# Write your MySQL query statement below
SELECT s.product_id, product_name
FROM Sales s
LEFT JOIN Product p USING(product_id)
GROUP BY 1
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'


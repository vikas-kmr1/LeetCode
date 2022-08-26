SELECT
    customer_number
FROM
    orders
GROUP BY 
    customer_number
ORDER BY
    COUNT(customer_number) DESC
LIMIT 1;



# select
#     customer_number
# from
#     orders 
# group by 
#     customer_number
# having 
#     count(customer_number) >= all 
#     (select
#         count(customer_number) 
#      from 
#         orders 
#      group by 
#         customer_number);
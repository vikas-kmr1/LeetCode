select
    customer_number
from
    orders 
group by 
    customer_number
having 
    count(customer_number) >= all 
    (select
        count(customer_number) 
     from 
        orders 
     group by 
        customer_number);
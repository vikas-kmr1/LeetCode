# Write your MySQL query statement below
select 
    user_id as buyer_id , join_date, COALESCE(count(o.order_id),0) as orders_in_2019 
from 
    users u
left outer join
    Orders o on u.user_id = o.buyer_id AND order_date like '2019%'
group by u.user_id;
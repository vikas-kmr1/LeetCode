# Write your MySQL query statement below
select
    U.name, sum(T.amount) as balance
from 
    Users U
Left join
    Transactions T
on
    U.account = T.account
group by 
    U.account
having 
    balance >= 10000;

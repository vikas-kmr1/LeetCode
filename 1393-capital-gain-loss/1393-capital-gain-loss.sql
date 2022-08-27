# Write your MySQL query statement below
select stock_name, 
	sum(case 
		when operation = 'Buy' then -price 
		else price 
		end) as capital_gain_loss 
from Stocks 
	group by stock_name
    

# select stock_name, 
# 	(select sum(price) 
# 		from stocks 
# 		where operation='Sell'
# 			and stock_name=S1.stock_name ) -
# 	(select sum(price) 
# 		from stocks 
# 		where operation='Buy'
# 			and stock_name=S1.stock_name) as capital_gain_loss 
# 	from stocks S1
# 	group by stock_name
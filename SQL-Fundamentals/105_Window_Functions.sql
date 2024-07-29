------------------------
-- Window Functions
------------------------

-- Window Function

select
  *,
  sum(sales_cost) over (partition by transaction_id) as transaction_total_sales,
  sales_cost / sum(sales_cost) over (partition by transaction_id) as transaction_sales_percent
  
from
  grocery_db.transactions;
  
-- Row Number and Rank


select
  *,
  row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number
  
from
  grocery_db.transactions;
  
  
-- NTILE - for deciles/percentiles etc

select
  customer_id,
  customer_loyalty_score,
  ntile(3) over(order by customer_loyalty_score desc) as loyalty_category,
  ntile(10) over(order by customer_loyalty_score desc) as loyalty_category2
  
from
  grocery_db.loyalty_scores;
  
-- Quiz

/*

You have been tasked with ranking customers in terms of their distance from the store.

We only want to rank customers who have a distance_from_store value present in the data, and for those who have a gender value of 'M' or 'F'

The criteria for the ranking are:

Ranking will be in ascending order (i.e. rank 1 would be for the customer who is closest to the store)
Rankings will be split (hint: partitioned) by gender
In the case of tied rankings, we want the subsequent ranking to represent the number of rows seen rather than purely the next number (i.e. 1,1,1,4 rather than 1,1,1,2)


Your query will return four columns:

customer_id
gender
distance_from_store
distance_from_store_rank (you will create this)

*/

select
  customer_id,
  gender,
  distance_from_store,
  rank() over (partition by gender order by distance_from_store) as distance_from_store_rank
  
from
  grocery_db.customer_details
  
where
  distance_from_store is not null and 
  gender in ('M', 'F');





























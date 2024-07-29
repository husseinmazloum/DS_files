-----------------------------
-- SQL Test 1
----------------------------

-------------------------------------------------------------
-- 1) How many rows are there in the transactions table?
-------------------------------------------------------------

select
  count(*)
  
from
  grocery_db.transactions;
  
-- Answer = 38506

--------------------------------------------------------------------------------
-- 2) Return the customer_id for the customer who lives farthest from the store
--------------------------------------------------------------------------------

select
  customer_id,
  distance_from_store
  
from
  grocery_db.customer_details
  
where
  distance_from_store = (select max(distance_from_store) from grocery_db.customer_details);
  
-- Answer = 400.97

--------------------------------------------------------------------------------
-- 3) Return the number of unique customers in the customer_details table, split by gender
--------------------------------------------------------------------------------

select
  gender,
  count(distinct customer_id) as customer_count
  
from
  grocery_db.customer_details
  
group by
  gender;
  
-- Answer: M = 380 F = 485

-----------------------------------------------------------------------------------------------------------------------------------
-- 4) What were the total sales for each product area name for July 2020. Return these in the order of highest sales to lowest sales
------------------------------------------------------------------------------------------------------------------------------------

select
  b.product_area_name,
  sum(a.sales_cost) as total_sales
  
from
  grocery_db.transactions a
  inner join grocery_db.product_areas b on a.product_area_id = b.product_area_id
  
where
  a.transaction_date between '07-01-2020' and '07-31-2020'
  
group by
  b.product_area_name
  
order by
  total_sales desc;
  

-----------------------------------------------------------------------------------------------------------------------------------------------------------
-- 5) Return a list of all customer_id's that do NOT have a loyalty score (i.e. they are in the customer_details table, but not in the loyalty_scores table)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

select
  a.customer_id,
  b.customer_id,
  customer_loyalty_score
  
from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  
where
  b.customer_loyalty_score is null
  
order by
  a.customer_id;






























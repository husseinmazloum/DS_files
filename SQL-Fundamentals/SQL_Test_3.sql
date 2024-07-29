-----------------------------
-- SQL Test 3
----------------------------

--------------------------------------------------------------------------------------------------------------------------
-- 1) Return a list of customers from the loyalty_scores table who have a customer_loyalty_score of 0.77, 0.88, or 0.99
--------------------------------------------------------------------------------------------------------------------------

select
  *
  
from
  grocery_db.loyalty_scores
  
where
  customer_loyalty_score = 0.77 or
  customer_loyalty_score = 0.88 or
  customer_loyalty_score = 0.99
  
order by
  customer_id;



--------------------------------------------------------------------------------
-- 2) Return the average customer_loyalty_score for customers, split by gender
--------------------------------------------------------------------------------

select
  a.gender,
  avg(b.customer_loyalty_score) as avg_customer_loyalty
  
from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  
group by
  a.gender
  
order by
  a.gender;



----------------------------------------------------------------------------------------------------------------------------------------------------------------
-- 3) Return customer_id, distance_from_store, and a new column called distance_category that tags customers who 
-- are less than 1 mile from store as "Walking Distance", 1 mile or more from store as "Driving Distance" and "Unknown" 
-- for customers where we do not know their distance from the store
----------------------------------------------------------------------------------------------------------------------------------------------------------------


select
  customer_id,
  distance_from_store,
  case 
    when distance_from_store < 1 then 'Walking Distance'
    when distance_from_store >= 1 then 'Driving Distance'
    else 'Unknown' end as distance_category
  
from
  grocery_db.customer_details
  
order by
  customer_id;






-------------------------------------------------------------------------------------------------------------------------------------------------------
-- 4) For the 400 customers with a customer_loyalty_score, divide them up into 10 deciles, and calculate the average distance_from_store for each decile
-------------------------------------------------------------------------------------------------------------------------------------------------------
create temp table n_tile_table as (
select
  a.customer_id,
  a.distance_from_store,
  b.customer_loyalty_score,
  ntile(10) over (order by b.customer_loyalty_score) as loyalty_category
  
from
  grocery_db.customer_details a
  inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  
order by
  customer_loyalty_score
  
);

--------------------------------------------------------------------------------------------


select
  loyalty_category,
  avg(distance_from_store) as avg_distance
  
from 
  n_tile_table

group by
  loyalty_category
  
order by
  loyalty_category;

  

-----------------------------------------------------------------------------------------------------------------------------------------------------------
-- 5) Return data showing, for each product_area_name - the total sales, and the percentage of overall sales that each product area makes up
-----------------------------------------------------------------------------------------------------------------------------------------------------------

create temp table product_id_total_sales as (
select
  product_area_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  product_area_id
  
);

------------------------------------------------------------------------------------------------------

select
  a.product_area_name,
  b.total_sales,
  b.total_sales / sum(b.total_sales) over () as percentage
  
from
  grocery_db.product_areas a
  inner join product_id_total_sales b on a.product_area_id = b.product_area_id
  
group by
  a.product_area_name,
  b.total_sales;






















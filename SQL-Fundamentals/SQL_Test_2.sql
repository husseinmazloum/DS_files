-----------------------------
-- SQL Test 2
----------------------------

-------------------------------------------------------------
-- 1)How many unique transactions are there in the transactions table?
-------------------------------------------------------------

select
  count(distinct transaction_id) as transaction_count
  
from
  grocery_db.transactions;


-- Answer = 18160





--------------------------------------------------------------------------------
-- 2) How many customers were in each mailer_type category for the delivery club campaign
--------------------------------------------------------------------------------

select
  mailer_type,
  count(distinct customer_id) as customer_count
  
from
  grocery_db.campaign_data
  
where
  campaign_name = 'delivery_club'
  
group by
  mailer_type;





--------------------------------------------------------------------------------
-- 3) Return a list of customers who spent more than $500 and had 5 or more unique transactions in the month of August 2020
--------------------------------------------------------------------------------

select
  customer_id,
  sum(sales_cost) as total_sales,
  count(distinct (transaction_id)) as trans_count
  
from
  grocery_db.transactions
  
where
  transaction_date between '08-01-2020' and '08-31-2020'
  
group by
  customer_id
  
having
  sum(sales_cost) > 500 and count(distinct (transaction_id)) >= 5;
  

------------------------------------------------------

  

-----------------------------------------------------------------------------------------------------------------------------------
-- 4) Return a list of duplicate credit scores that exist in the customer_details table
------------------------------------------------------------------------------------------------------------------------------------

create temp table credit_score_count_table as (
select
  credit_score,
  count(customer_id) as credit_score_count
  
from
  grocery_db.customer_details
  
group by
  credit_score
  
order by
  credit_score
);
--------------------------------------------------------

select
  *
  
from
  credit_score_count_table;

--------------------------------------------------------

select
  credit_score,
  credit_score_count
  
from
  credit_score_count_table
  
where
  credit_score_count > 1
  
order by
  credit_score;
  
---------------------------------------------------

select
  credit_score,
  count(customer_id) as credit_score_count
  
from
  grocery_db.customer_details
  
group by
  credit_score
  
having
  count(customer_id) > 1
  
order by
  credit_score;

-----------------------------------------------------------------------------------------------------------------------------------------------------------
-- 5) Return the customer_id(s) for the customer(s) who has/have the 2nd highest credit score. Make sure your code would work for the 
-- Nth highest creditscore as well
-----------------------------------------------------------------------------------------------------------------------------------------------------------

create temp table credit_score_rank_table as (
select
  customer_id,
  credit_score,
  dense_rank() over (order by credit_score desc) as credit_score_rank

from
  grocery_db.customer_details
  
where
  credit_score is not null
  
);

------------------------------------------------------------------

select
  *
  
from 
  credit_score_rank_table
  
where
  credit_score_rank = 2;



------------------------------------------------------------------


select
  customer_id,
  credit_score,
  rank() over (order by credit_score desc) as credit_score_rank

from
  grocery_db.customer_details
  
where
  credit_score is not null
  
having
  rank() over (order by credit_score desc) = 2;














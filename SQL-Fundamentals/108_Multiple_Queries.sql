---------------------------------------------------------
-- Temp Tables & CTE For Multiple Queries
---------------------------------------------------------

select * from grocery_db.transactions where customer_id = 1;


-- Temporary Tables

create temp table cust_transactions as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_id


);

select * from cust_transactions;


select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from
  cust_transactions
  
group by
  customer_id;

-- Common Table Expression (CTE)


with cust_transactions_cte as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_id


)


select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from
  cust_transactions_cte
  
group by
  customer_id;


/*

A stakeholder is investigating the idea of incentivizing customers who have spent a lot in a single transaction.

For this, they will need data showing each customer's largest transaction in terms of dollars spent.

As our transaction data is at product_id level, to get this data, we will need to aggregate twice, once to the transaction_id level, and then again to find out 
the maximum amount spent per transaction, per customer.

Use either temporary tables or CTE to get this information.

Your query should return one row per customer, showing their maximum transaction spend. To make it easy for the stakeholder, please make sure the output is 
sorted by customer_id.

Your output will have two columns:

customer_id
max_transaction_sales (you will create this)


Hint: If you work this correctly, customer 1 should have a max_transaction_sales value of 555.26

*/

select * from grocery_db.transactions where customer_id = 1;

create temp table cust_transactions as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_id
);

select
  customer_id,
  max(total_sales) as max_transaction_sales
  
from
  cust_transactions
  
group by
  customer_id
  
order by
  customer_id;

select * from cust_transactions;












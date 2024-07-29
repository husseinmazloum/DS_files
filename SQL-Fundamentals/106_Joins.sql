--------------------------------------
-- Joining Tables
--------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.loyalty_scores;


-- Inner Join

select 
  a.*,
  b.customer_loyalty_score
  
from
  grocery_db.customer_details a
  inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;


-- Left Join

select 
  a.*,
  b.customer_loyalty_score
  
from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;


-- Adding Other Logic

select 
  a.*,
  b.customer_loyalty_score
  
from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  
where
  customer_loyalty_score > 0.5;


-- Joining Multiple Tables

select 
  a.*,
  b.customer_loyalty_score,
  c.product_area_name
  
from
  grocery_db.transactions a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  inner join grocery_db.product_areas c on a.product_area_id = c.product_area_id;
  
-- Other Join Types

create temp table table1 (
                       id char(1),
                       t1_col1 int,
                       t1_col2 int);
                       
insert into table1 values ('A',1,1), ('B',1,1);

select * from table1;


create temp table table2 (
                       id char(1),
                       t2_col1 int,
                       t2_col2 int);
                       
insert into table2 values ('A',2,2), ('C',2,2);

select * from table2;




-- Inner Join

select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  inner join table2 b on a.id = b.id;
  
-- Left Join


select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  left join table2 b on a.id = b.id;

-- Outer Join

select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  full outer join table2 b on a.id = b.id;

-- Cross Join


select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  cross join table2 b;

-- Quiz

/*

A stakeholder wants to analyze the relationship between credit score and customer loyalty - so we need to provide them with this data.

Extract a list of customers, along with their credit score, and their customer loyalty score.

Important: The stakeholder only wants to analyze customers that do have a customer loyalty score present in our data)

Your query will return three columns:

customer_id
credit_score
customer_loyalty_score

*/

select
  a.customer_id,
  a.credit_score,
  b.customer_loyalty_score

from
  grocery_db.customer_details a
  inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;




















--------------------------------------------------------------------------
-- PART 2: APPLYING SELECTION CONDITIONS USING THE WHERE STATEMENT
--------------------------------------------------------------------------

-- THE WHERE STATEMENT

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2;
  
-- MULTIPLE CONDITIONS

-- and

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 and
  gender = 'M';

-- or

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 or
  gender = 'M';
  
-- OTHER OPERATIONS

/*
Equal to =
Not Equal to <>
Greater than/Less than/Equal < > <=
*/

-- in

select
  *
  
from
  grocery_db.campaign_data
  
where
  mailer_type in ('Mailer1', 'Mailer2');
  
-- like

select
  *
  
from
  grocery_db.campaign_data
  
where
  mailer_type like '%Mailer%';
  
-- QUIZ

-- You've been tasked with returning a list of customers who meet the following criteria:

-- Live less than or equal to 0.5 miles from the store
-- Have a value of 'M' or 'F' listed for their gender


-- Your query needs to return:

-- customer_id
-- distance_from_store
-- gender

select
  customer_id,
  distance_from_store,
  gender
   
from
  grocery_db.customer_details
  
where
  distance_from_store <= 0.5 and
  gender in ('M', 'F');






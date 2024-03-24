# Write your MySQL query statement below


with minYear as (
    select product_id, min(year) as year from Sales group by product_id
)

select s.product_id, m.year as first_year, quantity, price 
from Minyear as m, Sales as s
where m.product_id=s.product_id and m.year=s.year
    
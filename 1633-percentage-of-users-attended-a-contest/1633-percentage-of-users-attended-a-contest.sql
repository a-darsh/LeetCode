# Write your MySQL query statement below
select
contest_id, round((count(user_id)/total_count)*100,2) as percentage 
from Register, 
(select count(user_id) as total_count from Users) as UserCount

group by contest_id

order by percentage desc, contest_id asc
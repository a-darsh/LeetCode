# Write your MySQL query statement below

select round(sum(tiv_2016),2) as tiv_2016 
from
(select *, 
count(*) over (partition by tiv_2015) as count15,
count(*) over (partition by lat,lon) as countloc
from Insurance) as t0
where t0.count15>1 and t0.countloc=1




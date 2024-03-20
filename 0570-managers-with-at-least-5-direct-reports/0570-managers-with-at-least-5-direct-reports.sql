# Write your MySQL query statement below
select e2.name

from Employee as e1 join Employee as e2

on e1.managerID=e2.id and e1.managerId 

group by 

e2.id

having count(*) >=5 

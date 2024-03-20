# Write your MySQL query statement below
select w2.id as ID from Weather as w1 join Weather as w2
where Datediff(w2.recordDate, w1.recordDate)=1 and 
(w2.temperature>w1.temperature)
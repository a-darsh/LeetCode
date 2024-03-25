# Write your MySQL query statement below
with Combined as (

    select requester_id as id, accept_date from RequestAccepted
    union all
    select accepter_id as id, accept_date from RequestAccepted

)

select id, count(accept_date) as num from Combined
group by id
order by count(accept_date) desc
limit 1


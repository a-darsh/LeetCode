# Write your MySQL query statement below
with first_login as (
    select player_id, min(event_date) as event_date from Activity group by player_id
),

second_login as(

    select a.player_id 
    from first_login as f join Activity as a 
    on f.player_id=a.player_id and datediff(a.event_date, f.event_date)=1

)

select 
round((select count(player_id) from second_login)/
      (select count(player_id) from first_login), 2) 
as fraction




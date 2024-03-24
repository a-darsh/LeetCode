with first_order as (

    select customer_id, min(order_date) as order_date from Delivery group by customer_id
),

immediate_order as (

    select f.customer_id
    from first_order as f join Delivery as d 
    on f.order_date=d.order_date and f.customer_id=d.customer_id
    where d.order_date=d.customer_pref_delivery_date

)

select round((count(m.customer_id)/count(f.customer_id))*100,2) as immediate_percentage
from first_order as f left join immediate_order as m on f.customer_id=m.customer_id
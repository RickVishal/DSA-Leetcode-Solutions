select 
w1.id
from Weather w1
join 
Weather w2
on
DATE_ADD(w2.recordDate, INTERVAL 1 DAY) = w1.recordDate
WHERE 
    w1.temperature > w2.temperature;


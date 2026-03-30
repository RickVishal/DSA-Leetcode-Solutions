# Write your MySQL query statement below
select c.contest_id,
Round(count(distinct c.user_id)*100/(select count(distinct user_id) from Users),2)
as percentage from Register c
group by c.contest_id

order by percentage desc,contest_id asc
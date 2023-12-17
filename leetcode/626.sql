-- 626 Exchange Seats

Create table If Not Exists Seat (id int, student varchar(255))
Truncate table Seat
insert into Seat (id, student) values ('1', 'Abbot')
insert into Seat (id, student) values ('2', 'Doris')
insert into Seat (id, student) values ('3', 'Emerson')
insert into Seat (id, student) values ('4', 'Green')
insert into Seat (id, student) values ('5', 'Jeames')

-- Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

-- probably using a window function using lead and lag to swap 'student' in consecutive rows

select id, (case when swapped_student is null then student else swapped_student end) as student
from
(
	select id, student,
		case when mod(id, 2) = 0
		then lag(student) over (order by id)
		else lead(student) over (order by id)
		end as swapped_student
	from Seat
) as t;
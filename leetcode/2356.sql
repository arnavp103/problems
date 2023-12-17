-- 2356 Number of unique subjects taught by each teacher

Create table If Not Exists Teacher (teacher_id int, subject_id int, dept_id int)
Truncate table Teacher
insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '3')
insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '4')
insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '3', '3')
insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '1', '1')
insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '2', '1')
insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '3', '1')
insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '4', '1')

-- Write a solution to calculate the number of unique subjects each teacher teaches in the university.
select teacher_id, count(distinct subject_id) as cnt from Teacher group by teacher_id

-- 627 Swap Salary
Create table If Not Exists Salary (
	id int,
	name varchar(100),
	sex char(1),
	salary int
);

Truncate table Salary;
insert into Salary (id, name, sex, salary) values ('1', 'A', 'm', '2500');
insert into Salary (id, name, sex, salary) values ('2', 'B', 'f', '1500');
insert into Salary (id, name, sex, salary) values ('3', 'C', 'm', '5500');
insert into Salary (id, name, sex, salary) values ('4', 'D', 'f', '500');

-- Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.
update Salary
set sex = case
		when sex = 'm' then 'f'
		else 'm'
	end;
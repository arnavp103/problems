-- 608 Tree Node

Create table If Not Exists Tree (id int, p_id int)
Truncate table Tree
insert into Tree (id, p_id) values (1, null)
insert into Tree (id, p_id) values (2, 1)
insert into Tree (id, p_id) values (3, 1)
insert into Tree (id, p_id) values (4, 2)
insert into Tree (id, p_id) values (5, 2)

-- Each node in the tree can be one of three types:
--     "Leaf": if the node is a leaf node.
--     "Root": if the node is the root of the tree.
--     "Inner": If the node is neither a leaf node nor a root node.

-- Write a solution to report the type of each node in the tree.

select id, 'Root' as type
from Tree
where p_id is null
union
select id, 'Leaf' as type
from Tree
where id not in (select distinct p_id from Tree where p_id is not null)
and p_id is not null
union
select id, 'Inner' as type
from Tree
where id in (select p_id from Tree where p_id is not null)
and id not in (select id from Tree where p_id is null);

-- nicer version in discussions post

select id, case when p_id is null then 'Root'
				when id in (select p_id from Tree) then 'Inner'
				else 'Leaf'
		   end as type
from Tree;


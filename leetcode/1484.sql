-- 1484 Group sold products by the date

Create table If Not Exists Activities (sell_date date, product varchar(20))
Truncate table Activities
insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone')
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil')
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask')
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball')
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible')
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask')
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt')

-- Write a solution to find for each date the number of different products sold and their names.
-- The sold products names for each date should be sorted lexicographically.

-- how does string_agg work?
-- it concatenates the values of the column specified in the argument using the seperator provided
-- it can be distinct by adding a distinct keyword
-- it can be ordered by adding an order by clause

select sell_date, count(distinct product) as num_sold, string_agg(distinct product, ',' order by product) as products
from Activities
group by sell_date
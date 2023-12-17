-- 1084 Sales Analysis III

Create table If Not Exists Product (product_id int, product_name varchar(10), unit_price int)
Create table If Not Exists Sales (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int)
Truncate table Product
insert into Product (product_id, product_name, unit_price) values ('1', 'S8', '1000')
insert into Product (product_id, product_name, unit_price) values ('2', 'G4', '800')
insert into Product (product_id, product_name, unit_price) values ('3', 'iPhone', '1400')
Truncate table Sales
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '1', '1', '2019-01-21', '2', '2000')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '2', '2', '2019-02-17', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('2', '2', '3', '2019-06-02', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('3', '3', '4', '2019-05-13', '2', '2800')

-- Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

select p.product_id, p.product_name
from Product p join Sales s on p.product_id = s.product_id
where s.sale_date between '2019-01-01' and '2019-03-31'
-- remove them if they sold in any other quarter
except
select p.product_id, p.product_name
from Product p join Sales s on p.product_id = s.product_id
where s.sale_date < '2019-01-01' or s.sale_date > '2019-03-31'
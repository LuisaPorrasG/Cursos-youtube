CREATE TABLE products (
   id int not null auto_increment,
   name varchar (50) not null,
   create_by int not null,
   marca varchar (50) not null,
   PRIMARY KEY(id),
   FOREIGN KEY (create_by) references user (id)
);

rename table products to product; -- puedo renombrar una tabla

insert into products (name, create_by, marca)
values 
('ipad', 1, 'apple'),
('iphone', 1, 'apple'),
('watch', 2, 'apple'),
('mackbook', 1 , 'apple'),
('imac', 3, 'apple'),
('ipad mini', 2, 'apple');

SELECT * from products;

drop table if exists product; --  elimino una tabla 

select alias_usuario.id, alias_usuario.email from user  alias_usuario; -- consulta 
select u.id, u.email, p.name from user u left join products p on u.id = p.create_by; -- left join
select u.id, u.email, p.name from user u right join products p on u.id = p.create_by; -- rihth join
select u.id, u.email, p.name from user u inner join products p on u.id = p.create_by; -- inner join

SELECT u.id, u.name, p.id, p.name  from user u cross join products p; -- croos join, relacion de cada producto con los usuarios 

SELECT count(id), marca from products group by marca; -- agrupa losresultados de acuerdo al parametro, en este caso la maarca
SELECT count(p.id), u.name from products p left join user u on u.id = p.create_by group by p.create_by; -- me devuelve la cantidad de articulos que tiene cada nombre
SELECT count(p.id), u.name from products p left join user u on u.id = p.create_by group by p.create_by having count(p.id) >=2 ; -- me devuelve una consulta mayor o igual a 2 de productos

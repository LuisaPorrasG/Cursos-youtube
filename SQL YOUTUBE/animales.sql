CREATE DATABASE usuarios;
-- creo una tabla de mi base de datos
CREATE TABLE user(
    id int not null auto_increment,
    name varchar (50) not null,
    edad int not null,
    email varchar (50) not null,
    PRIMARY KEY (id)
); 

INSERT INTO user (name, edad, email) values ("Luisa", 23, "laluisa@.com");
INSERT INTO user (name, edad, email) values ("Diana", 34, "laDiana@.com");
INSERT INTO user (name, edad, email) values ("OScar", 23, "elOscar@.com");
INSERT INTO user (name, edad, email) values ("chanchito", 30, "elChanchito@.com");

SELECT * FROM user; --  selecciono todos los datos de la tabla para que me la mueste

SELECT * FROM user limit 1; -- da el primer registro que encuentre

SELECT * from user where name = "Luisa";
SELECT * FROM user WHERE edad < 30;
SELECT * FROM user WHERE edad >= 15;
SELECT * FROM user WHERE edad > 20 and email = "laluisa@.com";
SELECT * FROM user WHERE  email != "elOscar@.com";
SELECT * FROM user WHERE edad between 23 and 28; -- busqueda de un rango con between
SELECT * FROM user WHERE email like "%.com%"; -- busca los registros que en email tenga .com en su inico o final
SELECT * FROM user WHERE email like ".com%";  -- devuleve null  porque ningun registro incia con .com

SELECT * FROM user ORDER  by edad asc; -- 	qque me ordene los resultados de orden ascendente en edad
SELECT * FROM user ORDER  by edad desc; -- 	qque me ordene los resultados de orden descendente en edad

SELECT max(edad) as mayor_sobrenombre from user; -- coonsulta el mayor registro de edad
SELECT min(edad) as menor_sobrenombre from user; -- coonsulta el menor registro de edad

SELECT id, name from user;
SELECT id, name as nombre from user;

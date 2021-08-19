create table student (
name VARCHAR2(24),
mobile VARCHAR2(20),
gender char(1),
city varchar2(24)
);
insert into student VALUES('John','55554444','M','NewYork');
select * from student;
delete from student;
desc student;

create table menu (
menu_name VARCHAR2(50),
price number(100,0)
);
create table sell (
menu_name VARCHAR2(50),
cnt number(100,0),
sum number(100000,0),
mobile VARCHAR2(50)
);
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


field/column 세로 (열)
row/record 가로(행)

스키마(schema -> scheme:구조) (
menu_name VARCHAR2(50),
cnt number(100,0),
sum number(100000,0),
mobile VARCHAR2(50)
)

desc 테이블명;  :테이블 스키마 확인

insert into student VALUES('John','55554444','M','NewYork');
insert into student (mobile,name,city,gender) values ('555556666','jacob','miami','M');
insert into 테이블명 set 칼럼명1=값1, 칼럼명2=값2...

create table student (칼럼명1 타입(길이),칼럼명2 타입(길이)....)

select 칼럼명1,...칼럼명N from 테이블명

selct * from 테이블명

desc 테이블명

delete from 테이블명  //테이블내의 실제데이터 (데이터)

drop table 테이블명 //테이블 schema (메타데이터)






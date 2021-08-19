//DB관련 설명
table  데이터 보관장소
view  read-only(조회만 가능한 테이블) 
synonym 별명(nickname/alias) // CRUD 모두 가능
index 테이블데이터를 정리, 검색속도를 증가.
sequence 자동 번호 생성기

{procedure
package
function} 이거는 있지만 안함 PL/SQL(Programming Language with SQL)

SQL         DML         DDL
-------------------------------------------
Create      insert      create/grant
Read        select      select
Update      updage      alter
Delete      delete      drop/truncate/revoke


대상        실제데이터  메타데이터

varchar (Variable Character: 가변길이 문자열)

create table 이름( 칼럼명1타입(길이),칼럼명2타입(길이)) 테이블구조 스키마

insert into 테이블명 values(값1,값2...값n)

select * from 테이블명

delete from 테이블명

desc student; 유형확인

타입 종류
char
varchar2
number(m,n) m:전체길이, n:소수점이하자리수

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

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

update 테이블명 set 컬럼명1=값1,.....컬럼명N=값N

insert into ~ values ~
select ~ from ~
delete ~ from ~
update ~ set ~

문자열 char,varchar2 long(오라클) / char, varchar, text(MySQL) 
정수 number(N), number
실수 number(N,P), number,float
날짜/시간 date, timestamp(ms)

Lob(Larae Obiect)
이미지/동영상을 DB에 저장하는 방법
(1) 이미지/동영상 파일이름을 DB 테이블에 문자열 데이터로 저장
    ('http:/image.human.com/student/img/파일이름.jpg')
(2) 실제파일은 http:/image.human.com의 student/img폴더 안에 저장   

alter table 테이블 add(컬럼명 타입(길이))
                   drop column 칼럼명
                   modify (컬럼명타입(길이)) -- 타입/길이만 변경
                   rename column 컬럼명old to 컬럼명new --타입/길이는 불변,컬럼명 변경


alter table 테이블 add 컬럼명 타입(길이)
                   drop 컬럼명
                   change 컬럼명 새컬럼명 타입(길이)  <MySQL/MariaDB>

char(10) = 10자리를 다 사용해야함 주로 주민번호등에 많이사용

varchar2(10) = 1o자리중 자기가 쓴만큼 사용 
select '['||a||']','['||b||']' from chartest; //길이 확인용


-----------------------------------------------------------
시퀀스 설명
create sequence 시퀀스명 start with 첫값 increment by 증감분
            minvalue 최저값/maxvalue 최고값 cycle /nocycle

------------------------------------------------------------
select/update/delete 조건하에서 실행하는 경우가 대부분 <- where

select * from student where name='john'

MSCP
OCA (Oracle Ceritified Administrator) - DBA실력 (OCA족보)

-----------------------------------------------------------
검색하기
(1) 작업대상 테이블이름을 알아내서 from 뒤에 쓴다
(2) 관련된 컬럼명들을 찾아낸다.
(3) 표시할 컬럼명을 select 바로 뒤에 나열한다
(4) 조건비교하는 컬럼명을 쓰고 조건에 해당하는 연산자를 적용한다 -> where

---------------------------------------------------------------------
select * from student where gender='M';
--데이터 자체는 대소문자 구분이 있다 (키워드 테이블명 컬럼명은 관계없음)

---------------------------------------------------------------------
수정하는법
update employees set salary=8500 where employee_id = 206;

salary>=5000 and salary<=6000 == salary between 5000 and 6000(between연산자)


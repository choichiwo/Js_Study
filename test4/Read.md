//DB관련 설명
table  데이터 보관장소
view  read-only(조회만 가능한 테이블) 
synonym 별명(nickname/alias)
index 테이블데이터를 정리, 검색속도를 증가.
sequence

{procedure
package
function} 이거는 있지만 안함 PL/SQL(Programming Language with SQL)

SQL         DML         DDL
-------------------------------------------
Create      insert      create/grant/revoke
Read        select      select
Update      updage      alter
Delete      delete      drop/truncate


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
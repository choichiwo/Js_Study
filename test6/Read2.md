SELECT * from room;
desc room;
--backup 만들기
create table room1 as select * from room;
-- restore 하기
select * from room1; -- 사본확인
drop table room; -- 원본테이블 제거
create table room as select * from room1;--사본을 원본에 복구
select * from user_sequences;
create sequence seqroom start with 4;--시퀀스 만들기 뒤에4는 마지막 숫자에 맞춰서 바꿈
select seqroom.nextval from dual;--시퀀스 확인
select seq_room.nextval from dual;--시퀀스 확인
update room set name='칠성산' where roomcode=2;
commit;

create table member (
username varchar2(30) not null,
userid varchar2(20) primary key,
passcode1 varchar2(12) not null,
mobile varchar2(20) not null
);
desc member;
drop table member;

create table booking (
bookcode int primary key,
roomcode int not null,
person int not null,
checkin char(8) not null,
checkout char(8) not null,
name VARCHAR2(20) not null,
mobile VARCHAR2(20) not null
);

select * from roomtype;
select roomcode, name roomname, 
    (select name from roomtype where typecode=2) as typename,
    howmany, howmuch
from room 
where type=2 and roomcode not in(
select roomcode from room
INTERSECT
select roomcode from booking where (checkin between '21-09-06' and '21-09-08') 
and (checkout between '21-09-06' and '21-09-08') or (checkin<'21-09-06' and checkout>'21-09-08'));

select a.roomcode,a.name,b.name,a.howmany,a.howmuch
from room a,roomtype b
where a.type=b.typecode;

SELECT
    *
FROM roomtype;

desc room;
select * from room;
select * from booking;

create table booking (
bookcode int primary key,
roomcode int not null,
person int not null,
checkin char(8) not null,
checkout char(8) not null,
summuch VARCHAR2(20) not null,
name VARCHAR2(20) not null,
mobile VARCHAR2(20) not null
);
create sequence seqbooking;
select seqbooking.nextval from dual;
drop table booking;
commit;
desc booking;
select * from room;

select to_char(checkin, 'YYYY/MM/DD')
    , to_char(checkout, 'YYYY/MM/DD')
    from booking;
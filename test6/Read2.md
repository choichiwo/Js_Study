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
bookcode int,
roomcode int,
person int,
checkin char(8),
checkout char(8),
name VARCHAR2(20),
mobile VARCHAR2(20)
);
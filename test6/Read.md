create table room (
roomcode decimal(2) primary key, --단일컬럼, 전체테이블의 그 칼럼에서 유일한 값을 갖는다.
name varchar2(20),
type decimal(2),
howmany decimal(2),
howmuch decimal(6,0)
);
create table roomtype(
typecode decimal(2) primary key,
name varchar2(20)
);
create sequence seq_room;
insert into roomtype values(1,'Suite Room');
insert into roomtype values(2,'Family Room');
insert into roomtype values(3,'Double Room');
insert into roomtype values(4,'Single Room');
insert into room values(seq_room.nextval,'백두산',1,8,500000);
insert into room values(seq_room.nextval,'한라산',2,6,450000);
insert into room values(seq_room.nextval,'지리산',3,5,400000);
insert into room values(seq_room.nextval,'태조산',4,2,200000);
select * from roomtype;
select a.roomcode,a.name,b.name,a.howmany,a.howmuch
from room a,roomtype b
where a.type=b.typecode;
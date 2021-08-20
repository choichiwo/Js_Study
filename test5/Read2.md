널인값 찾는법
select * from employees where manager_id is null;

무결성(Integrity)&일관성(consistency)

정령 하는법(오름차순,내림차순) 
이때 널은 비교대상이 될수 없어서 뒤로 뺴짐
숫자 < 대문자 < 소문자
'19' > '100' 문자로 비교하는것은 순서상 비교해서 큰쪽이 더 큰것으로 판단
알파벳크기비교
a < ab 
A < a
오름차순(asc) (1234...100순서 abcd...z순서)
select employee_id,emp_name from employees order by employee_id;
내림차순(dsc) (1009998....1순서 zywx....a순서)
select employee_id,emp_name from employees order by employee_id DESC;


-------------------------------------------
테이블 다시 전환하는 순서
drop table employees; 
단톡에서 파일을 받고
cmd로 파일 받은 장소로 간다음
imp ora_user/human123 file=employees.dmp full=y

--------------------------------------------------
조건 붙이기
like **
** 에 표시하면 =하구 같은 의미 **인 사람 찾아라
**% 처음에 **들어가는 사람
select * from employees WHERE emp_name like 'son%' order by emp_name;
%**% 중간에 **들어가는 사람 또는 처음에 **들어가는 사람 , 끝에 **들어가는 사람을 다 검색될수 있음
select * from employees WHERE emp_name like '%son%' order by emp_name;
%** 끝에 **들어가는 사람
select * from employees WHERE emp_name like '%son' order by emp_name;
**%* **으로 시작하구 끝에 *이 들어가는 사람
select * from employees WHERE emp_name like 'son%n' order by emp_name;

두개의 조건일때는 
select * from employees WHERE emp_name like 'son%' or emp_name like 'son%' order by emp_name;

-----------------------------------------------------------
% == * (0개이상의 문자들)
_== 어떤 한 문자.

-------------------------------------------------------
s__ s로 시작하는 세글자 예 son등을 검색
select * from employees WHERE emp_name like 's__' order by emp_name;

----------------------------------------------------------
in (200, 300, 400, 500) 범위안에 있는 것을 검색 

not을 붙이면 부정문으로 전환
not in, not like

--------------------------------------------------
sql 함수
abs 절대값
select abs(-12) from dual;   
--dual == 상징적인 가상테이블 의미없음 from을 써주기 위해서 씀
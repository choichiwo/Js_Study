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
select * from employees WHERE emp_name like '%son' order by emp_name;
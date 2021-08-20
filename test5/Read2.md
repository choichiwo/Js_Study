널인값 찾는법
select * from employees where manager_id is null;

무결성(Integrity)&일관성(consistency)

정령 하는법(오름차순,내림차순) 
이때 널은 비교대상이 될수 없어서 뒤로 뺴짐
알파벳크기비교
a < ab 
A < a
오름차순 (1234...100순서 abcd...z순서)
select employee_id,emp_name from employees order by employee_id;
내림차순 (1009998....1순서 z....a순서)
select employee_id,emp_name from employees order by employee_id DESC;
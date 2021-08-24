select period,region,to_char(sum(loan_jan_amt),'9,999,999.99') total_jan
    from kor_loan_status
    where period like '2013%'
    group by period,region
    order by period,region;


-------------------------------------------------------
파일 임포트하는법 
먼저 파일을 받고
imp ora_user/human123 file=goods.dmp(파일명) full=y


--------------------------------
테이블 명칭 변경하는법
alter table exp_goods_asia rename to goods;


-----------------------------------------------
합집합 Union

중복된거만 찍어라
select goods from goods where country='한국'
union 
select goods from goods where country='일본';

중복되고 다찍어라
select goods from goods where country='한국'
union all
select goods from goods where country='일본';

교집합 Intersect 
select goods from goods where country='한국'
intersect
select goods from goods where country='일본';

차집합 Minus
한국꺼에서 일본꺼 뺸값
select goods from goods where country='한국'
minus
select goods from goods where country='일본';

------------------------
집합연산자로 연결되는 각 select문의 컬럼의 갯수와 타입이 각각 일치해야 한다.
select문을 연결할 때, order by 절은 마지막에 붙인다.
BLOB,CLOB,BFILE타입의 컬럼은 집합연산자를 적용할 수 없다.
union, intersect, minus연산자는 long타입컬럼에는 적용할 수 없다.(union all에는 적용가능)


update booking set roomname='금강산' where roomname='한라산'


update booking set roomname='금강산' where mobile='77778888'



-----------------------------------
join하는 법

이름과 직위명을 출력(employees,job테이블을 join)

내부조인(inner join)

동등조인(equi-join) 80%정도 비율
select a.emp_name,b.department_name
from employees a, departments b
where a.department_id=b.department_id;

semi-join(in/exists)
anti-join(!=)

셀프조인(self join)
select a.emp_name,a.employee_id,b.emp_name as manager_name
    from employees a, employees b
    where a.manager_id=b.employee_id;

외부조인(outer join) 
=, >, <, >=, <=, <>
(+) 이표시 들어감 널값도 나오게함
select a.emp_name,a.employee_id,b.emp_name as manager_name
    from employees a, employees b
    where a.manager_id=b.employee_id(+)  --for Oracle
    order by a.emp_name;    


 select a.emp_name,a.employee_id,b.emp_name as manager_name
    from employees a left outer join employees b --MySQL
    on a.manager_id=b.employee_id
    order by a.emp_name;   

----------------------------------------
select *
    from (select * from employees) --서브쿼리
    where manager_id=100
    order by emp_name;    


-------------------------------------------
select a.emp_name,b.department_name
from employees a, departments b
where a.department_id =b.department_id and parent_id is null;    

select a.emp_name,b.department_name
from employees a, departments b
where a.department_id in (select department_id from departments where parent_id is null) and a.department_id =b.department_id; --중첩쿼리


select a.emp_name,b.department_name
    from (select emp_name,department_id from employees) a,
         (select department_name,department_id from departments where parent_id is null) b
    where a.department_id=b.department_id;    --인라인 서브쿼리

위에 세개다 같은결과가 나옴

-----------------------------------------------

select a.employee_id, a.emp_name,
      (select b.emp_name from employees b where a.manager_id=b.employee_id) as manager_id,
      d.department_name, 
      j.job_title
from employees a, departments d, jobs j
where a.department_id=d.department_id and a.job_id=j.job_id
order by a.employee_id;  


select a.employee_id as "사원 번호", 
       a.emp_name as "사원 이름",
      (select b.emp_name from employees b where a.manager_id=b.employee_id) as "담당 매니저",
      d.department_name as "부서", 
      j.job_title as "직책"
from employees a, departments d, jobs j
where a.department_id=d.department_id and a.job_id=j.job_id
order by a.employee_id;   


Terminology(전문용어)
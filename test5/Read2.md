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

숫자함수

abs 절대값
select abs(-12) from dual;   
--dual == 상징적인 가상테이블 의미없음 from을 써주기 위해서 씀
power (2,3) 제곱근 2의3승 8이 나옴

select ceil(10.123),floor(10.123) from dual;
중요 ceil : 주어진 값보다 큰 정수 중 가장 작은 정수
중요 floor : 주어진 값보다 작은 정수 중 가장 큰 정수


문자함수

select lower(emp_name),upper(emp_name),initcap(emp_name) from employees WHERE employee_id=100;
중요 lower 소문자로 / 중요 upper대문자로 initcap 첫글자를 대문자로 나머지를 소문자

concat 연결연산자
SELECT concat(employee_id,emp_name) from employees; 두개만 연결 가능
위와같음  
select employee_id||emp_name from employees; 이걸 더 많이 사용 그리고 이것은 계속해서 연결할수있음

중요
substr(컬럼명,시작인덱스,길이)
select substr(emp_name,1,4) from employees;
c언어계열(java,javascript,python) -> 시작인덱스 = 0
pascal언어계열(oracle sql,pl/sql) -> 시작인덱스 = 1


ltrim 왼쪽을 짜름
select ltrim(emp_name, "A") from employees
rtrim 오른쪽을 짜름
select rtrim(emp_name, "A") from employees
양쪽다 짜르는법
select ltrim(rtrim(emp_name)) from employees


lpad(컬럼명/문자열,전체길이,채울문자열) 
컬럼명/문자열의 길이가 '전체길이' 보다 작으면 왼쪽을 '채울문자열'로 채운다
select lpad(emp_name,20,'*') from employees;

중요
select replace(emp_name,' ','-') from employees order by emp_name;
컬럼명/문자열에서 두번쨰 문자열에 해당하는 부분을 세번쨰 문자열로 대처

중요
select emp_name,instr(emp_name,'an') from employees order by emp_name;
컬럼명/문자열에서 두번쨰 문자열의 시작하는 인덱스 값을 변환


날짜함수

select sysdate from dual;
sysdate 날짜 표시 년 월 일

변환함수

중요 to_char
select to_char(sysdate,'YYYY-MM-DD') from dual;
select emp_name, to_char(hire_date,'YYYY-MM-DD') from employees order by hire_date;
YYYY-MM-DD = 2019-08-11  YY-MM-DD = 19-08-11 YYYY-MONTH-DD DAY = 2019-8월-11 11일

to_number
insert into student(id,name,mobile,gender) VALUES(to_number('1234'),'..','...','j');

to_date
select to_date('20210820','YYYY-MM-DD') from dual;

select to_char(to_date('20210820','YYYY-MM-DD'),'YYYY-MM-DD') from dual;


null관련 함수

중요 nvl
null값을 변환 
select emp_name,commission_pct from employees order by emp_name;
select emp_name,nvl(commission_pct,12) from employees order by emp_name;

nullif
(컬럼명1/값1,컬럼명2/값2): 


ifnull(MySQL)
(컬럼명1/값1,컬럼명2/값2): 컬럼명1/값1이 null이면, 컬럼명2/값2을 출력,
                         컬럼명1/값1이 null이 아니면, 컬럼명1/값1을 출력


-----------------------------------------------------------------

중요 count/ 중요 distinct/ 중요 sum/avg/중요 min/중요 max/variance(분산)/stddev

count() 안에 컬럼명을 사용할 떄, 컬럼내의 값이 null인 것은 count에서 제외된다.
select count(*),count(commission_pct) from employees;

널값을 0으로 전환해서 나오게 변환
select count(*),count(commission_pct),count(nvl(commission_pct,0)) from employees;


distinct 뒤따라 나오는 컬럼에 유일한 값만 조회, 중복값 제거
select distinct department_id 
        from employees
        where department_id is not null
        order by department_id;

select distinct cust_year_of_birth as byear from customers order by byear;

cust_year_of_birth as byear == as byear 명칭을 지정해주는 방식


select distinct cust_year_of_birth from customers order by 1; == 컴럼번호 1부터 오름차순


select employee_id,emp_name,manager_id from employees order by 3; 
== employee_id,emp_name,manager_id 이 세가지중 3번쨰인 manager_id 정렬 2면 emp_name로 정렬


먼저 manager_id정렬 후에 그안에서 emp_name 정렬 == 이중정렬이라고도 함.
select employee_id,emp_name,manager_id from employees order by manager_id,emp_name; 

select employee_id as eid,emp_name as ename, manager_id as mid
    from employees
    order by mid,eid;


sum() 합계구하기
select * from kor_loan_status;
select sum(loan_jan_amt) from kor_loan_status where region='세종' and gubun='기타대출';    

avg() 평균구하기
select * from kor_loan_status;
select avg(loan_jan_amt) from kor_loan_status where region='세종' and gubun='기타대출'; 



min() 최소값  max() 최대값   구하는 방법
select min(math),min(korean),max(math),max(korean) from student;


집계함수

group by = 특정 그룹을 묶음
group by 뒤에 쓸 컬럼은 무조건 select뒤에 모두 나열돼야 한다
select에 나열된 컬럼 뒤에는 무조건 하나이상의 집계함수가 있어야 한다.

select department_id, count(*) from employees group by department_id order by department_id;


having은 집계함수랑 같이 쓰인다.  즉 group by랑 같이 쓴다

즉 group by랑 같이 쓴다  

뒤에 조건을 붙여 주는것 count(*)>1, count(*) between 2 and 10 이런식으로 

select manager_id,count(*) as cnt from employees
        where manager_id is not null
        GROUP BY manager_id having count(*)>1
        order by cnt;

select manager_id,count(*) as cnt from employees
        where manager_id is not null
        GROUP BY manager_id having count(*) between 2 and 10
        order by cnt;        

select region,gubun,sum(loan_jan_amt)
        from kor_loan_status
        group by region,gubun
        ORDER by region;        

select 칼럼명1...칼럼명N,집계함수
        from 테이블명
        group by 칼럼명1...칼럼명N
        having 집계함수에 대한 조건
        order by 칼럼명a...칼럼명z
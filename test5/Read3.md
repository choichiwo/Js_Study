select period,region,to_char(sum(loan_jan_amt),'9,999,999.99') total_jan
    from kor_loan_status
    where period like '2013%'
    group by period,region
    order by period,region;


합집합 Union
교집합 Intersect 
차집합 Minus


-------------------------------------------------------
파일 임포트하는법 
먼저 파일을 받고
imp ora_user/human123 file=goods.dmp(파일명) full=y


--------------------------------
테이블 명칭 변경하는법
alter table exp_goods_asia rename to goods;
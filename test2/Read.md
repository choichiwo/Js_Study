table
    tr 열 세로 인덱스가 0으로 시작
        td 행 가로 인덱스가 0으로 시작

DOM(Document Object Model)    

rowspan 열 합침(위아래로)

colspan 행 합침(좌우로) 

table id=tbl
$('#tbl').find('tr;eq(1) td:eq(2)').text('A');
$('#tbl te:eq(1) td:eq(2)').text('A');

m=1;
n=2;
str='#tbl te:eq('+m+') td:eq('+n+')';
str='#tbl tr:eq(${m}) td:eq(${n})';
$(str).text('A');
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

정규표현식(Regular Expression)

[] -> 또는

* -> 0개 이상의 문자

. -> 한개의 문자

{n} -> 반복횟수
^ -> ~로 시작하는
$ -> ~로 끝나는
abc

^Ab*
Ab$
a로 시작하는 모든단어
 "a*" -> at,a,another
 "a." -> at,an,am
 "a.{3} -> any,amy,ami
a로 시작하는 세글자짜리 단어
첫글자가 대문자인 단어
the <- The => 대소문자구분없이 "[Tt]he" <- 정규표현식
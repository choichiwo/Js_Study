#정규표현식
#### 정의 : Regular Expression의 약자 regex
#### 탄생배경 : 많은 텍스트속에서 원하는 패턴을 검색
#### 사용처 : 찾기, 바꾸기, 유효성검사,
#### 실제 개발 경험 : 키움증권 날짜 입력
(그림으로 설명) 달력에서 날짜 선택하는 기능이 있었는데 타이핑으로 바로치고싶어하는 고객의 요구가 있어서 유효성 검사를 해야했음.
년-월-일을 yyyymmdd형태로 java단으로 넘어가야했음. 예) 20191231
총 10자리를 받고 ,나 .,-/이 혹시있다면 제거
yyyy중 앞의 2글자는 19또는 20으로 시작
mm중 앞글자는 0또는 1만 가능
    앞이 1일경우 뒤는 0,1,2만 가능
dd중 앞글자는 0,1,2,3만 가능
    앞이 0이면 뒤는 0이 되면 안됨.
    앞이 3일경우 뒤는 0,1만 가능
-> 여기에 국가공휴일, 우리회사만 자체적으로 쉬는 공휴일 등을 DB에 넣고 유효한 날짜인지 판별하면 모듈의 완성.




#### 공부한 소스 : https://www.youtube.com/watch?v=t3M6toIflyQ&t=884s
#### 장점 : 익히면 생산성이 매우 증가한다.
#### 단점 : 배우지 않은사람은 무슨소린지 하나도 모르고 배워도 가독성이 안좋다.
#### 문법 : /패턴/옵션
#### 테스트하기 좋은 사이트 : regexr.com/5mhou
아래의 Tools에 explane이 있어서 좋다.
#### 테스트 데이터 :
```text
Hi there, Nice to meet you. And Hello there and hi.
I love grey(gray) color not a gry, graay and graaay. grdy
Ya ya YaYaYa Ya

abcdefghijklmnopqrstuvwxyz
ABSCEFGHIJKLMNOPQRSTUVWZYZ
1234567890

.[]{}()\^$|?*+

010-898-0893
010 898 0893
010.898.893
010-405-3412
02-878-8888

dream.coder.ellie@gmail.com
hello@daum.net
hello@daum.co.kr

http://www.youtu.be/-ZClicWm0zM
https://www.youtu.be/-ZClicWm0zM
https://youtu.be/-ZClicWm0zM
youtu.be/-ZClicWm0zM
```

#### 공부
4가지 카테고리로 나눠서 공부한다.
##### 1. Groups and Ranges(그룹과 범위)
```
| : 또는
- : 범위
    예) [a-zA-Z0-9]
() : 그룹
    예) gr(e|a)y
[] : 문자셋. 괄호안의 어떤문자든
    예) gr[aed]y
[^] : 부정문자셋. 그문자셋 빼고
(?:) : 찾지만 그룹을 기억하지는 않음
```
---
##### 2.Quantifiers(수량)
```
? : 앞의글자가 0,1 (없거나 있거나)
* : 앞의글자가 0, 1, n(없거나 있거나 많거나)
+ : 앞의글자가 1, n (하나 또는 많이)
글자{n} : n번반복
글자{min, }: 최소
글자{min,max }: 최대
```

---
##### 3. Boundary-type(단어 경계)
```
\b : boundary. 단어경계
\B : 단어경계가 아님
    예) Ya\B : Ya중에 끝이 단어의 경계가 아닌것
^ : 부정문자열이 처음에 쓰이면 문장의 시작
$ : 문장의 끝
```
---
##### 4. Character classes(문자 클래스)
```
. : 아무글자(줄바꿈 문자 제외)
\a : a라는 특수문자 그대로
    예) \[\] : []
\d : digit. 숫자
\D : 숫자제외
\w : word. 문자
\W : 문자제외
\s : space. 공백
\S : 공백제외

```
---
#### 연습문제
위의 데이터를 보고
1. g로 시작하고 y로 끝나는 어떤단어든지 선택하고싶다.
g[a-zA-Z0-9]*y

1.알파벳으로 시작하는 문장의 시작부
^[a-zA-z]

1. 단어의 끝이후에 나타나는 2개이상의 스페이스
\b +

1. 국가이름에서 -스탄으로 끝나는 국가 찾기
[가-히]*스탄

1. 3이 3개이상들어간 숫자
(\d*3\d*){3,}

2. 전화번호만 골라보시오.
답 : 제일 쉬운것부터 접근 하는것이 좋은 방법
\d\d\d-\d\d\d-\d\d\d\d
\d{2,3}[ .-]\d{3,4}[ .-]\d{4}

3. 이메일을 골라보시오
아이디로 들어갈수있는건 영어와숫자, ._+-
이런것들이 여러번 반복가능
[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+.+[a-zA-Z]
[a-zA-Z0-9.-]+@[a-zA-z0-9.]+

3. 유튜브 주소에서 아이디만 가져와보시오.
http도, https도 가능하고 뒤에는 //
그리고 이 전체가 생략가능
www.도 있어도 되고 없어도되고
눈썰미가 좋아야 11발견. 없어도 상관없다.
괄호가 3개기 때문에 3개의 그룹이 지어졌지만 원하지않는것에 ?

(https?:\/\/)?(www\.)?youtu.be\/([a-zA-Z0-9-]{11})
(?:https?:\/\/)?(?:www\.)?youtu.be\/([a-zA-Z0-9-]{11})


#### 퀴즈 : https://regexone.com/
#### 옵션(플래그)
g : global. 매칭되는 다수의 것을 기억한다.
m : multiline.
줄띄움을 무시하고 하나의문단으로 볼지
줄띄움을 각각의 문단으로 멀티커서처럼 봄

##### 자바스크립트
const regex = /(?:https?:\/\/)?(?:www\.)?youtu.be\/([a-zA-Z0-9-]{11})/;
const url = 'https://www.youtu.be/-ZClicWm0zM';
url.match(regex);
const result = url.match(regex);
result[1];

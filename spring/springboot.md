- [진짜 정리 잘된 mysql, gradle 블로그](https://congsong.tistory.com/category/Spring%20Boot)
  - [게시판 테이블생성, controller, service, domain, mapper 패키지, Xml, DBConfiguration, Junit으로 CRUD테스트](https://congsong.tistory.com/15?category=749196)
  - [게시글 등록](https://congsong.tistory.com/16?category=749196)
  - [글 리스트](17)  ,[글 상세내용](19),
  - [글 삭제](20) 403에러 csrf
- [스프링 공식 사이트](https://start.spring.io/)
- [완전 강추 책](스프링부트  시작하기_ 김인우 저자)
---
### 스프링과 스프링 부트 차이
  - 왜 이름이 스프링인가? 개발자들의 겨울이 끝났다는 의미.
  스프링부트의 소개문장 : 쉽게 만든다. 단독적인. 상용화수준의. 스프링기반 애플리케이션. 그냥 실행.
  - 스프링부트의 가장큰차이점
  dependency. 너무 길고 버전까지 정확하게 명시해야한다.    훨씬 짧아지고 버전도 권장버전으로 자동 설정.
  설정도 application.properties에서 간단하게 다할수 있다. 최근에는 application.yml     이 유행하고있다.
  인간친화적. yaml ain't markup language   원래는 yet another markup language
  내장서버.  서버구동시간이 절반가까이 단축.
  내장 서블릿 컨테이너 덕분에 jar파일로 간단배포.
---

## 1. 개발환경 설정
스프링은 개발환경 설정이 반이라 할정도로 어렵지만 스프링부트와 STS4조합이면 설정이 매우쉽다.
다수의 인원이 개발을 할때는 공통적인 개발환경을 구성하고 편하게 설치 및 배포를 하는것이 매우 중요하다.
한폴더안에 STS, JDK, workspace 를 다 만들어놓고 그 폴더만 압축해서 배포하는 방법을 쓴다.
- JAVA_HOME 설정
- JDK위치가 기본경로가 아닐경우 ini파일의 -vmargs 옵션위쪽 아무곳에나 -vm 해서 JDK 경로설정, 힙 메모리설정
- 이클립스 워크스페이스 설정
- STS 플러그인 설정(마켓플레이스)
  - Buildship Gradle
  - Minimalist Gradle Editor(색상, 자동완성)
  - Windows - preferences - General  - Editors - File Associations메뉴에서 *.gradle 찾아서 Minimalist Gradle Editor를 기본에디터로 설정.
- 이클립스 메뉴 및 Perspective변경
  - Windows - Perspective - Customize Perspective - Shortcuts 에서 필요한 메뉴 선택
  - 좌측상단 Project Explorer 옆의 아래삼각형 버튼클릭 - Package Presentation - Hierarchical 선택
  - 뷰변경 Windows - Show view - Other
  (Console, Search, Problems, Progress, Package Explorer(이건 프로젝트 익스플로어 뷰 옆으로 이동)추가
    Markers, Properties, Data Source Explorer, Snippets 삭제
  )
  - 인코딩 설정
    - Window - Preferences - General - Workspace - Text file encoding을 UTF-8로


## 2. 프로젝트 생성
1. file - new - Spring Starter Project
제일 최소의 의존성은 Web, DevTools
1. 프로젝트 우클릭 - Run As - Spring Boot App 이클립스 콘솔창에 Spring 로그가 출력되면 정상적으로 프로젝트가 생성된것.
로그의 끝부분을 보면 Tomcat started on port(s) : 8080(http) 로 돼있을거다. 스프링부트는 톰캣서버를 내장하고있기 때문에 따로 설정안해도 됨.
1. 브라우저에서 localhost:8080입력
Whitelabel Error Page뜨면 정상
1. Hello World페이지 만들기
기본 패키지 밑에 controller패키지 만들고, 그밑에  HelloController클래스 생성
```java
@RestController
public class HelloController{
  @RequestMapping("/")
  public String hello(){
    return "Hello World!";
  }
}
```
1. 다시 브라우저에서 localhost:8080입력
1. application.properties 설정
  - #서버 재시작 없이 HTML, JS 등 변경 사항 적용
  compile("org.springframework.boot:spring-boot-devtools")
  - db접속정보
  datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:{port(보통3306)}/{DB명}?useSSL=false
  username: {사용자계정(따로 설정 안 했으면 root)}
  password: {계정 비번}


## 3. DB연결
Mybatis, mysql, lombok, stst4조합
https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=aube17&logNo=221524291517&redirect=Dlog&widgetTypeCall=true&directAccess=false


## 4. SQL연결


## 5.  Security 적용
- SecurityConfig.java 만들어서 유저권한, 로그인안됐을때 보여줄 페이지 등 설정한다.
- encode 함수 = 비밀번호 암호화 할때 사용
    input이 같아도 output 이 다르다.
- watch함수 = 해시결과의 일치여부를 반환하는 함수
    첫번째 인자로는 암호화되기전 스트링, 두번째 인자로는 암호화된 후의 스트링

---

# log 로그
요즘은 logback 라이브러리 많이 사용한다. slf4j와함께 스프링의 표준이기도 하다.
테스트
junit 4가 굉장히 오래유지되다가 최근에 5버전 사용하는 추세. mockito, assertj는 테스트를 편하게 하도록 도와주는 라이브러리.

---


포트번호 찾아서 종료시키기
netstat -ano | find "8080"
taskkill /f /pid 번호
---

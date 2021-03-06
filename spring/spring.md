# 역사와 배경
- 스프링 공식 사이트의 한줄 소개
Spring makes it easy to create Java enterprise applications.
It provieds everything you need to embrace the Java language in an enterprise environment.
자바 엔터프라이즈 애플리케이션 개발을 편하게 해주는 오픈소스 경량급 애플리케이션 애플리케이션 프레임워크
  - 엔터프라이즈 애플리케이션은 뭔가?
    서버에서 동작하며 기업과 조직의 업무를 처리해주는 시스템.
    - 대규모의 복잡한 데이터를 관리하고, 이러한 데이터를 이용해 비지니스 프로세스의 지원 및 자동화를 제공한다.
    - 비지니스의 근간으로 보안과 안정성, 확장성이 뛰어나야 한다.
    - 다수의 사용자가 접근하며 기업내 분산된 다른 엔터프라이즈 애플리케이션과 통합된다.
    - 데이터 입출력을 위한 다양한 사용자 인터페이스가 제공된다.
    - 엔터프라이즈 앱의 예: 고객서비스, 공급망, 인사, 회계, 보험, 외환거래, 환자기록, 배송추적
    - 엔터프라이즈가 아닌 앱의 예 : 운영체제, 게임, 워드프로세서, 공장자동화, 승강기제어
  - 엔터프라이즈 에디션 자바 (Java EE)
    - 엔터프라이즈 애플리케이션에 필요한 확장성, 신뢰성, 보안성 등을 제공하는 자바 플랫폼이자 프레임워크
    - 대규모, 네트워크, 다계층 애플리케이션을 더 쉽고 안전하고 탄탄하게 구축할 수 있도록 설계됨
    - 웹을 통한 UI, 시스템통합을 위한 리모팅, 선언적 트랜잭션 처리 등 전체 애플리케이션 스택을 제공한다.
    - 다양한 자바 명세 요청서를 바탕으로 작성된 표준 API 모음이다.
    - 자바 EE서버는 2가지로 나뉜다.
      - 웹 모듈만 배포가능한 경량급 WAS를 서블릿 컨테이너라고 부른다.
      - 자바EE의 모든 표준을 지원하고 다양한 모듈로 배포가 가능한 완전한 WAS
    - ※2018년 JavaEE는 오라클에서 이클립스 재단으로 이관된 후 Javarta EE 라는 새 이름을 받았다.
-  기본 흐름이나 구조가 정해져있기 때문에 개발자들의 실력의 차이를 좁힐수있고 의사소통이 효율적이다. 반쯤 완성한 상태에서 필요한 부분을 조립하는 형태의 개발. 개발자가 다루기 어려운 저수준의 기술에 많은 신경쓰지 않도록 해줌
- 스프링이 살아남은 이유
  - 기존 EJB로 대표되는 복잡한 프레임워크에 반기를 들며 등장한 경량화된 프레임워크
  - 특정 한 분야가 아니라 전체 구조를 다루는 프레임워크이므로 다른 프레임워크를 포용하여 혼용사용 가능
  - 개발 생산성과 개발도구의 지원
- 스프링 공부
  - 스프링컨테이너(애플리케이션 컨텍스트)를 다루는 방법과 설정정보를 작성하는 방법을 익혀야한다.
  - 기본구조가 만들어져있는것을 사용하는것이기 때문에 **설정이 반**이다.
  - 스프링을 사용한다는것은 다음3가지를 적극적으로 사용해서 애플리케이션을 개발한다는 뜻이다.
    1. 애플리케이션의 기본틀(스프링 컨테이너)
    1. 공통 프로그래밍 모델 (IoC/DI, 서비스추상화, AOP)
    1. 기술 API
---
1. # 개발환경 설치
    - JDK11 //windows 64bit installer
    - IntelliJ 또는 STS (무료버전에서는 스프링 연동 안된다)
    - tomcat
1. # 개발할때 지향해야할 방향
    - 느슨한 결합(약한 의존성) 나를 바꿀때 다른놈을 안바꿔도 되도록. 인터페이스의 사용.

    - 높은 응집도. 관심사들끼리 묶이도록.
1. # 스프링강의
  - [T아카데미](https://www.youtube.com/playlist?list=PL9mhQYIlKEhfYqQ-UkO2pe2suSx9IoFT2)
  - [T아카데미  Honeymon](https://www.youtube.com/watch?v=26GuwzdB3iI)
  - [뉴렉처](https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFWxnsrMu5kS_jt_o8gpEiTR)
  - [Kenu Heo](https://www.youtube.com/playlist?list=PLDMPhWe3CfpY9idK7tGd8QKr36KBID58P)
  - 김지헌님. 특히 스프링부트
  - 토비
  - 김영한님(배민 개발팀장) 스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술
  - 백기선
1. # 스프링
  - ### 스프링의 핵심철학
    객체지향 프로그래밍이 제공하는 폭넓은 혜택을 누릴 수 있도록 기본으로 돌아가자. 그래서 가장 관심을 많이 두는 대상이 '오브젝트'. 오브젝트의 생성, 다른오브젝트와 관계, 사용, 소멸 까지의 전과정을 진지하게 생각해볼필요가 있다. 나아가 어떻게 설계되어야 하는지.
    그래서 재활용 가능한 설계방법인 디자인패턴, 리팩토링, 단위테스트 같은 여러가지 응용기술지식이 요구된다.
  - 2004년 3월 1차버전 출시 이후 20여년동안 자바 엔터프라이즈 어플리케이션 개발 부동의 1위 프레임워크
  - 20여가지의 모듈이 있고 필요한것만 선택하여 사용가능. (부트, 클라우드, 데이터, 배치, 시큐리티가 주요한 모듈)
  - 스프링의 탄생배경 : 테스트 용이성, 느슨한 결합
  - #### 복잡성을 다루기 위한 스프링의 전략
    - 비지니스 핵심코드와 엔터프라이즈 기술을 처리하는 코드를 분리
    - POJO와 함께 스프링3대 핵심기술을 사용
    - 이 전략이 효과적으로 적용되려면 반드시 좋은 객체지향 설계가 바탕이 되어야한다.

- #### POJO
  - Plain Old Java object.   2000년 마틴파울러가 컨터런스 준비과정에서 만든 용어
  - 객체지향적 원리에 충실하고 특정 환경에 종속되지 않게 재활용될수있는 방식으로 설계된 객체
  - 객체에 애플리케이션의 핵심 로직을 담아 설계, 개발하는 방법을 POJO 프로그래밍이라 한다.
  - 자동화된 테스트에 유리하며 유지보수성이 높다.


---
1. ### 컨테이너
객체들을 담는 용기. 스프링 빈들의 생면주기를 관리한다.

---
### 스프링  vs  스프링부트
스프링부트 : 스프링의 확장판.
스프링부트는 어노테이션 기반으로 작동. @SpringBootApplication이 스프링부트의 마법이 시작되는 곳.
2014.04.01 스프링부트1.0 출시
2018.03.01 스프링부트2.0 출시
스프링2.5 : 어노테이션 도입
스프링3.0 : 별도설정없이 자바클래스만으로 설정 파일 대신
스프링4.0 : 모바일환경과 REST방식의 컨트롤러 지원
스프링5.0 : 리엑트 스타일의 개발 환경 지원
pivotal이 스프링부트의 개발을 주도하는 업체
- 스프링부트의 특징
  - 단독실행 가능한 스프링 애플리케이션 생성
  - 내장 컨테이너로 톰캣, 제티, 언더토우 중에서 선택가능
  - 스타터를 통해 간결한 의존성 구성 지원
  - 스프링에 대한 자동구성 제공
  - 더이상 xml구성이 필요없음
  - 제품출시후 운영에 필요한 다양한 기능을 제공
- 스프링부트의 구성요소
  - 빌드툴(gradle vs maven)
  - 스프링 프레임워크(4점대 vs 5점대)
  - 스프링부트(1.5 vs 2.0)   2019년 8월부터 1.5업그레이드 중지
  - 스프링부트 스타터(의존성 구성이 매우 쉬워진다.)

---
## 컨트롤러, 서비스, DTO, DAO
![MVC흐름](이미지/MVC흐름.png)
- 컨트롤러
사용자의 요청을 누가 처리할지 결정하는 파트

- 서비스
요청을 어떻게 처리를 할지 결정하는 파트

- DTO
Data Transfer Object
계층간의 데이터 교환을 위한 Java Bean (프로세스와 데이터베이스간의 데이터를 운반하는 객체)

- DAO
Data Access Object
DB에 접근하기 위한 객체
---
# 프로젝트 실행 구조
프로젝트 구동시 관여하는 33개의 설정파일.
- web.xml
    톰캣구동과 관련된 설정. 프로젝트가 구동할때 제일 처음 참조함
    <context-param>에는  root-context.xml의 경로 설정
    <listener>에는 ContextLoaderListener가 등록되어있다.
- root-context.xml
    처리되면 빈 설정들이 동작한다.(스프링의 영역안에서 라이프사이클을 가지고 의존성이 처리된다)
- servlet-context.xml
    내부적으로 웹 관련 처리의 준비작업을 진행
---

1. ## 스프링 특징3가지
- ## IoC/DI  (생성과 제어)
    - #### IoC. Inversion of Control. 제어의 역전
        스프링에서는 일반적으로 객체를 new로 생성하지 않고 컨테이너에게 맡긴다.
        즉, 개발자가 하던 객체의 관리를 프레임워크(엄밀하게는 컨테이너)가 대신 해주는것. 이것이 바로 IoC컨테이너.
        ![스프링ioc](스프링IoC.png)
        - 우리가 조립컴퓨터를 맞출때 cpu는 어디꺼 어느제품, 그래픽카드는 어디꺼 어디제품 다 정해서 명세서를 넘겨주면 조립업체에서 주문해서 조립해주듯이 명세서를 넘기면 객체를 생성해서 조립해서 컨테이너에 담아준다.
        작은부품이 먼저 만들어야지 큰부품을 만들때 끼워넣을수있다.
        - 일반적인 개발
        main()메소드와 같이 프로그램이 시작되는 지점에서 사용할 오브젝트를 결정하고,
        결정한 오브젝트를 생성하고
        만들어진 오브젝트에 있는 메소드를 호출하고
        그 메소드안에서 다음에 사용할것을 결정하고 호출하는 식의 작업이 반복된다.
        그러나 제어의 역전이란 이 흐름의 반대.
        오브젝트가 자신이 사용할 오브젝트를 스스로 선택하지 않는다. 당연히 생성하지도 않는다.
        또 자신도 어떻게 만들어지고 어디서 사용되는지 알 수 없다.
        모든 제어 권한을 자신이 아닌 다른 대상에게 위임하기 때문이다.

        그것이 바로 역전이다. 조립까지 된다는것을 표현하고싶어서 IoC라는 말이 되었다.
        스프링은 IoC를 기반기술로 삼아 극한까지 적용하고있는 프레임워크다.
        사실 **프레임워크**라는것이 자체가 제어의 역전 개념이 적용된 대표적인 기술이다.
        프레임워크는 단지 미리 만들어둔 반제품이나 확장해서 사용할 수 있도록 준비된 추상 라이브러리의 집합이 아니다.
        라이브러리는 우리 코드가 라이브러리를 제어하고,
        프레임워크는 프레임워크가 우리 코드를 제어한다.

        IoC를 적용하면 설계가 깔끔해지고 유연성이 증가하며 확장성이 좋아진다.

    - #### DI. Dependency Injection. 의존관계 주입.
      - IoC컨테이너에서 빈 객체를 생성하는 방식. IoC를 구현하는 대표적인 원리.
      - 쉽게 설명
        의존을 부품이라고 생각하면된다. 스프링은 일체형부품을 조립형으로 만든것이 큰 특징이라는 것이다.
        느슨한 결합으로 부품만 갈아끼울수 있도록. A입장에서는 B가 부품이다. 부품객체를 디펜던시라고 하고, 꽂아주는것을 주입이라고 하는것이다.
        예를들어
        ```java
        A a = new A();
        방식에서

        B b = new B();
        A a  = new A();
        a.setB(b);
        방식으로 만든것.
      - 더쉽게 설명하면 음식점에서 직접 식재료를 사지않고 대행업체에서 배송해주는것을 사용하는 경우에 얻는 장점이 무엇인가?를 생각해보면 편리하다, 장사에만 집중할 수 있다. 즉 주입을 받는 입장에서는 타입만 맞으면 어떤 객체인지 신경 쓸 필요가 없다, 자신의 역할은 변하지 않는다.
      - 어려운 예제
        - DI없을때
        ```java
        @restcontroller
        public class mycontroller {
            private myservice service = new myservice();

            @requestmapping("/welcome")
            public string welcome() {
                return service.retrievewelcomemessage();
            }
        }
        ```

        - DI 있을때
        ```java
        @component
        public class myservice {
            public string retrievewelcomemessage(){
               return "welcome to innovationm";
            }
        }


        @restcontroller
        public class mycontroller {

            @autowired
            private myservice service;

            @requestmapping("/welcome")
            public string welcome() {
                return service.retrievewelcomemessage();
            }
        }
        ```

      - 장점 : 부품을 쉽게 바꿀수 있음
      - 단점 : 부품을 조립해야하는 불편함
        조립해주는 서비스를 이용하면 편하겠지. 그것이 바로 스프링
        어떤 부품이 필요하고 어떻게 결합하기를 원하는지 설정만 해주면 알아서 조립해준다.
      ```
      - 방법3가지
        - 수정자 주입 : Setter
        - 생성자 주입 : final사용가능. 레퍼런스 변경되지 않음
        - 필드 주입 :
      - **의존성**이 사라짐 : 추상화, 코드 테스트에 용이, 순환참조 방지
      -   **생성자**로 주입해주나?


- ## AOP
Aspect Oriented Programming. 관점 지향 프로그래밍
스프링 어플리케이션은 대부분 MVC모델을 사용하기 때문에 WEB, Business, Data 3개의 레이어로 정의된다.
'횡단 관심' 공통적인 기능
- 주요 어노테이션
  - @Aspect : AOP를 정의하는 Class에 할당
  - @Pointcut : 기능을 어디에 적용시킬지.
  - @Before : 메소드 실행하기 이전
  - @After : 메소드가 성공적으로 실행후 예외가 발생되더라도 실행
  - @AfterReturning : 메소드 호출 성공 실행시
  - @AfterThrowing : 메소드 호출 실패 예외 발생
  - @Around : before / after 모두 제어
- 글로보면 이해하기 어렵지만 소스를 보면 쉽게 이해한다.
- dependency 추가해줘야한다.

- ## PSA
    - Portable Service Abstraction
    다른 기술스택으로 간편하게 바꿀수있는 확장성을 갖고 있는 추상화
    - 즉, 하나의 추상화로 여러 서비스를 묶어둔 것
    환경의 변화와 관계없이 일관된 방식의 기술 접근 환경을 제공하려는 추상화 구조
    - 예)
    원래 톰캣으로 실행되던 프로젝트를 Spring Web MVC 추상화 계층을 사용하면 netty기반으로 간단하게 바꿀수있다.
   - 원리
   추상화와 DI주입

---
# ApplicationContext
- 스프링 애플리케이션 전반에 걸쳐 모든 구성요소의 제어를 담당하는 IoC엔진
- 스프링은 기본적으로 별다른 설정을 하지않으면 내부에서 생성하는 빈 오브젝트를 모두 싱글톤으로 만든다.
---

1. # Annotation (어노테이션)
    - 프로그램에게 추가정보를 제공해주는 메타데이터
    - 역할
        - 컴파일러에게 문법 에러 체크
        - 빌드나 배치시 코드를 자동 생성
        - 런타임에 특정 기능을 실행
    - 종류
        - ### @ComponentScan (**중요**)
            - @Component, @Service, @Repository, @Controller, @Configuration이 붙은 클래스 Bean들을 찾아서 Context에 bean등록.
            - 해당 애노테이션을 갖는 클래스가 무엇을 하는지 단 번에 알 수 있다
        - ### @Component (**중요**)
            - 개발자가 직접 작성한 클래스를 빈으로 등록. 1개의 Class단위로 등록할때 사용
        - ### @Bean (**중요**)
            - 개발자가 직접 제어가 불가능한 외부 라이브러리등을 Bean으로 만들때 사용
        - ### @Configuration (**중요**)
            - xml대신 클래스의 인스턴스를 활용해서 설정파일을 대신한다. 1개이상의 bean을 등록할때 설정
        - ### @Autowired (**중요**)
            - 속성(field), setter method, constructor(생성자)에서 사용하며 Type에 따라 알아서 Bean을 주입
            - Controller 클래스에서 DAO나 Service에 관한 객체들을 주입 시킬 때 많이 사용. 즉 DI가 목적
            - Type을 먼저 확인후 못찾으면 Name에 따라서 주입
        - ### @Inject (**중요**)
            - Autowired와 비슷한 역할
        - ### @Controller (**중요**)
            - 해당클래스가 스프링의 컨트롤러임을 나타냄. 뷰를 제공한다.
        - ### @RestController (**중요**)
            - View로 응답하지 않고 Rest API를 제공하는 컨트롤러로 설정
            - method의 반환 결과를 JSON 형태로 반환
        - ### @RequestMapping (**중요**)
            -  해당요청(URL)을 어떤 컨트롤러나 메서드가 처리할지 매핑해줌
        - ### @GetMapping (**중요**)
            - Http GetMothod Url을 받아 화면 반환.
        - ### @PostMapping (**중요**)
            - Http PostMothod Url을 받아화면 반환.
        - ### @RequestParam (**중요**)
            -  컨트롤러 메소드의 파라미터와 웹요청 파라미터를 매핑해줌
        - ### @RequestBody (**중요**)
            -  Http Body를 Parsing 매핑
        - ### @ModelAttribute (**중요**)
            - 컨트롤러 메소드의 파라미터나 리턴값을 Model객체와 바인딩해줌
        - ### @SessionAttributes
            - Model객체를 세션에 저장해줌
        - #### @PathVariable
            - URL 경로에 변수를 넣어줌. {템플릿변수} 와 동일한 이름을 갖는 파라미터를 추가해주면 된다.
            - 예
            ```java
            @RequestMapping(value = "/user/email/{email}", method=RequestMethod.GET)
            이런 형식일때 아래와 같이 바꿔주면 제대로 들어옵니다.
            @RequestMapping(value = "user/email/{email:.+}", method = RequestMethod.GET)
            public ModelAndView getUserByEmail(@PathVariable("email") String email) {
            ```
        - ### @SpringBootApplication (**중요**)
          - 스프링부트어플리케이션으로 설정

        - ### @Qualifier
            - 오토와이어드 사용시 bean이 2개이상일때 스프링이 무엇을 선택할지 명시적으로 알려주기 위해 사용
        - ### @Resource
            - @Autowired + @Qualifier의 개념

1. ## Bean( # 빈)
  - 디폴트 생성자와 getter, setter메소드가 있는 오브젝트를 말한다.
  - 스프링 IoC컨테이너가 관리하는 객체
  - 스프링이 제어권을 가지고 생성하고 의존관계를 부여하는 오브젝트
  - 등록법
    1. 어노테이션
      @Component, @Repository, @Service, @Controller, @Configuration,
    1. 직접 또는 xml같은설정파일
      @Configuration안에서 @Bean
  - 사용법
    1. 어노테이션
      @Autowired, @Inject
    1. 직접
      ApplicationContext에서 getBean()으로
---


---
# 스프링의 기능 활용
1. Validation
어노테이션으로 검증할수 있다.
@Size, @NotNull, @NotEmpty, @NotBlank, @Past, @Future, @Max, @AssertTrue, @Valid, @Pattern 등이 있다.

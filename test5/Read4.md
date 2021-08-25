웹(서비스)환경
웹서버Sofware - Apache(WS)+Tomcat(WAS) <-Java

Database(Oracle/MySQL)
서버(JAVA,Spring,PHP,Django)
클라이언트(HTML/CSS/Javascript/jQuery)

Server(Apache+Tomcat)

Internet

Client

sts 스피링 툴 슈트
spring tool suites

spring3
spring4 -> spring Boot

---------------------------------------------

MVC (Model View Controller)


<body> <!-- View (보이는 부분) -->
    <input type=button id=btnGO>  <!-- id= Model (중간에 접점) --> 
</body>
<script> <!-- Control -->
</script>

@RequestMapping(value = "경로명", method = RequestMethod.GET)
	public String 메소드이름( Model m) {		
		m.addAttribute("변수명1", "값1");		
		return "JSP화일이름";  //home    .jsp생략
	}

home.jsp에서
 <body> 
    ...${변수명1}
</body>   

기본경로명(http//localhost:8081/프로젝트이름)+"/경로명"
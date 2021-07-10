- git config --local user.name ""
- git config --local user.email "" 

- git: fatal: No configured push destination 에러 나올 시 해결 방안
  https://www.python2.net/questions-246949.htm 

- Decorater 꾸며서 새로운 함수
- 통합 개발 환경(Integrated Development Environment, IDE)

- 제어의 역전 https://madplay.github.io/post/spring-framework-basic-inversion-of-control

#### 20210710(토) 작업
- 클래스
- STS = Spring Tool Suite

#### 20210703(토) 작업
- 변수사용범위(scope)
- from 모듈명 import 내가 사용할 함수 as 별칭
- 
- sys 모듈의 argv 
- 지점이 많은 커피숍관리 프로그램일때,
- 명령프롬프트에서 python a.py 지점명
- argv = ['a.py','지점명']
- print('coffee숍 관리', argv[1])
- 지점명의 파라미터를 가져온다.
- 1970.1.1.0.0.0 이 기본시간 매초마다 1000씩 증가
- 스티브잡스가 표준시간을 정의하였으며, 추후 빌게이츠가 IBMPC에 표준시간을 적용

- 자바 스크립트 : setTimeout(함수, 시간(1000분의 1))-5초 뒤 실행, setIntervel 
- 파이썬에서는 time모듈을 import해서 time.sleep(5) 이렇게 써준다.
- 다른 pc의 파일을 열고싶을 때,import urllib 후 urlopen(인터넷주소)
- 크롤링
- f = urllib.urlopen("http://아마존사이트")
- f.read() 
- 
- if __name__ == '__main__':
- 
- 객체지향 특징 : 캡슐화, 상속, 다형성, 추상화

#### 20210626(토) 작업
- 함수 = 사용자 정의 함수, 내장 함수(print,input,int 등....)
- 재귀함수 = 자기 자신 안에서 자기 자신을 호출하는 함수.
- 
- 트리구조 (게시판, 회사 DB테이블 예시(셀프조인))
- 
- 파일 열기 (open), file = open("d/menu.txt", "w"), "a", "r"
- with open("d/menu.txt", "w") as file: (with문은 close가 필요없다.)
- 예외처리 (file, network, index 등등)
- try(실행될 코드), catch(예외처리 부분), else(실행성공시 후처리), finally(무조건 실행되는 코드)
- 파일 읽기 https://wikidocs.net/26
- 
- 모듈 : 표준모듈, 외부모듈(pip install), 사용자 정의 모듈
- 표준 모듈 - python 설치할 때, 설치되는 모듈(Math, random, sys(하드웨어), os, datetime, time, urllib)
-  ceil(2.5) = 3, floor(2.5) = 2

#### 20210619(토) 작업
- 튜플 () 
- 인덱스에 접근할 수 있다. - 리스트와 동일
- update 연산 불가, 값을 바꿀수가 없다.
- 
- 세트{} 중복X, 순서X, 인덱스 접근 불가, 집합 연산만 가능
- a = set()
- 합집합 |, 교집합 &, 차집합 - 
- a.add(9), a.update([1,3,4,5]), a.remove(값)
- 
- 딕셔너리 {} key와 value가 한쌍, 키는 중복을 허용하지 않는다.
- a["name"] 키값으로 value 가져오기
- 
- 함수


#### 20210612(토) 작업
- 0과 빈문자열""은 false로 취급
- if a = None: // 파이썬에서의 None은 None = null과 같다. 그래서 false
- 
- 파이썬에서 중요한 자료구조 4가지
- 리스트 = 배열과 같은 개념 / 
- 리스트에서 연속적으로 인덱스 값 가져오기 : a[0:3] = a의 리스트의 0~2까지의 인덱스값 가져오기, a[3:] = a의 리스트의 3인덱스부터 끝인덱스까지의 값 가져오기. 반대 a[:3](처음부터 2번째까지)
- 리스트의 값 지우기 : del 리스트[인덱스번호), 리스트.pop(인덱스번호), remove(인덱스 번호가 아니라 value값), 리스트.clear() 모든값을 삭제
- list for문 실습
- while문
- Terminology(전문용어)를 많이 써야한다.


#### 20210605(토) 작업
- 문자열
- 비교연산(==,<,<=,>=,>,!=), 논리연산(and, or, not), Boolena(True, False)
- http://3.134.55.142/ncs/ncs.php?class=ncs6&name=임은비
- if 문 


#### 20210529(토) 작업
- 키워드 : 각 언어에서 쓰이는 예약어 (예 : 자바 - String, int, abstarct, class, return 등등)
- 식별자 : 변수, 클래스, 함수 이름을 만들 때 사용하는 단어 (처음에 영문자, _, 시작 가능함. 이름에 숫자와 공백, 특수문자는 안됨)
- 연산자(operator) : 사칙연산 2 + 3, 5 - 3, 5 * 3 (*: asterisk, @: at, circle A), 5 / 3, 2 ** 3 (거듭제곱), x = 3 (배정 연산자)
- 프로그램 실행은 -> 순차적(sequential) 


- 언어의 족보
- 포트란(미국 나사가 아폴로 착륙시킬 때 쓴 언어) -> C -> C# -> java(C#의 장점을 많이 받음 (sunmicro 1995) -> javascript -> jquery
- 파이썬은 C#의 영향을 많이 받음 (java와 경쟁하지만 아직까지는 많이 밀림 )
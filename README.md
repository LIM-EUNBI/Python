- git config --local user.name ""
- git config --local user.email "" 

- git: fatal: No configured push destination 에러 나올 시 해결 방안
  https://www.python2.net/questions-246949.htm 

- Decorater 꾸며서 새로운 함수

#### 20210619(토) 작업
- 튜플 () 
- 인덱스에 접근할 수 있다. - 리스트와 동일
- update 연산 불가, 값을 바꿀수가 없다.
- 
- 세트() 중복X, 순서X, 인덱스 접근 불가, 집합 연산만 가능
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
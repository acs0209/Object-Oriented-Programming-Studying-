# 변수, 함수, 클래스를 쓰는게 추상화를 쓰고 있는거다
# list클래스를 쓰는것과 같이 클래스의 내부 내용을 몰라도 클래스를 사용하기 위한 최소한의 정보만 알면
# 클래스를 잘 사용할 수 있다 다 추상화덕분인거다 
# 추상화 잘하는법
# -> 클래스, 변수, 메소드 이름 잘짓기
# 하지만 이름을 잘짓는거에는 한계가 존재 그래서 """""""을 사용하여 문서화를 이용한다

# help() -> 어떤 클래스의 코드를 직접 보기 전에 docstring만 보고 싶으면 help함수를 사용하면 된다
help(list)

# 09. 여기서 잠깐! 파이썬의 type hinting
# 파이썬은 동적타입 언어이다 이 말은 변수의 타입을 따로 정하지 않아도 된다는거다
# 타입 힌팅(Type Hinting) 파이썬에서도 정적 타입 언어처럼 타입을 표시할 수 있는 기능이다
# 타입 힌팅을 지키지 않아도 실행자체에는 에러가 나지 않는다 타입 힌팅은 실행에 직접 영향을 주지 않지만
# 개발자들이 변수, 메소드 등을 사용할때 어떤 값을 넣거나 읽을 수 있는지 빨리 파악하도록 도움을 준다


#추상화란 클래스나 함수의 작동 원리를 세세하게 표현하지 않고,
#공통적으로 필수적인 내용만 골라서 표현하는 것을 의미합니다.
#캡슐화는 클래스의 내부 속성을 말 그대로 숨겨서 외부에서 접근하지 못하게 막는 것입니다.
#자동차의 예를 들면,
#(1) (엑셀의 작동 원래를 세세하게 설명하지 않고) 엑셀을 밟으면 차가 앞으로 간다 -> 추상화
#(2) 자동차 속도 관련 소프트웨어에 보안을 걸어 소프트웨어를 조작하지 못하게 한다 -> 캡슐화
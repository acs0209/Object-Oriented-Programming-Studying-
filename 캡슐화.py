class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        """주민등록번호를 읽거나 설정하는 메소드가 아니다 그냥 주민등록 번호를 기준으로 본인이 맞는지 인증하는 메소드다"""
        return self._resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self._age) + "살입니다!"

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        """변수의 값을 읽는 메소드 -> getter 메소드"""
        return self._age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        """변수의 값을 설정하는 메소드 -> setter 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정 하겠습니다.")
            self._age = 0
        else:
            self._age = value


# 04. 객체의 메소드를 통해 변수 접근하기 I
# Citizen 클래스의 __age변수에 바로 접근할수는 없다 하지만 can_drink, get_age, set_age 메소드를 통해서
# 접근할 수 있다. 이렇게 외부에서 직접 접근이 불가능한 변수에 대해 접근할 수 있는 메소드를 만드는 것이
# 캡슐화의 두 번째 정의를 적용하는 방법이다 캡슐화의 두번째 정의는 객체의 속성과 그것을 사용하는 행동을
# 하나로 묶는것인데 하나로 묶는다는게 무슨 말일까 지금 Citizen클래스에서 변수 __age는 can_drink,get_age,set_age
# 메소드를 통해서만 사용이 가능하다 이렇게 변수에 접근하는 통로를 메서드로 제한하는 것을 속성과 행동을 하나로 묶는다고 하는거다

# 05. 객체의 메소드를 통해 변수 접근하기 II
# 변수의 값을 읽는 메소드 -> getter 메소드
# 변수의 값을 설정하는 메소드 -> setter 메소드 

# 캡슐화를 할때 숨긴 변수에 대해서 getter, setter메소드를 꼭 만들어야 하는건 아닙니다
# 어떤 변수냐에 따라서 다른식으로 변수를 사용하는 메소드만 만들어 주는 것도 괜찮습니다.
# 지금 __resident_id변수에 관해서는 authenticate메소드만 있는 것 처럼요

# 외부에서 직접 접근이 불가능한 변수에 대해 접근 할 수 있는 메소드를 만드는 것이 캡슐화의 2번째 정의를 적용하는거다
# authenticate함수와 같이 캡슐화를 할때 숨긴 변수에(여기서는 __resident_id) 대해서 getter,setter메소드를 
# 꼭 만들어야 하는건 아니다.
# 어떤 변수냐에 따라서 다른식으로 변수를 사용하는 메소드만 만들어 주는 것도 괜찮다

# 캡슐화 정리
# 1. 클래스 밖에서 접근 못하게 할 변수, 메소드 작성하기
# 2. 변수나 메소드 이름 앞에 언더바 2개 붙이기
# 3. 변수에 간접 접근할 수 있게 메소드 추가하기
# 보통 변수의 값을 읽는 getter메소드, 변수의 값을 설정하는 setter메소드를 추가해 준다. 또는 __resident_id처럼
# 변수에 따라서는 getter,setter메소드가 아닌 다른 용도의 메소드만 추가해줘도 된다.



# 09. 데코레이터를 사용한 캡슐화
# 메소드 이름 위에 @property라고 쓰면 그 메소드를 어떤 변수에 대한 getter메소드로 만들 수 있습니다.
# @이를 쓰고 getter메소드의 이름을 쓰고 .을찍고 setter라고 쓰면( -> @age.setter) 이껄 어떤 메소드의 이름 위에 쓰면
# 그 메소드를 어떤 변수에 대한 setter메소드로 만들 수 있습니다.
# 데코레이터를 쓰고 나면 young.age라는(월래 age라는 변수를 가져오는) 구문의 의미가 변합니다.
# 바로 같은 이름을 가진 age메소드를 실행하라는 뜻이 된다.
# 또한 young.age = 30(월래 age변수에 값 30을 설정 하는) 의미가 바뀐다 함수위에 데코레이터가 붙는다면 
# age라는 이름의 setter메소드를 실행하라는 뜻으로 바뀝니다 그리고 이때 value파라미터로 30이 전달 된다

# property 데코레이터: 변수의 값을 읽거나 설정하는 구문 -> 아예 다른 의미로 실행
# property 데코레이터: 캡슐화 전 사용하던 코드를 캡슐화 후 수정X 
# 주민 인스턴스 생성
young = Citizen("younghoon kang", 18, "980322-1234")

print(young.__str__()) # 출력: younghoon kang씨는 18살입니다!
print(young.authenticate("980322-1234"))
print(young.can_drink())
print(young.get_age())
young.set_age(30)
print(young.get_age())

young.set_age(-10)
young.set_age(19)
print(young.get_age())
#print(young.__age)
#print(young.__authenticate("87654321")) # 에러가 난다!!!
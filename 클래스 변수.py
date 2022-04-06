# 11. 클래스 변수 1
# 인스턴스 자신만의 속성을 나타내는 인스턴스 변수를 배웠다.
# 그런데 여러 인스턴스들이 공유하는 속성이 있을 수 있다.
# 특정 인스턴스가 갖고있는 값이 아니라 서로 공유하고 있는 값이다.
# 어떤 인스턴스라도 똑같은 값을 가지고 있어야 하는 것이다 파이썬에서는 이런 속성을 클래스 변수라는 걸로 나타낸다
# 클래스 변수는 같은 클래스의 인스턴스들이 공유하는 값이다

class User:
    count = 0
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해 주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1 # 지금 count는 클래스 변수이다. 그래서 클래스 변수는 클래스명.변수 로 접근을 해줘야 한다.
#User.count = 1
#print(User.count)

user1 = User("강영훈", "yoong@naver.com", "123123")
user2 = User("이윤수", "qwe@naver.com", "1234")
user3 = User("서혜린", "qwezxc@naver.com", "123abc")

print(User.count)
User.count = 5
print(User.count)

# 12.클래스 변수 2
# 클래스 변수의 값을 읽거나 설정하는 방법을 알아보자
# 같은 이름의 클래스 변수가 있고 같은 이름의 인스턴스 변수가 있으면 인스턴스 변수가 읽어진다.
# 헷갈리고 꼬일 수 있기 때문에 클래스 변수에 값을 설정할때는 클래스 이름으로만 해야 한다

# 한 클래스의 모든 인스턴스가 공유하는 속성이라면 클래스 변수로 적으면 된다. 
# 그리고 클래스 변수의 값을 읽는 법은 1. 클래스 이름.클래스 변수 이름 2. 인스턴스 이름.클래스 변수 이름
# 하지만 클래스 변수의 값을 설정할때는 꼭 클래스 이름을 통해서만 해야 한다.

# 13. 데코레이터1
# 어떤 걸 꾸미는 걸 영어로 데코레이팅한다 라고 한다
# 파이썬에서는 어떤 함수를 꾸며서 새로운 함수로 만들 수 있다 이떄 사용하는게 바로 데코레이터 이다.

def print_hello():
    print('안녕하세요!')

def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

print_hello = add_print_to(print_hello)
print_hello()
# 지금 위에보면 우리는 add_print_to함수를 호출했다 근데 이 함수가 하는일이 뭔가 이 함수는 정의 했던 wrapper함수를 
# 리턴해주기만 한다 이 wrapper함수를 실행시키는게 아니라 이걸 리턴해주기만 하는거다 그래서 아무것도 출력이 되지 않는다
# 리턴된 wrapper함수는 호출한 부분에 그대로 들어가야 한다 리턴된 함수를 호출하기 위해서는 add_print_to(print_hello)에
# ()을 열고 닫아야 한다 add_print_to(print_hello)()이렇게 이걸 조금더 깔끔하게 고치고 싶다
# print_hello = add_print_to(print_hello) print_hello() 이렇게 하면 잘 출력된다 지금 add_print_to(print_hello)함수가
# 이제 새로운 함수를 리턴한다 그러니까 그 리턴된 함수를 다시 print_hello에 넣고 print_hello함수를 호출하는거다
# 정리를 해보면 우리는 add_print_to 함수를 정의했다 그런데 이 함수가 하는일이 뭐냐 이 함수는 파라미터로
# 어떤 함수를 받습니다. add_print_to가 하는 일은 파라미터로 받은 함수를 데코레이팅 즉 꾸며주는 거다
# 우리 대단한건 아니지만 앞뒤로 출력하는 코드를 추가했다 아무튼 이렇게 꾸며진 함수를 리턴시켜준다 다시 말하면 
# add_print_to는 어떤 함수를 받고 꾸며서 새로운 함수를 리턴해주는거다 그래서 이 함수는 다른 함수를 꾸며주는 역할이기에
# add_print_to함수를 데코레이트 함수라고 부른다.

# 14. 데코레이터2
# print_hello = add_print_to(print_hello) 보면 print_hello 함수를 꾸미기 위해서 add_print_to함수가 print_hello를 
# 꾸며주고 print_hello가 꾸며진 함수를 다시 가리키도록 하는거다 사실 이줄을 쓰지않고도 print_hello함수를 꾸밀수 있다
# print_hello() 함수위에 @add_print_to를 쓴다 이 뜻은 print_hello()함수를 add_print_to()로 꾸며주라는 소리다
# 이걸 쓰고나서 앞으로 print_hello함수를 호출하면 꾸며진 print_hello함수가 호출된다
def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

@add_print_to
def print_hello():
    print('안녕하세요!')

print_hello()
# 함수위에 @가 보이면 데코레이터구나 라고 생각해라 그리고 함수를 어떤 함수로 꾸며서 새로운 기능을 준다 라고 알면된다.
# 데코레이터 -> 기존의 함수에 새로운 기능 추가
classmethod
def function():
    # 함수 내용
    pass

# 15 
# 인스턴스 변수의값을 읽거나 설정하는 메소드 -> 인스턴스 메소드
# 클래스 변수의값을 읽거나 설정하는 메소드 -> 클래스 메소드
# 클래스 메소드는 메소드이름 위에 #classmethod라고 작성한다 클래스 메소드에는 꼭 알아야 할 규칙이 있다.
# 인스턴스 메소드는 첫번째 파라미터인 self로 인스턴스 자신이 자동 전달되는 규칙이 있어서 인스턴스 메소드는 self를 써줬다
# 클래스 메소드는 첫번째 파라미터로 클래스가 자동 전달된다 그리고 클래스를 cls라는 파라미터로 전달 받는다 

class User:
    count = 0
    
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해 주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저수는: {}입니다".format(cls.count))

user1 = User("강영훈", "yoong@naver.com", "123123")
user2 = User("이윤수", "qwe@naver.com", "1234")
user3 = User("서혜린", "qwezxc@naver.com", "123abc")

User.number_of_users()
user1.number_of_users()

# 인스턴스 메소드와 클래스 메소드의 차이점
# 인스턴스 메소드 사용
# User.say_hello(user1)
# user1.say_hello() -> 인스턴스 자신이 첫번째 파라미터로 자동 전달, 인스턴스를 통해서 인스턴스 메소드를 호출할때만 인스턴스 자신이 자동전달된다.
# 클래스 메소드 사용 -> 하지만 클래스 메소드는 2가지 방법 모두 첫 번째 파라미터로 클래스가가 자동 전달된다 클래스가 자동 전달 되는 이유는 @classmethod 데코레이터로 number_of_users를 클래스 메소드로 만들어 줬기 때문이다.
# User.number_of_users()
# user1.number_of_users()

# 클래스 메소드는 인스턴스마다 다른 행동을 하는게 아니라 같은 행동을 할 때 1번만 정의해서 
# 모든 인스턴스가 같은 행동을 하도록 하려고 사용합니다.


# 16.클래스 메소드2
# 인스턴스 변수 말고 클래스 변수만 사용하는 메소드라면 클래스 메소드로 작성해야 한다
# 클래스 변수를 사용할떄?
# 인스턴스 변수 사용 -> 인스턴스 메소드
# 클래스 변수 사용 -> 클래스 메소드

# 클래스 변수와 인스턴스 변수 둘 다 쓴다면?
# -> 인스턴스 메소드는 인스턴스 변수, 클래스 변수 모두 사용 가능 그래서 인스턴스 메소드를 사용한다.
# 인스턴스 변수는 self를 통해 클래스 변수는 그냥 클래스이름에 .을 붙여서 가져오면 된다.
# 하지만 클래스 메소드는 인스턴스 변수를 가져올 수 없다 클래스가 자동전달되는 cls를 통해 클래스 변수는 가져올 수 있지만
# 인스턴스 변수는 가져올 수 없어 사용불가다

# 인스턴스가 없을때도 필요한 정보가 있으면 꼭 클래스 메소드를 사용해야 한다 예를 들어 User클래스의 변수 count는
# user인스턴스가 하나도 없더라도 필요한 정보이다 user인스턴스가 없어도 count가 0개라는걸 출력해야 한다
# 즉 이말은 count변수를 사용하는 클래스 메소드 또한 user인스턴스가 하나도 없어도 필요하다 라는 소리다
# 인스턴스가 하나도 없을때에도 사용할 가능성이 있으면 클래스 메소드로 만들어야 한다
class User:
    count = 0
    
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해 주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users1(cls, string_params):
        print("총 유저수는: {}입니다".format(cls.count))

    @classmethod
    def number_of_users2(cls, list_params):
        print("총 유저수는: {}입니다".format(cls.count))


younghoon = User.number_of_users1("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.number_of_users2(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

info_string = "강영훈,younghoon@codeit.kr,123456"
info_list = ["이윤수", "yoonsoo@codeit.kr", "abcdef"]
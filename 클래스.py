#클래스의 맨처음은 대문자로 한다. 클래스를 설계도라고 생각하면 좋다
class User:
    #이 부분에 이제 속성과 행동을 작성할꺼다
    def say_hello(some_user):
        # 인사 메시지 출력 메소드
        print("안녕하세요 저는 {}입니다!".format(some_user.name))

    def login(some_user, my_email, my_password):
        # 로그인 메소드
        if (some_user.email == my_email and some_user.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

# 같은 클래스로 만들었어도 서로 다른 인스턴스다
user1 = User()#변수이름이 지금 user1이다 User()이 부분을 통해서 user인스턴스가 만들어지고 변수 user1이 User() 인스턴스를 가리키게 된다
user2 = User()
user3 = User()

# 변수 사용법은 name = "김대위"이다 user1인스턴스에 속성을 추가하고 싶으면 
# 인스턴스 이름.속성이름(인스턴스 변수) = "속성에 넣을 값"
#  user1         name                       "김대위"
user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"
# 이렇게 하면 user1 인스턴스에 이메일 속성과 비밀번호 속성이 생긴거다

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"
# 위를 보면 각 인스턴스는 같은 이름의 속성을 가지고 있어도 서로 다른 값을 가지고 있다.
# 즉 user1,user2,user3가 속성을 공유한게 아니라 각자 개인적으로 가지고 있는거다 이렇게 인스턴스가 개인적으로 
# 갖고 있는 속성을 인스턴스 변수라고 한다 name,email,password 모두 인스턴스 변수이다.

# 인스턴스 변수 사용 -> 인스턴스 이름.인스턴스 변수이름
print(user1.email)
print(user2.password)
# 인스턴스 변수를 사용하려면 꼭 그전에 미리 정의해 놔야 합니다.

# 객체는 속성과 행동으로 이루어져 있다. 파이썬에서는 속성을 인스턴스 변수로 나타낸다. 그러니까 변수로 속성을 나타낸거다.
# 파이썬에서 행동은 함수로 나타낸다. 클래스 안에 함수를 정의하면 객체의 행동을 정의한거다. 이렇게 객체의 행동을 나타내는
# 함수를 특별히 메소드 라고 부른다.그러니까 클래스 안에 함수를 정의하면 메소드를 정의했다 라고 할 수 있다.

# 메소드에는 크게 3가지 종류가 있다. 1.인스턴스 메소드 2.클래스 메소드 3.정적 메소드 
# 인스턴스 메소드는 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드 이다.

# 인스턴스 메소드
# 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정한는 메소드

# 인스턴스 메소드 사용법 -> 클래스 이름.메소드 이름(인스턴스)
User.say_hello(user1)
# 인스턴스 메소드를 사용하는 또 다른 방법 -> 인스턴스 이름.메소드 이름()
user1.say_hello()
# 그런데 자세히 보면 좀 이상함 say_hello 메소드를 보면 some_user라는 파라미터를 넘겨줘야 하는데 우리는 
# 파라미터를 넘겨주지 않았는데 에러가 안났다 왜 에러가 안날까 그건 인스턴스 메소드의 특별한 규칙때문이다.
# 윗줄은 클래스에서 메소드를 호출했고 아래줄은 인스턴스에서 메소드를 호출했다. 인스턴스에서 메소드를 호출하면
# 이 user1인스턴스가 say_hello()의 첫번째 파라미터로 자동으로 전달된다. 즉 파라미터를 따로 써줄 필요가 없다.
# 이 윗줄과 아랫줄은 다르게 보이지만 완전히 똑같다 

user1.login(user1, "captain@codeit.kr", "12345")
user1.login("captaincodeit.kr", "12345")
# 둘중에 아래가 맞다 왜냐면 아래 방법을 쓰면 user1이 자동으로 전달되기 때문이다


# self를 만들어 봅시다
# 이전 영상에서 인스턴스 메서드의 특별한 규칙을 설명했다. 인스턴스 메서드를 호출하면
# 인스턴스가 메소드의 첫번째 파라미터로 자동 전달되고 그러니까 인스턴스 메서드를 정의할때는
# 항상 첫번째 파라미터로 인스턴스를 받기 위한 파라미터를 써줘야 한다 우리는 그 파라미터의 이름을
# some_user라고 지어준거다 그런데 우리가 앞으로 지켜야할 규칙이 하나 있다. 
# 파이썬에서는 인스턴스 메서드의 첫번째 파라미터 이름을 self로 쓴다고 가정한다.
# 인스턴스 메서드를 호출하는 인스턴스 자신이 첫번째 파라미터로 들어가니까 self라는 단어가 굉장히 어울린다
# 첫번째 파라미터를 self로 써주면 주인공이 항상 self라는거를 알기때문에 훨씬 읽기 편한 코드가 된다.
# 사실 self말고 다른 단어를 써도 실행하는데 아무런 지장이 없다 하지만 이건 파이썬 세계의 약속이다
# 그래서 인스턴스 메소드의 첫번째 파라미터는 self로 써야 한다



class User:
    # initialize 메소드를 여기 쓰세요
    def initialize(self, name, email, password):
        self.name = name # -> 인수턴스 변수와 파라미터의 이름이 둘다 name이다 이래도 되는걸까? 사실 이 코드는 아무런 문제가 없다. 
                         # name하나는 그냥 이 함수내에서 사용하는 값이다 다른 하나는(self.name) self의 name이다 그러니까
                         # 어떤 인스턴스가 갖고 있는 인스턴스 변수 name이다. 그냥 name과 self.name은 구분히 확실하기 때문에
                         # 이렇게 작성해도 아무런 문제가 없다. 심지어 이런식으로 작성하는게 꽤나 일반적이다.
        self.email = email
        self.password = password        
        
        return self.name, self.email, self.password
    
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")


def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    # 위에는 인스턴스 변수들의 초깃값을 설정한거다 그러니까 결국 __init__ 메소드를 사용하면 인스턴스 생성과
    # 인스턴스 변수 초깃값 설정을 한줄에 할 수 있다. 이런 장점때문에 클래스에는 보통 __init__메소드를 꼭 작성한다.

# 특수 메소드는 양 옆으로 _가 2개씩 있으니까 double underscore 줄여서 dunder메소드라고 부른다. 그래서 __str__을 던더 에스티알이라고 부른다
# __str__(던더 -> __  __) 메소드는 print()함수를 호출할때 자동으로 불립니다. 쉽게 얘기해서 어떤 인스턴스를 출력하면
# __str__에 있어야할 메소드의 리턴값이 출력된다는 거다.
# 인스턴스를 출력할때 우리가 원하는 정보를 나오게 할려면 class에 던더 str 메소드를 정의하면 됩니다.




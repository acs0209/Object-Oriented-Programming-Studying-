# 캡슐화 전
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        """주민등록번호를 읽거나 설정하는 메소드가 아니다 그냥 주민등록 번호를 기준으로 본인이 맞는지 인증하는 메소드다"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"

#young = Citizen("kang", 19, "980322")
#print(young.age)
#young.age = 30
#print(young.age)

# 캡슐화 후
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        """주민등록번호를 읽거나 설정하는 메소드가 아니다 그냥 주민등록 번호를 기준으로 본인이 맞는지 인증하는 메소드다"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"

    @property
    def age(self):
        print("나이를 리턴 합니다")
        return self._age

    @age.setter
    def age(self, value):
        print("나이를 설정 합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

young = Citizen("kang", 19, "980322")
print(young.age)


young.age = 30
print(young.age)












# 파이썬에서 진정한 캡슐화 전
class Citizen:
    drinking_age = 19
    
    def __init__(self, name, age, resident_id):
        self.name = name
        self.set_age(age)
        self.__resident_id = resident_id
    
    def authenticate(self, id_field):
        return self.__resident_id == id_field

    def can_drink(self):
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self.__age == 0
        else:
            self.__age = value

taeho = Citizen("taeho", 13, "980322")
print(taeho)
print(taeho.can_drink())
print(taeho.name)

print(taeho.get_age())
taeho.set_age(23)
print(taeho.get_age())
print(taeho.can_drink())

taeho.set_age(-13)
print(dir(taeho))
print(taeho._Citizen__age)

# 파이썬에서 진정한 캡슐화 후
class Citizen:
    drinking_age = 19
    
    def __init__(self, name, age, resident_id):
        self.name = name
        self.set_age(age)
        self._resident_id = resident_id
    
    def authenticate(self, id_field):
        return self._resident_id == id_field

    def can_drink(self):
        return self._age >= Citizen.drinking_age

    def __str__(self):
        return self.name + "씨는 " + str(self._age) + "살입니다!"

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age == 0
        else:
            self._age = value

taeho = Citizen("taeho", 13, "980322")
print(taeho)
print(taeho.can_drink())
print(taeho.name)

print(taeho.get_age())
taeho.set_age(23)
print(taeho.get_age())
print(taeho.can_drink())

taeho.set_age(-13)

# 파이썬에서 데코레이터를 사용한 캡슐화 -> 이방식으로 해야함!!
class Citizen:
    drinking_age = 19
    
    def __init__(self, name, age, resident_id):
        self.name = name
        self.age = age
        self._resident_id = resident_id
    
    def authenticate(self, id_field):
        return self._resident_id == id_field

    def can_drink(self):
        return self._age >= Citizen.drinking_age

    def __str__(self):
        return self.name + "씨는 " + str(self._age) + "살입니다!"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value


taeho = Citizen("taeho", 13, "980322")
print(taeho)
print(taeho.can_drink())
print(taeho.name)

#print(taeho.get_age())
#taeho.set_age(23)
#print(taeho.get_age())

#taeho.set_age(-13)
print(taeho.age)
taeho.age = 30
print(taeho.age)

taeho.age = -13
print(taeho.age)
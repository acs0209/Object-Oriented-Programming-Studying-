# 06. 상속2(오버라이딩)
# 자식 클래스들(Cashier, DeliveryMan)은 부모 클래스의 변수와 메소드를 물려받기만 한다. 
# 이렇게 되면 자식 클래스를 제대로 사용할 수 없다 둘 다 물려받은 내용이 같아서 두 클래스 사이에 차이가 없기 때문이다
# 물려 받은 내용을 Cashier클래스와 DeliveryMan 클래스에 맞게 각각 바꿔줘야 합니다.
# 부모클래스로부터 물려받은 내용을 자식 클래스가 자신에 맞게 변경하는걸 오버라이딩이라고 합니다.
# 오버라이딩은 우리말로 덮어 쓴다는 뜻이다. 부모로부터 물려받은걸 자기에 맞게 덮어써서 수정한다는 뜻이다

# 이제 Cashier클래스에서 오버라이딩을 해보자 Cashier클래에서 __init__메소드를 오버라이딩 해보자
# 근데 Employee 클래스의 __init__ 메소드를 그대로 물려받아 사용해도 될까?
# Employee 클래스의 __init__ 메소드는 지금 name 과 wage만 설정하고 있다 근데 원래 Cashier클래스의 __init__메소드에는
# number_sold라는 변수도 있었다 그래서 Employee 클래스의 __init__ 메소드를 그대로 사용하면 안 될꺼 같다
# 이럴 땐 Cashier클래스에서 __init__메소드를 오버라이딩하면 된다. 오버라이딩은 자식클래스에서 물려받은 메소드와
# 같은 이름의 메소드를 내용을 바꿔서 정의해 주면 된다 한번 해보자 어떻게 하냐면 예를 들어 똑같이 __init__ 메소드를
# 정의하고 조금 다른 내용으로 적어 주면 된다. 방금 작성한 __init__메소드는 Employee클래스의 __init__ 메소드와 달리
# 판매나 햄버거의 개수를 나타내는 number_sold 파라미터와 변수가 있다 부모로부터 물려받은 __init__메소드와는 
# 차이가 있는거죠 이렇게 오버라이딩 하면 Cashier클래스로 인스턴스를 생성할때 Employee 클래스한테 물려받은
# __init__ 메소드가 아니라 Cashier클래스 자신의 __init__메소드가 실행된다.
# 근데 지금 Cashier클래스의 __init__메소드와 Employee클래스의 __init__메소드에는 겹치는 부분이 있다
# 그 부분은 super()라는 함수를 쓰면 된다 super()함수는 자식 클래스에서 부모 클래스의 메소드를 사용하고 싶을때
# 쓰는 함수이다 super함수로 부모 클래스의 메소드를 사용할때는 self파라미터를 넘겨 줄 필요가 없습니다.
# 이건 파이썬의 규칙이니까 기억하자 그래서 super().__init__(name, wage)이렇게 작성하면 된다.

# 변수를 오버라이딩하는 것은 자식 클래스에서 다른 값을 대입하는 겁니다.
# 변수를 오버라이딩하려면 그냥 자식 클래스에도 똑같은 이름의 변수를 두고 다른 값을 넣으면 됩니다.

# 메소드는 자식 클래스부터 부모 클래스 방향으로 검색된다 이거때문에 메소드 오버라이딩이 가능하다
# 부모 클래스와 자식 클래스에 같은 이름의 메소드가 있더라도 자식 클래스의 메소드가 먼저 검색되어 실행 되기 때문에.
# 메소드 오버라이딩이 가능하다.
class Employee:
    """직원 클래스"""
    raise_percentage = 1.03
    company_name = "코드잇 버거"

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= Employee.raise_percentage
        return self.wage
    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name

class Cashier(Employee):
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거르슴돈을 리턴한다."""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


class DeliveryMan(Employee):
    pass

young = Cashier("강영훈", 8900, 4000)
print(young)
print(young.raise_pay())

print(young.raise_percentage)
print(Cashier.raise_percentage)
print(Employee.raise_percentage)

print(young.take_order(80000))
print(young.raise_pay())
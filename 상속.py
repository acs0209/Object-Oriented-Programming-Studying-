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

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    burger_price = 4000
    
    def __init__(self, name, wage, number_sold = 0):
        self.name = name
        self.wage = wage
        self.number_sold = number_sold

    def raise_pay(self):
        """시급을 인상하다"""
        self.wage *= self.raise_percentage

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다."""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + "계산대 직원:" + self.name

jiwoong = Cashier("최지웅", 8900, 0)

jiwoong.raise_pay()
print(jiwoong.wage)
print(jiwoong.take_order(10000))
print(jiwoong.burger_price)
print(Cashier.burger_price)
print(jiwoong)

class DeliveryMan(Employee):
    def __init__(self, name, wage, on_standby):
        
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력한다."""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다.")
    
    def back(self):
        """배달원 복귀 처리한다"""
        self.on_standby = True


print(Cashier.mro())
print(list.mro())
print(IndentationError.mro())

print(isinstance(jiwoong, Cashier))
print(isinstance(jiwoong, DeliveryMan))
print(isinstance(jiwoong, Employee))
print(isinstance(jiwoong, list))
print(isinstance(jiwoong, int))

print(issubclass(Cashier, Employee))
print(issubclass(DeliveryMan, Employee))
print(issubclass(Employee, list))




 
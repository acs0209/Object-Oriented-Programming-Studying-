from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*self.width + 2*self.height

    def __str__(self):
        return "밑변 높이 {}, 높이{}인 직사각형".format(self.width, self.height)

# 04
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius**2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return "반지름 {}인 원".format(self.radius)

#05
class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)

class Paint:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        # 이렇게 area,perimeter메소드가 있는 인스턴스만 그림판에 추가되어야 나중에 shape.메소드()부분이 오류가 나지 않는다.
        # 만약 shape클래스의 인스턴스가 아니라면 추가할 수 없다는 메시지룰 출력하자
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])
    
    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다."""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str

rectangle = Rectangle(3, 7)
circle = Circle(4)
eq = EquilateralTriangle(5)

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
print(paint_program)
# 리스트 shapes에 도형을 추가하기 전에 그 인스턴스가 Rectangle 클래스의 인스턴스 혹은 Circle 클래스의 인스턴스가 맞는지 확인하고, 맞는 경우에만 추가하면 어떨까요?

# 04. 상속을 활용한 다형성1(일반상속)
# 위에 내용을 정리해 보면 어떤 변수가 여러 종류의 인스턴스를 가리키게 해서 다형성을 가지게 할 수 있습니다.
# 하지만 그 인스턴스에 어떤 메소드를 호출했을때 인스턴스가 그 메소드를 가지고 있어야만 다형성이 성립됩니다.
# 그 메소드를 갖고 있지 않으면 에러가 발생한다 이걸 방지할려면 메소드 호출전에 isinstance함수로
# 어떤 클래스의 인스턴스가 맞는지 미리 확인해야 하는데요 이때 클래스 종류가 많으면 isinstance함수의 개수가
# 많아 진다는 단점이 있습니다.하지만 상속을 사용하면 isinstance를 딱 한번만 쓰면 된다 상속을 사용하면
# 좀 더 짧은 코드로 안전하게 다형성을 익힐 수 있습니다
# isinstance(shape, Shape) -> 1. shape은 Shape클래스의 인스턴스인가?(이때 생각해야할점은 자식 클래스의 인스턴스는 부모 클래스의 인스턴스 이기도 하다!)
#                             2. shape은 area메소드와 perimeter메소드를 갖고 있는가?


# 05. 상속을 활용한 다형성2(일반 상속의 문제점)
# 일단 Shape클래스에 area,perimeter메소드 내용이 pass로 채운 이유는 상속을 받는 자식클래스에서 오버라이딩을 하라는 소리다
# 월래 Shape에 있는 area,perimeter메소드는 자식 클래스가 알아서 오버라이딩하라고 일부러 비워둔거다 그런데
# 정삼각형 클래스처럼 자식 클래스가 오버라이딩을 하지 않았는데도 그림판에 추가 되는 경우가 생길 수도 있다
# 그림판에 추가될 도형들은 Shape클래스를 상속받아야할뿐만아니라 area,perimeter메소드도 꼭 오버라이딩 해야합니다
# 그래야 에러를 막을 수 있다 Shape클래스의 자식클래스가 area,perimeter메소드를 오버라이딩하도록 강제할수는 없을까?

# 06. 상속을 활용한 다형성 III (추상 클래스 개념)
# Shape클래스의 자식 클래스가 메소드도 강제로 오버라이딩하게 할려면 추상클래스를 사용하면 된다
# 추상 클래스란 여러 클래스들의 공통점을 추상화해서 모아 놓은 클래스입니다.
# 추상 클래스는 ABC 클래스를 상속받고 적어도 하나 이상의 추상 메소드를 가져야 합니다
# 여기서 주의할점은 추상 클래스는 인스턴스 생성이 불가능하다 
# 추상클래스는 인스턴스를 직접 생성하려고 쓰는 클래스가 아닙니다.
# 추상클래스는 여러 클래스들의 공통점을 담아두고 다른 클래스들이 상속받는 부모 클래스가 될 목적으로 존재합니다.


# 07. 상속을 활용한 다형성 IV (추상 클래스 활용)
# 추상 메소드를 오버라이딩 하지 않으면 그대로 추상 메소드인데요 
# 지금 삼각형 메소드에서는 area와 perimeter메소드는 여전히 추상 메소드인 겁니다.
# 지금 정삼각형 메소드는 ABC를 상속받고, 추상 메소드를 하나 이상 가지고 있기 때문에 추상 클래스이다
# 하지만 물려받은 추상 메소드를 오버라이딩하면 일반 클래스로 만들 수 있다 
# Shape클래스를 추상 클래스로 만드니까 자식 클래스가 추상 메소드인 area, perimeter메소드를 강제로 오버라이딩 하게 했습니다
# 오버라이딩을 안 하면 에러가 났었죠? 


# 08
# 추상 클래스로 원하는 클래스의 조건(여기서는 클래스가 area, perimeter 메소드를 가져야한다는 조건)을 정하고
# 해당 추상 클래스의 인스턴스만 그림판에 추가한다면(추상 클래스로는 인스턴스를 바로 생성할 수 없으므로 실제로는 
# 해당 추상 클래스의 자식 클래스의 인스턴스입니다, isinstance 함수를 배울 때 자식 클래스의 인스턴스는 
# 부모 클래스의 인스턴스이기도 하다는 걸 배웠죠?)






class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass
  
    def larger_than(self, shape):
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()








class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass
  
    def larger_than(self, shape):
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()
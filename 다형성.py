# shape이 지금 rectangle 인스턴스를 가리킬때도 있고 circle 인스턴스를 가리킬때도 있는것을 다형성이 있다 라고 표현하다.
# 하나의 변수가 서로 다른 클래스의 인스턴스를 가리킬 수 있는 성질을 다형성이라고 한다
# 다형성은 월래 여러가지 형태를 갖는 성질을 말한다. 
# 지금 shape이 어쩔때는 rectangle 인스턴스가 되고 어쩔때는 circle 인스턴스가 되는 이 카멜레온처럼 변하는 모습을 다형성이 있다라고 얘기한다
# 다시한번 강조하면 위에처럼 되는건 shape변수에 들어가는 Rectangle클래스 Circle클래스 둘다 area메소드와 perimeter메소드를
# 갖고 있기 때문에 가능한거다




class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


from math import pi

class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])
    
    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])
    
    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다."""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str



rectangle = Rectangle(3, 7)
circle = Circle(4)
cylinder = Cylinder(7, 3)

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)
paint_program.add_shape(cylinder)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

# 추상 클래스
# 여러 클래스들의 공통점을 추상화해서 모아놓은 클래스

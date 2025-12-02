"""Math exercises."""
import math
from wsgiref.validate import assert_


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    addition_result = num_a + num_b
    difference = num_a - num_b
    return addition_result, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * radius ** 2
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return int(round(triangle_area, 0))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c ** 2 - a ** 2)
    return b


if __name__ == '__main__':
    addition_result, difference = sum_and_difference(5, 6)
    assert addition_result == 11
    assert difference == -1

    float_division_result = float_division(10, 10)
    assert isinstance(float_division_result, float)
    assert 0.99 < float_division_result < 1.01
    float_division_result = float_division(10, 2)
    assert 4.99 < float_division_result < 5.01

    integer_division_result = integer_division(10, 10)
    assert isinstance(integer_division_result, int), f"Result should be of type int but is {type(integer_division_result)}"
    assert integer_division_result == 1
    integer_division_result = integer_division(10, 2)
    assert integer_division_result == 5

    multiplication, power, remainder = powerful_operations(3, 4)
    assert multiplication == 12
    assert power == 81
    assert remainder == 3

    multiplication, power, remainder = powerful_operations(10, 2)
    assert multiplication == 20
    assert power == 100
    assert remainder == 0

    area_of_a_circle_result = area_of_a_circle(3)
    assert 28.269 < area_of_a_circle_result < 28.271, f"{area_of_a_circle_result}"

    """Math exercises vol2."""
    import math


    def time_converter(seconds: int) -> str:
        """Convert time in seconds to hours and minutes."""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


    def student_helper(angle: int) -> str:
        """Return the sine and cosine of the given angle in degrees."""
        radians = math.radians(angle)
        sine = round(math.sin(radians), 1)
        cosine = round(math.cos(radians), 1)
        return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


    def greetings(n: int) -> str:
        """Return a string that contains "Hey" n times."""
        lots_of_heys = "Hey" * n
        return lots_of_heys


    def adding_numbers(num_a: int, num_b: int) -> str:
        """Return given numbers added together as a string."""
        string_numbers = str(num_a) + str(num_b)
        return string_numbers


    """Basic function exercises."""
    import math


    def print_hello():
        """Print "hello"."""
        print("Hello")


    def get_hello() -> str:
        """Return "hello"."""
        return "Hello"


    def ask_name_and_greet_user():
        """
        Ask name and greet user.

        The user has to enter his/her name. The function prints the greeting.

        Regular greeting: Hi, [name]. Would you like to have a Hamburger?
        [name] is capitalized, meaning first letter is capital, the rest is lower.

        If the name is Thanos (case insensitive, so thanos and THANOS also count):
        Get out of here, Thanos! Nobody wants to play with you!
        """
        name = input("Sisesta nimi: ")
        regular_greeting = f"Hi, {name.capitalize()}. Would you like to have a Hamburger?"
        thanos_greeting = "Get out of here, Thanos! Nobody wants to play with you!"
        if name.lower() == "thanos":
            print(thanos_greeting)
        else:
            print(regular_greeting)


    def calculate_hypotenuse_length(a: float, b: float) -> float:
        """Return hypotenuse value."""
        c = math.sqrt(a ** 2 + b ** 2)
        return c


    def calculate_cathetus_length(a: float, c: float) -> float:
        """Return cathetus value."""
        b = math.sqrt(c ** 2 - a ** 2)
        return b


    if __name__ == '__main__':
        print_hello()  # should print "Hello"
        hello = get_hello()  # should return "Hello"
        print(hello)  # let's check the value of hello variable
        ask_name_and_greet_user()  # should ask name and greet
        print(calculate_hypotenuse_length(3, 4))  # should print 5.0
        print(calculate_cathetus_length(3, 5))  # should print 4.0


        """Function examples."""


        # func()
        def func():
            """Print a message I'm inside the function."""
            print("I´m inside the function")


        # my_name_is(name)
        def my_name_is(name):
            """Print 'My name is [name]'."""
            print("My name is " + name)


        # sum_six(num)`
        def sum_six(num: int) -> int:
            """Return num plus 6."""
            return num + 6


        # sum_numbers()
        def sum_numbers(num_a: int, num_b: int) -> int:
            """Return the sum of num_a and num_b."""
            return num_a + num_b


        # usd_to_eur()
        def usd_to_eur(num_a: int) -> float:
            """Convert USD to EUR at rate 1 USD = 0.8 EUR."""
            return num_a * 0.8

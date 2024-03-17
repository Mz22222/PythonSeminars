# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# просто число - это число, которое делится на себя и на 1

def is_prime(number: int) -> bool:

    for index in range(2, int(number ** 0.5) + 1):

        if number % index == 0:

            return False

    return True


print(is_prime(7))
import math

def problem1(limit):
    sum_multiples = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    return sum_multiples

def problem2(max_value):
    def sum_even_fibonacci(max_value):
        fib_1, fib_2 = 1, 2
        even_sum = 0
        
        while fib_1 <= max_value:
            if fib_1 % 2 == 0:
                even_sum += fib_1
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        
        return even_sum

    return sum_even_fibonacci(max_value)

def problem3(numero):
    mayor_primo = 0
    
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            mayor_primo = i
            numero //= i
    
    if numero > 1:
        mayor_primo = numero
    return mayor_primo

def find_largest_palindrome(num):
    return str(num) == str(num)[::-1]

def problem4():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if find_largest_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

def problem5(num):
    lcm = 1
    for i in range(1, num):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm




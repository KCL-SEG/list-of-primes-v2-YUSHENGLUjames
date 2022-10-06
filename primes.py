"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isprime(number):
    for n in range(2,number):
        if number % n == 0:
            return False
    return True

def primes(number_of_primes):

    list = []
    index = 0
    number = 2

    if number_of_primes<=0:
        raise ValueError("Number should be positive")

    while index < number_of_primes:
        if isprime(number):
            index += 1
            list.append(number)
        number += 1

    return list

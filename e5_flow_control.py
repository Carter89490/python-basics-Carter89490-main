'''
fizz_buzz:
  - return "fizz" if divisible by 3
  - return "buzz" if divisible by 5
  - return "fizzbuzz" if divisible by both 3 and 5
  - return the number itself if not divisible by 3 or 5
  - return False if the input is not a number
'''
def fizz_buzz(n):
    if not isinstance(n, (int, float)):
        return False
    if n % 15 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return n
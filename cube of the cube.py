def cube(number):
    return number*number*number

def div_by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return "Not divisible by 3. False."
    
print(div_by_three(6))
print(div_by_three(7))
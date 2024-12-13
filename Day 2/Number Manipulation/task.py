bmi = 84 / 1.85 ** 2
print(bmi)
print(int(bmi))         # floors it down to nearest integer -- 2.2 & 2.8 both equal 2
print(round(bmi))       # rounds it traditionally -- 2.2 = 2 and 2.8 = 3
print(round(bmi, 5))    # how accurately, how many decimal numbers

def addition_wAdd():
    add = 2
    add += bmi
    print(add)

def substraction_wSub():
    sub = 2
    sub -= bmi
    print(sub)

def multiply_wMul():
    mul = 2
    mul *= bmi
    print(mul)

def divide_wDiv():
    div = 2
    div /= bmi
    print(div)

addition_wAdd()
substraction_wSub()
multiply_wMul()
divide_wDiv()

age = int(input("Age: "))
print(f"My age: {age + 12}")
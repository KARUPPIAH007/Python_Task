def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return 'Cannot be divide by zero'

values = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

def cal():
    while True:
        print('\n select the choice:')
        print('1.Addition of Two Number')
        print('2.Subtraction of Two Number')
        print('3.Multiplication of Two Number')
        print('4.Division of Two Number')
        print('5.Exit')
        
        choice = int(input('Enter your choice:'))
        
        if choice in values:
            x = int(input('Enter First Number:'))
            y = int(input('Enter Second Number:'))
            Finalvalue = values[choice](x,y)
            print(f"Result: {Finalvalue}")
        else:
            exit(0)

if __name__ == "__main__":
    cal()
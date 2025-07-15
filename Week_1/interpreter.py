

def main(usr_input):
    ''' 
    x is an integer
    y is an operator, '+','-','*','/'
    z is an integer
    '''
    x, y, z = usr_input.split(" ")
    x = int(x)
    z = int(z)
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z) 
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)

if __name__ == "__main__":
    usr_input = input("Expression: ")
    main(usr_input)


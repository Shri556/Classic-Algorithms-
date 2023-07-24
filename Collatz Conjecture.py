#Start with a number *n > 1*. Find the number of steps it takes to reach 
#one using the following process: 
#If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1

def inpt():
    while True:
        x = input("Please enter a Number:\n>>")
        
        if x.isnumeric():
            x = int(x)
            if x > 1:
                break
            else:
                print("INPUT should be greater than 1.")
        
        else:
            print("Enter a Valid Input")
    return x

def calc(n):
    
    while n > 1:
        print(n,end=' ')
        if n % 2 ==0:
            n = n // 2
        else:
            n = n * 3 + 1
    print('1',end='')

if __name__== '__main__':
    x = inpt()
    calc(x)
    
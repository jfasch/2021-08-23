import sys

number = int(sys.argv[1])

if number == 1:
    print(number, 'is not prime')
    sys.exit()

for divisor in range(2, number):
    if number % divisor == 0:
        divisor_found = True
        print(number, 'is not prime')
        break
else:
    print(number, 'is prime')
    

def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if (number%i==0):
            is_prime=False
    if is_prime:
        print("ITS A PRIME NUMBER")
    else:
        print("ITS NOT A PRIME")
n=int(input("ENTER A NUMBER"))
prime_checker(n)
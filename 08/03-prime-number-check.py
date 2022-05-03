
# #Write your code below this line 👇

# def prime_checker(number):
#     if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
#         print("It's a prime number")
#     elif number % 2 == 0:
#         print("It's not a prime number")
#     elif number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
#         print("It's not a prime number")
#     else:
#         print("It's a prime number")


# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")
        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

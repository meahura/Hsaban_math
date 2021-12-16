#!bin/python3.8.10 

# Import required modules

import math


# colors ; 
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'


help = F"""
{GREEN} Geometric {WHITE} and arithmetic{RED} follow-ups 🇮 🇷 🇦 🇳 {WHITE}
\033[32m
\33[34m[1] = \033[37mArithmetic sequences 
\33[34m[2] = \033[37mGeometric sequence  
\33[34m[3] = \033[37mRadius in Daryereh 
\33[34m[4] = \033[37mChinus 
\33[34m[5] = \033[37mSquare root 
\33[34m[6] = \033[37mReturn the absolute value of x.  

""" 
print(help)

math_ = int(input('\033[91mEnter number "Tools" : ')) 


if math_ == 1 : 
    try:
        # input  First account sequence number and Enter Number of sentences requested and Wad absolute magnitude  
        a = int(input('\033[32mEnter First account sequence number : ‌'))
        d = int(input("\033[32mWad absolute magnitude : "))
        n = int(input('\033[32mEnter Number of sentences requested : ') )
        # Calculation of input numbers ; 
        word_Split = n / 2 
        word_2a = 2 * a 
        word_n_d = (n - 1 ) * d 
        # Calculation and output of work ; 
        new_1 = word_2a + word_n_d 
        print(f"answer : \033[31m{word_Split * new_1}")
        # end 
    except : 
        print(f"\033[31mvalue Error : Please enter the correct entry!")

elif math_ == 2 :
    try:
        # input  First account sequence number and Enter Number of sentences requested and Wad absolute magnitude   
        a = int(input('\033[32mEnter First account sequence number :‌ '))
        q = int(input("\033[32mWad absolute magnitude : "))
        n = int(input('\033[32mEnter Number of sentences requested : ') )
        # Calculate  ; 
        Qu_N = q ** n 
        Calc = Qu_N - 1  
        # Final Output [ Geometric sequence ] ; 
        print(f"answer : \033[31m{a * Calc}")
        # end 
    except : 
        print(f"\033[31mvalue Error : Please enter the correct entry! ")

elif math_ == 3 : 
    try: 
        # Input the number of points asked in the circle 
        p = int(input('\033[32mEnter the number of dots : '))
        # Calculation of dots  
        P_Not_One = p -1 
        Calculate = P_Not_One * p 
        Tg = Calculate /  2 
        # Final Output [ Dots on the circle ] ; 
        print(f"answer : \033[31m{Tg}")
        # end 
    except : 
        print(f"\033[31mvalue Error : {p}")  

elif math_ == 4 : 
    try:
        # input Chinus 
        cosinoss = int(input('\033[32mEnter your number [ Convert to cosine ] : '))
        # Convert number to cosine 
        print(F"answer : \033[31m{math.cos(cosinoss)}")
        # end 
    except: 
        print(f"\033[31mvalue Error : {cosinoss}")  

elif math_ == 5 : 
    try: 
        # input sqrt  
        user_  = int(input('\033[32mEnter Square root [ number ]  : '))
        # Take the second input number  
        print(f"answer : \033[31m{math.sqrt(user_)}") 
        # end 
    except: 
        print(f"\033[31mvalue Error : {user_}")  

elif math_ == 6:
    try: 
        # Rturn the absolute value of x = > input 
        user_X = int(input('\033[32mEnter number [ Return the absolute value ] : '))
        print(f"answer : \033[31m{math.fabs(user_X)}")
    except : 
        print(f"\033[31mvalue Error : {user_X}")  

else: 
    print(f"""\33[1m\033[37mError Entry !""")

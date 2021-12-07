# !bin/ruby 2.7

# import moudles ; 
module Math
    

help = """

geometric and arithmetic follow-ups 🇮 🇷 🇦 🇳

# 1 = Arithmetic sequences 
# 2 = Geometric sequence  
# 3 = Radius in Daryereh 
# 4 = Chinus 
# 5 = Square root 
# 6 = erf , Calculates the error function of x.   

"""
puts help 

# input [ NUMBER TOOLS !! ] 

news = 6 # Variable value  


if news == 1
    #  input  First account sequence number and Enter
    # Number of sentences requested and Wad absolute magnitude    

    a = 10 # Variable value [a]
    d = 15 # Variable value [d]
    n = 17 # Variable value [n]

    # Calculation of input numbers ;   
    word_Split = n /2 
    word_2a = 2 * a 
    word_n_d = (n - 1 ) * d 
    # Calculation and output of work ; 
    new_1 = word_2a + word_n_d 
    puts "answer : #{word_Split * new_1} - a"
end 

if news == 2 
    # Variable value   
    a = 10 # value [a]
    q = 20 # value [q]
    n = 17 # value [n]
    # Calculate  ;   
    qu_N = q ** n 
    calc = qu_N - 1  
    # Final Output [ Geometric sequence ] ; 
    puts "answer : #{a * calc} - b "
end 

if news == 3 
    # Variable value  
    po = 19 
    # Calculation of dots   
    p_Not_One = po -1 
    calculate = p_Not_One * po
    tg = calculate /  2 
    # Final Output [ Dots on the circle ] ; 
    puts "answer : #{tg}"
end 

if news == 4 
    n = 12 # Variable value   
    cosinoosn = Math.cos(n) # Cos 
    puts "answer : #{cosinoosn}" 
end  

if news == 5 
    n = 12 # Variable value  
    puts "answer : #{Math.sqrt(n)}" # Sqrt 
end

if news == 6 
    n = 17 
    puts "answer : #{Math.erf(n)}" 
end
end

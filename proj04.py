#############################################
# 
# CSE 231 Project 04
#
# Main Function
#   Ask for input to determine which function
#   Ask for input function dependant
#   Call Function
#   Errors for incorrect or unusable inputs
#
#   Conway
#       Int to Base 
#           Loop until q=0
#           12 = C
#           11 = B
#           10 = A
#           r gets added if none of above
#       Tridecimal Expanstion  
#           Character Replacement
#           A = +
#           B = -
#           C = .
#           Everything else is untouched
#       Tridec to Conway
#           Flip and look for specifics
#           Find decimal and sign before
#           Check again to make sure has decimal
#       Return
#
#   Zeta
#       Zeta Function
#       Check if difference in current and next term is less than delta
#       if yes
#           Return
#       if no
#           Continue to next term
# 
#############################################

# Float Check

def float_check(n):
    try:
        float(n)
        return True
    except:
        return False

# Int to Base Working

def int_to_base13(n):
    n = int(n)
    n_str = ''
    q = n
    while q != 0:
        r = q % 13
        if r == 12:
            n_str += 'C'
        elif r == 11:
            n_str += 'B'
        elif r == 10:
            n_str += 'A'
        else:
            n_str += str(r)
        q = q // 13
    n_str = n_str[::-1] # Could you just not flip this until the end?
    return( n_str )

# Tridecimal Expansion Working

def tridecimal_expansion(n_str):
    n_str = n_str.replace('A','+')
    n_str = n_str.replace('B','-')
    n_str = n_str.replace('C','.')
    return( n_str )

# Tridecimal to Conway
    
def tridecimal_to_conway(n_str):
    n_str = str(n_str)
    n_str = n_str[::-1]
    if n_str[0] == '-' or n_str[0] == '+':
        return 0
    if n_str.find('.') == -1:
        return 0
    p = n_str.find('+')
    m = n_str.find('-')
    
    # No Signs
    
    if p == -1 and m == -1:
        c_str = n_str[::-1]
        return( float(c_str) )
    
    # No Negative Signs
    
    elif m == -1:
        p = int(p)
        c_str = str(n_str[0:p])
        c_str = c_str[::-1]
        if c_str.find('.') == -1:
            return 0
        else:
            return( float(c_str) )
    
    # No Positive Signs
    
    elif p == -1:
        m = int(m+1)
        c_str = str(n_str[0:m])
        c_str = c_str[::-1]
        if c_str.find('.') == -1:
            return 0
        else:
            return( float(c_str) )
    
    # Postive Sign First    
    
    elif p < m:
        p = int(p)
        c_str = str(n_str[0:p])
        c_str = c_str[::-1]
        if c_str.find('.') == -1:
            return 0
        else:
            return( float(c_str) )
    
    # Negative Sign First
    
    elif p > m:
        m = int(m+1)
        c_str = str(n_str[0:m])
        c_str = c_str[::-1]
        if c_str.find('.') == -1:
            return 0
        else:
            return( float(c_str) )
    
# Zeta Working

def zeta(s):
    try:
        float(s)
        s = float(s)
    except:
        int(s)
        s = int(s)
        
    if s <= 0:
        return None
    elif s > 0:
        z = 1
        n = 2
        while abs(( 1 / ( ( n-1 )**s ) ) - ( 1 / ( n**s ) ) ) > 10**-7:
            z += ( 1/ ( n**s ) )
            n += 1
    return( z )         
                    
# Main Working
    
def main():
    print("Functions")
    qm = input("Enter Z for Zeta, C for Conway, Q to quit: ")
    qm = qm.lower()
    while True:  
        if qm == 'z':
            print('Zeta')
            s = input("Input a number: ")
            while True:
                if float_check(s) == True:
                    print(zeta(s))
                    break
                else:
                    print("Error in input.  Please try again.") 
                    s = (input("Input a number: "))

            qm = input("Enter Z for Zeta, C for Conway, Q to quit: ")
            qm = qm.lower() 
            
        elif qm == 'c':
            print("Conway")
            n = input("Input a positive integer: ")
            while True:
                if n.isdigit():
                    print("Base 13:",int_to_base13(n)) 
                    n_str = int_to_base13(n)
                    print("Tridecimal:",tridecimal_expansion(n_str))
                    n_str = tridecimal_expansion(n_str)
                    print("Conway float: ",tridecimal_to_conway(n_str))
                    break
                else:
                    print("Error in input.  Please try again.") 
                    n = input("Input a positive integer: ")
            
            qm = input("Enter Z for Zeta, C for Conway, Q to quit: ")
            qm = qm.lower()   
            
            
        elif qm == 'q':
            print("\nThank you for playing.")
            break              
        else:
            print("Error in input.  Please try again.")
            qm = input("Enter Z for Zeta, C for Conway, Q to quit: ")
            qm = qm.lower()

# Call Main

if __name__ == "__main__":
    main()
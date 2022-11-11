#############################################
#
# CSE 231 Project 03
#
# Calc tuition based on
#  1. Grede Level
#  2. College
#  3. Credits
#
#############################################
level = 0
college = 0
coe = 0
jmc = 0
tuition = 0
rep = 'yes'

print( "2021 MSU Undergraduate Tuition Calculator.\n" )

while rep == 'yes':
    level = input( "Enter Level as freshman, sophomore, junior, senior: " )
    level = level.lower()

    while level.isalpha():
        if (level == 'junior') or (level == 'senior'):
            college = input("Enter college as business, engineering, health, sciences, or none: " )
            college = college.lower()
            if (college == 'business') or (college == 'engineering') or (college == 'health') or (college == 'sciences'):
                break
            else:
                jmc = input( "Are you in the James Madison College (yes/no): " )
                jmc = jmc.lower()
                if jmc == 'yes':
                    break
                else:
                    break      
        elif (level == 'freshman') or (level == 'sophomore'):
            coe = input( "Are you admitted to the College of Engineering (yes/no): " )
            coe = coe.lower()  
            if coe == 'yes':
                break
            else:
                jmc = input( "Are you in the James Madison College (yes/no): " )
                jmc = jmc.lower()
                if jmc == 'yes':
                    break
                else:
                    break
        else:
            print( "Invalid input. Try again." )
            level = input( "Enter Level as freshman, sophomore, junior, senior: " )
            
            
    
    credits = input( "Credits: " )
    
    while credits:
        if credits.isdigit():
            credits = int(credits)
            if credits > 0:
                break
            else:
                print( "Invalid input. Try again." )
                credits = input( "Credits: " )
        else:
            print( "Invalid input. Try again." )
            credits = input( "Credits: " )
            
    while credits > 0:        

    # 1-11 Base
        
        if 1 <= credits <= 11:
            if level == 'freshman':
                tuition = 482*credits
                break
            elif level == 'sophomore':
                tuition = 494*credits
                break
            elif level == 'junior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 573*credits
                    break
                else:
                    tuition = 555*credits
                    break
            elif level == 'senior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 573*credits
                    break
                else:
                    tuition = 555*credits
                    break   
                
    # 12-18 Base
    
        elif 12 <= credits <= 18:
            if level == 'freshman':
                tuition = 7230 
                break
            elif level == 'sophomore':
                tuition = 7410
                break
            elif level == 'junior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 8595
                    break
                else:
                    tuition = 8325
                    break
            elif level == 'senior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 8595
                    break
                else:
                    tuition = 8325
                    break  
    
    # >18 Base    
    
        elif credits > 18:
            credit_o = int(credits - 18)
            if level == 'freshman':
                tuition = 7230 + 482*credit_o
                break
            elif level == 'sophomore':
                tuition = 7410 + 494*credit_o
                break
            elif level == 'junior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 8595 + 573*credit_o
                    break
                else:
                    tuition = 8325 + 555*credit_o
                    break
            elif level == 'senior':
                if (college == 'business') or (college == 'engineering'):
                    tuition = 8595 + 555*credit_o
                    break
                else:
                    tuition = 8325 + 555*credit_o
                    break
                
        else:
            print( "Invalid input. Try again." )  
            credits = input( "Credits: " )
            
    # Special College Charges
        
    if college == 'business':
        if credits <= 4:
            tuition += 113
        else:
            tuition += 226
    if (college == 'engineering') or (coe == 'yes'):
        if credits <= 4:
            tuition += 402
        else:
            tuition += 670
    if college == 'health':
        if credits <= 4:
            tuition += 50
        else:
            tuition += 100
    if college == 'sciences':
        if credits <= 4:
            tuition += 50
        else:
            tuition += 100
            
    # Student Taxes
    
    if level.isalpha():
        tuition += 21
        tuition += 3
    if credits >= 6:
        tuition += 5
    if (jmc == 'yes'):
        tuition += 7.5
    
    # Final Tuition
    
    tuition = float(tuition)
    print("Tuition is ${:,.2f}.".format(tuition))

    # Loop

    rep = input( "Do you want to do another calculation (yes/no): ") 
    rep = rep.lower()
                
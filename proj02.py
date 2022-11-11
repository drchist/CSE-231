#############################################
#
# CSE 231 Project 02
#
# Forza Horizon 5 Car Rental
# 1. Ask the customer if the would like to continue A/B
# 2. Prompt the customer for
#   a. Classification Code (Character)
#   b. Number of days rented (Integer)
#   c. Initial odometer reading (Integer)
#   d. Final odometer reading (Integer)
# 3. Calc total based on classification code
#   a. BD (Budget) 40 (Daily Charge) + .25 M (Per Mile)
#   b. D (Daily) 60 (Daily Charge) + .25 M (Per Miles over AVG 100 per day)
#   c. W (Weekly) 190 (Weekly Charge) 
# 4. Compute miles driven (6 digits with last being tenths)
# 5. Display summary
#   a. Classification Code
#   b. Number of days rented
#   c. Initial Odometer
#   d. Final Odometer
#   e. Miles Driven in Rental Period
#   f. Amount Billed
# 6. Prompt again if invalid classification code
# 
# I Could Have used prompt and banner instead of repeating prints
#
#
#############################################

import math

print( "\nWelcome to Horizons car rentals. \n" )
print( "At the prompts, please enter the following: " )
print( "	Customer's classification code (a character: BD, D, W) " )
print( "	Number of days the vehicle was rented (int)" )
print( "	Odometer reading at the start of the rental period (int)" )
print( "	Odometer reading at the end of the rental period (int)" )
test = input( "\nWould you like to continue (A/B)? ")

while test == 'A' or test == 'B':
    if test == 'A':
        CC = input( "\nCustomer code (BD, D, W): " )
        if CC == 'BD' or CC == 'D' or CC =='W':
            T = input( "\nNumber of days: " )
            OD1 = input( "Odometer reading at the start: " )
            OD2 = input( "Odometer reading at the end:   " )
            
# BD WORK DONE BUT STUPID

        if CC == 'BD': 
            if OD2 >= OD1:
                OD3 = (int(OD2)-int(OD1)) / 10
                c_tot = 40.0 * int( T ) + .25 * int(OD3)
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
            elif OD1 > OD2:
                OD3 = ( (1000000.0 + int( OD2 ) ) - int( OD1 ) ) / 10.0  
                c_tot = 40.0 * int( T ) + .25 * int( OD3 )
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot+.2 ) # FIX
                
            test = input( "Would you like to continue (A/B)? ") 
           
# D WORK DONE
            
        elif CC == 'D':
            if ( int( OD2 ) - int( OD1 ) ) / int( T ) / 10 <= 100.0:
                OD3 = ( int(OD2) - int( OD1 ) ) / 10.0
                c_tot = 60.0 * int( T ) 
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
            elif ( int( OD2 ) - int( OD1 ) ) / int( T ) / 10 > 100:
                OD3 = ( int(OD2) - int( OD1 ) ) / 10.0
                AVG_D = ( OD3 ) / int( T )
                D_OV = AVG_D - 100
                c_BC = 60.0 * int( T )
                c_OV = D_OV * .25 * int( T ) 
                c_tot = c_BC + c_OV
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
                
            test = input( "Would you like to continue (A/B)? ") 
            
# W WORK DONE

        elif CC == 'W':
            T_W = math.ceil( int( T )/7 )
            AVG_WD = ( int(OD2) - int( OD1 ) ) / 10.0 / int( T_W ) 
            if 900 >= AVG_WD:
                OD3 = ( int(OD2) - int( OD1 ) ) / 10.0
                c_tot = 190.0 * T_W
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
            elif 900.0 < AVG_WD < 1500:
                OD3 = ( int(OD2) - int( OD1 ) ) / 10.0
                c_tot = 290.0 * T_W
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
            elif AVG_WD >= 1500 :
                OD3 = ( int(OD2) - int( OD1 ) ) / 10.0
                c_BC = 390 * int( T_W )
                c_OC = (AVG_WD - 1500) * .25 * int( T_W )
                c_tot = c_BC + c_OC
                print( "\nCustomer summary:" )
                print( "\tclassification code:",CC )
                print( "\trental period (days):",T )
                print( "\todometer reading at start:",int( OD1 ) )
                print( "\todometer reading at end:  ",int( OD2 ) )
                print( "\tnumber of miles driven: ",OD3 )
                print( "\tamount due: $",c_tot )
        
            test = input( "Would you like to continue (A/B)? ") 
           
# ERROR WORK
           
        else:
            print("\n\t*** Invalid customer code. Try again. ***")
            CC = input( "\nCustomer code (BD, D, W): " )
            print("\n\t*** Invalid customer code. Try again. ***")
     
    elif test == 'B':
        print("Thank you for your loyalty.")
        break
    
        test = input( "Would you like to continue (A/B)? ") 
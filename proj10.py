#############################################
# 
# CSE 231 Project 09
#
# Initialize Function
#   Create a foundation list of lists and the same for tableau
#   Shuffle Deck
#   Append 6 or 7 cards to each tableau list depending on index
#   Return Foundation List and Tableau List
#
# Valid Move Check Functions
#   Checks based on move
#   T to T
#       Check if Source is empty
#       Check if destination rank is one greater than source
#
#   F to T
#       Check if Source is empty
#       Check if destination rank is one greater than source
#
#   T to F
#       Check if Source is empty
#       Check if destination is empty, if so only Ace
#       Check if same suit as destination
#       Check if destination rank is one greater than source
#
# Move Functions
#   Append card value to destination list
#   Remove card from source list
#
# Check for Win Function
#   Check if all foundation lists are the same length, could fail
#
# Get Option Function
#   Asks for user input
#   Returns option as list and error checks
#
# Main Function
#   Pretty standard 
#   Calls functions when needed
#   Excecutes what each option needs
#   Q ends loop
#
#############################################

#DO NOT DELETE THESE LINES
import cards, random, copy
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

# Initialize WORKING
             
def initialize():
    '''Create Lists for Tablea and Foundation, return the lists'''
    foundation = [[],[],[],[]]
    tableau = [[],[],[],[],[],[],[],[]]
    deck = cards.Deck()
    deck.shuffle()
    n = 0
    for x in range(4):
        for num1 in range(7):
            tableau[n].append(deck.deal())
        for num2 in range(6):
            tableau[n+1].append(deck.deal())
        n += 2
    
    return tableau,foundation


# Display WORKING

def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
 
    
# Valid Tableau to Tableau and Move Tableau to Tableau WORKING
          
def valid_tableau_to_tableau(tableau,s,d):
    '''Checks if move is valid from tableau to tableau, returns True or False'''
    s_card_list = tableau[s]
    d_card_list = tableau[d]
    
    # Source List is Empty
    if len(s_card_list) == 0:
        return False
    
    # Destination List is Empty
    elif len(d_card_list) == 0:
        return True
        
    # Both Lists have Cards
    else:
        s_card = s_card_list[-1].rank()
        d_card = d_card_list[-1].rank()
        
        if s_card < d_card:
            if d_card - s_card == 1:
                return True
            else:
                return False     
        else:
            return False
    
def move_tableau_to_tableau(tableau,s,d):
    '''Moves card from tableau list to tableau list, returns new list'''
    if valid_tableau_to_tableau(tableau,s,d) == True:
        tableau[d].append(tableau[s][-1])
        tableau[s].pop()
        return True
    elif valid_tableau_to_tableau(tableau,s,d) == False:
        return False


# Valid Foundation to Tableau and Move Foundation to Tableau WORKING

def valid_foundation_to_tableau(tableau,foundation,s,d):
    '''Checks if move is valid from foudnation to tableau, returns True or False'''
    s_card_list = foundation[s]
    d_card_list = tableau[d]
    
    # Source List is Empty
    if len(s_card_list) == 0:
        return False
    
    # Destination List is Empty
    elif len(d_card_list) == 0:
        return True
        
    # Both Lists have Cards
    else:
        s_card = s_card_list[-1].rank()
        d_card = d_card_list[-1].rank()
        
        if s_card < d_card:
            if d_card - s_card == 1:
                return True
            else:
                return False     
        else:
            return False
        
def move_foundation_to_tableau(tableau,foundation,s,d):
    '''Moves card from foundation list to tableau list, returns new list'''
    if valid_foundation_to_tableau(tableau,foundation,s,d) == True:
        tableau[d].append(foundation[s][-1])
        foundation[s].pop()
        return True
    elif valid_foundation_to_tableau(tableau,foundation,s,d) == False:
        return False


# Valid Tableau to Foundation and Move Tableau to Foundation WOKRING

def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''Checks if move is valid from tableau to foundation, returns True or False'''
    s_card_list = tableau[s]
    d_card_list = foundation[d]
    
    # Source List is Empty
    if len(s_card_list) == 0:
        return False
    
    # Destination List is Empty
    elif len(d_card_list) == 0:
        if s_card_list[-1].rank() == 1:
            return True
        else:
            return False
        
    # Both Lists Have Cards
    else:
        s_card = s_card_list[-1].rank()
        d_card = d_card_list[-1].rank()
        s_card_suit = s_card_list[-1].suit()
        d_card_suit = d_card_list[-1].suit()

        if s_card > d_card and d_card_suit == s_card_suit:
            if s_card - d_card == 1:
                    return True
            else:
                return False           
        else:
            return False
    
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''Moves card from tableau list to foudnation list, returns new list'''
    if valid_tableau_to_foundation(tableau,foundation,s,d) == True:
        foundation[d].append(tableau[s][-1])
        tableau[s].pop()
        return True
    elif valid_tableau_to_foundation(tableau,foundation,s,d) == False:
        return False


# Check for Win WORKING

def check_for_win(foundation):
    '''Checks if all foundation lists are correct length, returns True or False'''
    return not any(len(foundation[0])!= len(i) for i in foundation)


# Get Option

def get_option():
    '''Asks for user input from menu prompt, error checks response and returns'''
    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
    while True:
        if option.upper() == 'U' or option.upper() == 'R' or option.upper() == 'H' or option.upper() == 'Q':
            return [option.upper()]
        elif len((option).split()) == 3:
            option_list = option.split()
            option_list[0] = option_list[0].upper()
            
            if option_list[0] == 'MTT':
                if int(option_list[1]) not in range(0, 8):
                    print("Error in Source.")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                elif int(option_list[2]) not in range(0, 8):
                    print("Error in Destination")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                else:
                    return option_list
                
            elif option_list[0] == 'MTF':
                if int(option_list[1]) not in range(0, 8):
                    print("Error in Source.")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                elif int(option_list[2]) not in range(0, 4):
                    print("Error in Destination")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                else:
                    return option_list
                    
            elif option_list[0] == 'MFT':
                if int(option_list[1]) not in range(0, 4):
                    print("Error in Source.")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                elif int(option_list[2]) not in range(0, 8):
                    print("Error in Destination")
                    option = input( "\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
                else:
                    return option_list
    
        else:
            print("damn I messed up we gotta go bald")
            option = input( "Input an option (MTT,MTF,MFT,U,R,H,Q):" )


# Main

def main():  
    tableau, foundation = initialize()
    move_lst = [(copy.deepcopy(tableau),copy.deepcopy(foundation))]
    
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    display(tableau, foundation)
    print(MENU)
    while True:
        option = get_option()

        # Tableau to Tableau

        if option[0] == 'MTT':
            s = int(option[1])
            d = int(option[2])
            if valid_tableau_to_tableau(tableau,s,d) is True:
                move_tableau_to_tableau(tableau,s,d)
                display(tableau, foundation)
                move_lst.append((copy.deepcopy(tableau),copy.deepcopy(foundation),copy.deepcopy(option)))

            else:
                print("Error in move:",' , '.join(option))
            
        # Tableau to Foundation
            
        elif option[0] == 'MTF':
            s = int(option[1])
            d = int(option[2])
            if valid_tableau_to_foundation(tableau,foundation,s,d) is True:
                move_tableau_to_foundation(tableau, foundation, s,d)
                if check_for_win(foundation) is True:
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)

                else:
                    display(tableau, foundation)
                    move_lst.append((copy.deepcopy(tableau),copy.deepcopy(foundation),copy.deepcopy(option)))
            else:
                print("Error in move:",' , '.join(option))
            
        # Foundation to Tableau
            
        elif option[0] == 'MFT':
            s = int(option[1])
            d = int(option[2])
            if valid_foundation_to_tableau(tableau,foundation,s,d) is True:
                move_foundation_to_tableau(tableau,foundation,s,d)
                display(tableau, foundation)
                move_lst.append((copy.deepcopy(tableau),copy.deepcopy(foundation),copy.deepcopy(option)))
            else:
                print("Error in move:",' , '.join(option))
        
        # Undo
        
        elif option[0] == 'U':
            if len(move_lst) == 1:
                print("No moves to undo.")
            else:
                print("Undo:",' '.join(move_lst[-1][2]))
                tableau = move_lst[-2][0]
                foundation = move_lst[-2][1]
                display(tableau, foundation)
                move_lst.pop()
                continue
           
        # Restart
                
        elif option[0] == 'R':
            print("\n- - - - New Game. - - - -\n")
            tableau, foundation = initialize()
            display(tableau, foundation)
            print(MENU)
            
        # Help Menu
            
        elif option[0] == 'H':
            print(MENU)
        
        # Quit    
        
        elif option[0] == 'Q':
            break

    print("Thank you for playing.")


# Thing to Make it Work

if __name__ == '__main__':
     main()
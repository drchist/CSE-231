#############################################
# 
# CSE 231 Project 07
# 
# Open File
#   Prompt for file name
#   Test if file is correct
#       Loop until correct input
#   Return file pointer
#
# Read File
#   Reads File
#   Skips first Line
#   Creates Two Lists
#       List of Country Names
#       List of Country Data
#   Return Lists
#
# Histoy of Country
#   Uses the List of Country Data two determine the most common Regime in a Country
#   If two Regimes have the same value, choose the lower of the two
#
# Historical Allies
#   Use a similar method to History of Country to determine all countries that 
# 
# Top Coup
#   Count the number of changes in each countries data in Country Data list
#   Create a new list with tuples containing each country as well as its number of changes
#   Sort this list from highest to lowest based on second value
#   Return only the first inputted number of tuples
#
# Main
#   Pretty standard
#   open_file()
#   read_file()
#   Print MENU and ask for input
#       Error checking
#   Each input (1,2,3) will have error checking while (q) must work with upper and lower
#   1 HISTORY OF COUNTRY
#       Asks for country name
#           Error Checking
#           Find location of name in name list
#           Use that location to obtain the data for the country
#           Find the most common Regime
#           If tie, use the lower number
#           Return Regime Str
#   2 HISTORICAL ALIIES
#       Asks for regime
#           Error Checking
#           Use similar method to history of country
#           Take all countries that share the most common Regime with the input
#           Return lst
#   3 TOP COUP DETAT
#       Asks for int
#           Error Checking
#           Count the number of changes of each countries data
#           Create a new list containing tuples and sort based on number
#           return lst
#   Q Quit
#       Display the end
#       End program
#
#############################################

import csv

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
VOWELS = ('a','e','i','o','u','A','E','I','O','U')
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes     
    '''
    
# OPEN FILE WORKING

def open_file():
    file = input("Enter a file: ")
    while True:
        try:
            open(file,'r')
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
            file = input("Enter a file: ")
    
    return open(file,'r')

# READ FILE WORKING

def read_file(fp):
    reader = csv.reader(fp)
    country_names = []
    list_of_regime_lists = []
    next(reader)
    for row in reader:
        if row[1] not in country_names:
            country_names.append(row[1])
            list_of_regime_lists.append([])
            list_of_regime_lists[-1].append(int(row[4]))
        else:
            list_of_regime_lists[-1].append(int(row[4]))
        
    return country_names,list_of_regime_lists
   
# HISTORY OF COUNTRY WORKING
    
def history_of_country(country,country_names,list_of_regime_lists):
    pos = int(country_names.index(country))
    country_data = list_of_regime_lists[pos]
    num_count = [country_data.count(0),country_data.count(1),country_data.count(2),country_data.count(3)]
    max_count = max(num_count)
    index_list = [index for index in range(len(num_count)) if num_count[index] == max_count]
    index_list.sort()
    return REGIME[index_list[0]]

# HISTORICAL ALIIES WORKING

def historical_allies(regime,country_names,list_of_regime_lists):
    allies_list = []
    n = 0
    for country_data in list_of_regime_lists:
        num_count = [country_data.count(0),country_data.count(1),country_data.count(2),country_data.count(3)]
        max_count = max(num_count)
        index_list = [index for index in range(len(num_count)) if num_count[index] == max_count]
        index_list.sort()
        if REGIME[index_list[0]] == regime:
            allies_list.append(country_names[n])
            n += 1
        else:
            n += 1
    return allies_list
        
# TOP COUP DETAT WORKING

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    n = 0
    top_list = []
    for country_data in list_of_regime_lists:
        coup_count = len([1 for i,x in enumerate(country_data[:-1]) if x!= country_data[i+1] ])
        top_list.append((country_names[n],coup_count))
        n += 1
    top_list.sort(key = lambda x: x[1],reverse=True) 
    return(top_list[:int(top)])
              
# MAIN WORKING

def main():
    file = open_file()
    country_names,list_of_regime_lists = read_file(file)
    print(MENU)
    option = input("Input an option (Q to quit): ")
    
    while True:
        if option == '1':
            country = input("Enter a country: ")
            while True:
                if country in country_names:
                    regime = history_of_country(country,country_names,list_of_regime_lists)
                    if regime.startswith(VOWELS):
                        print("\nHistorically {} has mostly been an {}".format(country,regime))
                        break
                    else:
                        print("\nHistorically {} has mostly been a {}".format(country,regime))
                        break
                else:
                    print("Invalid country. Please try again.")
                    country = input("Enter a country: ")
                    
            print(MENU)
            option = input("Input an option (Q to quit): ")
                
        elif option == '2':
            regime = input("Enter a regime: ")
            while True:
                if regime in REGIME:
                    allies_list = historical_allies(regime,country_names,list_of_regime_lists)
                    print("\nHistorically these countries are allies of type:",regime)
                    print('\n'+(', '.join(allies_list)))
                    break
                else:
                    print("Invalid regime. Please try again.")
                    regime = input("Enter a regime: ")
                    
            print(MENU)
            option = input("Input an option (Q to quit): ")
            
        elif option == '3':
            top = input("Enter how many to display: ")
            while True:
                if int(top.isnumeric()):
                    top_list = top_coup_detat_count(top, country_names,list_of_regime_lists)
                    print("\n{: >25} {: >8}".format("Country","Changes"))
                    for tup in top_list:
                        print("{: >25} {: >8}".format(tup[0],tup[1]))
                    break
                else:
                    print("Invalid number. Please try again.")
                    top = input("Enter how many to display: ")
                    
            print(MENU)
            option = input("Input an option (Q to quit): ")
                   
        elif option.lower() == 'q':
            print("The end.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            option = input("Input an option (Q to quit): ")
    
# Thing to Make it Work

if __name__ == "__main__": 
    main() 
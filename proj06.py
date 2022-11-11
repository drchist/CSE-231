#############################################
# 
# CSE 231 Project 06
#
# Get Option
#   Print Options
#   Prompt for option
#       Loop until correct input
#   Return Option Letter
#
# Open File
#   Prompt for file name
#   Test if file is correct
#       Loop until correct input
#   Return file pointer
#
# Read File
#   Reads file
#   Skip first line
#   Append row in file to master list
#       If values of rank, last week, peak rand, or weeks on is not int, replace with -1
#       int values of rank, last week, peak rand, and weeks on
#       if length of song values is greater than 6, remove the rest
#   Return master list
#
# Get Christmas Songs
#   Goes through song titles
#   If any words in CHRISTMAS WORDS 
#       Append to new list
#   Return new list
#
# Sort by Peak
#   Sort the master list by index 4
#   Return Master List
#
# Sort by Weeks on List
#   Sort the master list by index 5
#   Return Master List
#
# Song Score
#   Assign scores to each song
#
# Sort by Score
#   Sort songs by their scores
#
#############################################

import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()

CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()

TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation

A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed

OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option

PROMPT = "Enter one of the listed options: "


# Get Option WORKING

def get_option():
    print(OPTIONS)
    option = input(PROMPT)
    option = option.lower()
    while True:
        if option == 'a' or option == 'b' or option == 'c' or option == 'd' or option == 'q':
            return option
        else:
           print("Invalid option!\nTry again")
           option = input(PROMPT)
           option = option.lower()

# Open File WORKING

def open_file():
    file = input("Enter a file name: ")
    while True:
        try:
            open(file,'r')
            break
        except FileNotFoundError:
            print("\nInvalid file name; please try again.\n")
            file = input("Enter a file name: ")
    
    return open(file,'r')
    
# Read File WORKING

def read_file(fp):
    reader = csv.reader(fp)
    master_list = []
    next(reader)
    for row in reader:
        master_list.append(row)
    
    for song in master_list:
        
# Change Invalid Values

        for i in range(2,len(song)):
            try:
                int(song[i])
            except:
                song[i] = -1
                
# Int Values
                
        song[2] = int(song[2])
        song[3] = int(song[3])
        song[4] = int(song[4])
        song[5] = int(song[5])
        
# Make sure all are length = 6

        if len(song) > 6:
            del song[6:]
        
    return master_list   

# Print Data WORKING

def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

# Get Christmas Songs WORKING

def get_christmas_songs(master_list):
    lis = []
    for song in master_list:
        title = song[0].lower()
        if any(CHRISTMAS_WORDS in title for CHRISTMAS_WORDS in CHRISTMAS_WORDS):
            lis.append(song) 
    lis.sort()
    return lis
            
# Sort by Peak WORKING

def sort_by_peak(master_list):
    n = 0
    for song in master_list:
        if song[4] == -1:
            master_list.pop(n)
        n +=1    
    master_list.sort(key=lambda x: x[4])
    return master_list

# Sort by Weeks on List WORKING

def sort_by_weeks_on_list(master_list):
    n = 0
    for song in master_list:
        if song[5] == -1:
            master_list.pop(n)
        n +=1    
    '''Insert Docstring here'''
    pass
    master_list.sort(key=lambda x: x[5])
    master_list.reverse()
    return master_list

# Song Score WORKING
    
def song_score(song):
    if song[2] == -1:
        curr_rank = -100
    else:
        curr_rank = 100 - song[2]
    if song[4] == -1:
        peak_rank = -100
    else:
        peak_rank = 100 - song[4]
    rank_delta = song[2] - song[3]
    weeks_on_chart = song[5]
    score = A * peak_rank + B * rank_delta + C * weeks_on_chart + D * curr_rank
    return score

# Sort by Score

def sort_by_score(master_list):
    score_list = []
    for song in master_list:
        score_list.append(song_score(song))
    combined_list = zip(score_list,master_list)
    master_list = sorted(combined_list)
    return master_list
        
# Main Working
    
def main():
    print("\nBillboard Top 100\n")
    file = open_file()
    master_list = read_file(file)
    print_data(master_list)
    option = get_option()
    
    while True:
        if option == 'a':
            chr_lis = get_christmas_songs(master_list)
            if chr_lis == []:
                print_data(chr_lis)
                print('None of the top 100 songs are Christmas songs.' )
            else:
                print_data(chr_lis)
                per = (len(chr_lis)/len(master_list))*100
                print('\n{:d}% of the top 100 songs are Christmas songs.'.format(int(per)))       
            option = get_option()
            
        elif option == 'b':
            print_data(sort_by_peak(master_list))
            option = get_option()
        
        elif option == 'c':       
            print_data(sort_by_weeks_on_list(master_list))
            option = get_option()
            
        elif option == 'd':
            print_data(sort_by_score(master_list))
            option = get_option()
            
        elif option == 'q':
            print("\nThanks for using this program!\nHave a good day!\n")
            break
  
# Thing to Make it Work

if __name__ == "__main__":
    main()           
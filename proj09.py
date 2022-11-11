#############################################
# 
# CSE 231 Project 09
#
# Get Option
#   Print MENU   
#   Prompts user for option
#       Error checking
#       Return option
#
# Open File
#   Takes string input for print
#   Prompts user for file name
#       Error checking
#       Return file pointr
#
# Read Annotated File
#   Takes json file pointer
#   Returns loaded file
#
# Read Category File
#   Takes category file pointer
#   Creates new dictionary with values from category file
#   Returns Catogory Dictionary
#
# Collect Category Set
#   Takes d_annot and d_cat
#   Returns set of strings contained in both the d_cat keys and d_annot 'bbox_category_label'
#
# Collect Image List for Categories
#   Creates a dicitonary from cat_set with keys as category strings
#   Iterates through d_annot and pulls 'bbox_category_label'
#   If the num for the category string is contained within 'bbox_category_label' then append image ID to dictionary
#   Return Dictionary of Images
#
# Max Instances for Item
#   Returns longest list in dictionary of images counting all values in list
#
# Max Images for Item
#   Returns longest list in dictionary of iamges without repeating ID
#
# Word Count
#   Creates dictionary of unique words not contained within STOP_WORDS
#   Returns list of tuples of the unique words and their counts
#
# Main
#   Pretty standard
#   Calls functions
#   Error checks for required inputs
#   Prints closing message when q is entered
#
#############################################

import json,string

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''
    
OPTIONS ="cfimwq"


# Get Option WORKING
def get_option():
    '''Prompts user for option in menu, returns option'''
    option = input(MENU).lower()
    while True:
        if option in OPTIONS:
            return option
        else:
            print("Incorrect choice.  Please try again.")
            option = input(MENU).lower()
    
    
# Open File WORKING
def open_file(s):
    ''' Prompts user for file name, file pointers'''
    file = input("Enter a {} file name: ".format(s))
    while True:
        try:
            fp = open(file, 'r')
            break
        except FileNotFoundError:
            print("File not found.  Try again.")
            file = input("Enter a {} file name: ".format(s))
           
    return fp
       
 
# Read Annotated File WORKING
def read_annot_file(fp):
    '''Takes json file pointer and creates dictionary of dictionaries'''
    return json.load(fp)


# Read Category File WORKING
def read_category_file(fp):
    '''Takes category file pointer and creates dictionary of ints and strings'''
    d_cat = {}
    for line in fp: 
        line = line.strip()
        line = line.split()
        (key, value) = (line[0],line[1])
        d_cat[int(key)] = value
    return d_cat


# Collect Catogorey Set WORKING
def collect_catogory_set(d_annot,d_cat):
    '''Takes both dicionaries as input, returns set of catogory strings'''
    annot_cat_list = []
    cat_set = set()
   
    for image, info in d_annot.items():
        for key in info:
            annot_cat_list.extend(info['bbox_category_label'])
           
    annot_cat_set = set(annot_cat_list)
   
    for num in annot_cat_set:
        for key in d_cat:
            if num == key:
                cat_set.add(d_cat[key])
              
    return cat_set
       

# Collect Image List for Categories WORKING
def collect_img_list_for_categories(d_annot,d_cat,cat_set):
    '''Creates a dictionary from category set and adds a list of all images with that category'''
    d_image = {}
    for cat in cat_set:
        d_image[cat] = []
    
    for image in d_annot:
        for num in d_annot[image]['bbox_category_label']:
            if ( num in d_cat.keys() ) and ( d_cat[num] in d_image.keys() ):
                d_image[d_cat[num]].append(image)
                          
    return d_image


# Max Instances for Item
def max_instances_for_item(d_image):
    '''Returns the category with the most instances in images and the number of instances in category'''
    return (len(d_image[max(d_image, key=lambda x:len(d_image[x]))]), max(d_image, key=lambda x:len(d_image[x])))


# Max Images for Item
def max_images_for_item(d_image):
    '''Returns the category with the most unique instances in images and the number of instances in category'''
    return (len(max(d_image, key=lambda x:len(set(d_image[x])))), max(d_image, key=lambda x:len(set(d_image[x]))))


# Count Words WORKING
def count_words(d_annot):
    '''Counts the number of unique words and skips all words in STOP_WORDS, returns list of tuples'''
    cap_str = ''
    word_dict = {}
    fin_list = []
    
    for image in d_annot.keys():
        for key in d_annot[image].keys():
            if key == 'cap_list':
                cap_str += ' '.join(d_annot[image][key])

    for char in string.punctuation:
        cap_str = cap_str.replace(char, ' ')    
    
    cap_word_list = cap_str.split()
    word_list = [x for x in cap_word_list if x not in STOP_WORDS]
    
    for word in word_list:
        # Was getting a weird issue with a few words getting combined with 'a' at the end
        if word[-1] == 'a':
            word = word[0: (len(word) - 1)]
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    for key,value in word_dict.items():
        fin_list.append((value,key))
        
    fin_list.sort(reverse=True)
    return fin_list


# Main WORKING
def main():    
    print("Images\n")
    d_annot = read_annot_file(open_file("JSON image"))
    d_cat = read_category_file(open_file("category"))
    cat_set = collect_catogory_set(d_annot,d_cat)
    cat_list = list(cat_set)
    cat_list.sort()
    d_image = collect_img_list_for_categories(d_annot,d_cat,cat_set)
    
    while True:
        option = get_option()
        if option == 'c':
            print("\nCategories:")
            print(', '.join(cat_list))
            
        elif option == 'f':
            print("\nCategories:")
            print(', '.join(cat_list))
            category = input("Choose a category from the list above: ")
            while True:
                if category in d_image.keys():
                    print("\nThe category {} appears in the following images:".format(category))
                    image_list = list(set(d_image[category]))
                    image_list.sort()
                    print(', '.join(image_list))
                    break
                else:
                    print("Incorrect category choice.")
                    category = input("Choose a category from the list above: ")
                
        elif option == 'i':
            max_tup = max_instances_for_item(d_image)
            print("\nMax instances: the category {} appears {} times in images.".format(max_tup[1],max_tup[0]))
            
        elif option == 'm':
            max_tup = max_images_for_item(d_image)
            print("\nMax images: the category {} appears in {} images.".format(max_tup[1],max_tup[0]))
            
        elif option == 'w':
            word_list = count_words(d_annot)
            num = input("\nEnter number of desired words: ")
            while True:
                try:
                    int(num)
                    break
                except:
                    print("Error: input must be a positive integer: ")
                    num = input("\nEnter number of desired words: ")
                    
            print_list = word_list[:int(num)]
            
            print("\nTop {} words in captions.".format(num))
            print("{:<14s}{:>6s}".format("word","count"))
            for tup in print_list:
                print("{:<14s}{:>6d}".format(tup[1],tup[0]))
                    
        elif option == 'q':
            break
    
    print("\nThank you for running my code.") 
    
    
# Thing to Make it Work
if __name__ == "__main__":
    main()     
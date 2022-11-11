#############################################
# 
# CSE 231 Project 08
#
# Open File
#   Prompt for file name
#   Test if file is correct
#       Loop until correct input
#   Return file pointer
#
# Read File
#   Create new dictionary
#   Reads row by row
#   If region dne in dict
#       Create new key
#       append region data
#       if region in dict
#           append country data
#   Return Master Dictionary
#
# Add Per Capita
#   Append every country data with per capita diabetes data
#   For region in master
#       For country in region
#           Append each list with data
#   Return New Master Dictionary
#
# Max in Region
#   Find and return the max per capita value tuple
#
# Min in Region
#   Find and return the min per capita value tuple excluding zeros
#
# Display Region
#   Display region data, then loop to print country data 
#
# Main
#   Pretty standard
#   Call open file into read file to make master dictionary
#   Master dictionary into append per capita to add values
#   Get list of regions in dictionary
#   Print data for every region in dictionary
#       Master dictionary to display region
#       Display data from max in region and min in region
#   Display closing message
#
#############################################

import csv

# Open File WORKING

def open_file():
    '''prompts for file name and returns file pointer'''
    file = input("Input a file: ")
    while True:
        try:
            fp = open(file, 'r', encoding="utf8")
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
            file = input("Input a file: ")
    
    return fp

# Read File WORKING

def read_file(fp):
    '''reads file and returns dictionary with regions as key and a list of lists of country data'''
    master_dict = {}
    reader = csv.reader(fp)
    next(reader)
    for row in reader:
        region = row[1]
        country = row[2]
        pop = row[5].replace(',','')
        diabetes = row[9]
        
        try:
            float(pop)
        except:
            continue
        try:
            float(diabetes)
        except:
            continue
        
        country_data = [country,float(diabetes),float(pop)]
        if region not in master_dict:
            master_dict[region] = []
            master_dict[region].append(country_data)
        else:
            master_dict[region].append(country_data)
            
        master_dict[region].sort()
    
    return master_dict

# Add per Capita WORKING

def add_per_capita(master_dict):
    '''appends per capita diabetes values to each countries data'''
    for region in master_dict:
        region_data = master_dict[region]
        for country_data in region_data:
            per_cap = country_data[1] / country_data[2]
            country_data.append(per_cap)
           
    return master_dict

# Max in Region WORKING

def max_in_region(master_dict,region):
    '''locates and returns the maximum per capita value from each region'''
    max_lst = max(master_dict[region], key=lambda x: x[3])
    return (max_lst[0],max_lst[3])
    
# Min in  WORKING

def min_in_region(master_dict,region):
    '''locates and returns the minium per capita value from each region'''
    no_zero = list(filter(lambda x: x[3] > 0 ,master_dict[region]))
    min_lst = min(no_zero, key=lambda x: x[3])
    return (min_lst[0],min_lst[3])

# Display Region WORKING

def display_region(master_dict,region):
    '''displays each countries data within each region'''
    for index,country_data in enumerate(master_dict[region]):
        if country_data[0] == region:
            region_data = master_dict[region][index]
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(region,region_data[1],region_data[2],region_data[3]))
    
    print("\n{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))
    region_data = master_dict[region].sort(key=lambda x: x[3],reverse=True)
    for country_data in master_dict[region]:
        if country_data[0] != region:
            print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(country_data[0],country_data[1],country_data[2],country_data[3]))
        else:
            continue
    
# Main WORKING
    
def main():
    master_dict = read_file(open_file())
    master_dict = add_per_capita(master_dict)
    region_list = list(master_dict.keys())
    for region in region_list:
        print("Type1 Diabetes Data (in thousands)")
        display_region(master_dict,region)
        max_tup = max_in_region(master_dict,region)
        min_tup = min_in_region(master_dict,region)
        
        print("\nMaximum per-capita in the {} region".format(region))
        print("{:<37s} {:>11s}".format("Country","Per Capita"))
        print("{:<37s} {:>11.5f}".format(max_tup[0],max_tup[1]))
        
        print("\nMinimum per-capita in the {} region".format(region))
        print("{:<37s} {:>11s}".format("Country","Per Capita"))
        print("{:<37s} {:>11.5f}\n".format(min_tup[0],min_tup[1]))
        
        
        print("-"*72)
        
    print('\n Thanks for using this program!\nHave a good day!')

# Thing to Make it Work    
        
if __name__ == "__main__": 
    main()
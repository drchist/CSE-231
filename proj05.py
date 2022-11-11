#############################################
# 
# CSE 231 Project 05
#
# open_file()
#   Promt for year
#   Create string with year 
#   WHile, Try, Except loop to make sure valid year
#   Reutnr file pointer
#
# get_month_str(mm)
#   Takes month input
#   Returns three letter month str from numerical value
#
# best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd)
#   Takes value of wvht and compares to best whvt
#       If wvht > best wvht
#           replace old values
#       Elif wvht < best wvht
#           continue
#       Eliff wvht = best wvht
#           compare dpd to best dpd
#               If dpd > best dpd
#                   replace old values
#               Elif dpd < best dpd
#                   continue
#                   
# main()
#   Call open_file()
#   Find avg, min, max of wvht
#       Add all wvht to list and avg
#       Compare whvt to min, replace if smallet
#       Compare wvht to max, replace if larget
#   Call best_surf()
#   Call get_month_str()
#   Print Everything
#
#############################################

import statistics

# Open File WORKING

def open_file():
    year = input("Input a year: ")
    filename = 'wave_data_'+year+'.txt'
    while True:
        try:
            open(filename,'r')
            break
        except FileNotFoundError:
            print("File does not exist. Please try again.")
            year = input("Input a year: ")
            filename = 'wave_data_'+year+'.txt'
    
    file = open(filename,'r')
    file.readline()
    file.readline()
    return file

# Get Month WORKING
    
def get_month_str(mm):
    if mm == '01':
        return str('Jan')
    elif mm == '02':
        return str('Feb')
    elif mm == '03':
        return str('Mar')
    elif mm == '04':
        return str('Apr')
    elif mm == '05':
        return str('May')
    elif mm == '06':
        return str('Jun')
    elif mm == '07':
        return str('Jul')
    elif mm == '08':
        return str('Aug')
    elif mm == '09':
        return str('Sep')
    elif mm == '10':
        return str('Oct')
    elif mm == '11':
        return str('Nov')
    elif mm == '12':
        return str('Dec')
    
# Best Surf WORKING
    
def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    mm = str(mm)
    dd = str(dd)
    hr = int(hr)
    wvht = float(wvht)
    dpd = float(dpd)
    
# Time Check
    
    if hr <= 6 or hr >= 19:
        return best_mm,best_dd,best_hr,best_wvht,best_dpd
    else: 
        
# wvht Check

        if wvht < best_wvht:
            return best_mm,best_dd,best_hr,best_wvht,best_dpd
        
        elif wvht > best_wvht:
            best_mm = mm
            best_dd = dd
            best_hr = hr
            best_wvht = wvht
            best_dpd = dpd
            return best_mm,best_dd,best_hr,best_wvht,best_dpd
        
        elif wvht == best_wvht:
            
# dpd Check
            
            if dpd < best_dpd:
                return best_mm,best_dd,best_hr,best_wvht,best_dpd
            
            elif dpd > best_dpd:
                best_mm = mm
                best_dd = dd
                best_hr = hr
                best_wvht = wvht
                best_dpd = dpd
                return best_mm,best_dd,best_hr,best_wvht,best_dpd
    
# Main WORKING
    
def main():  
    
# Variables

    best_mm = str('test')
    best_dd = str('test')
    best_hr = int(0)
    best_wvht = float(0)
    best_dpd = float(0)
    wav_tot = []
    wav_min = int(10**6)
    wav_max = 0
    
# Main Main WORKING

    print("Wave Data")
    for line in open_file():
        line = line.strip()
        lis = line.split()
        mm = str(lis[1])
        dd = str(lis[2])
        hr = int(lis[3])
        wvht = float(lis[8])
        dpd = float(lis[9])
        
# Avg, Max, Min WORKING

        if wvht == 99.00 or dpd == 99.00:
            continue
        elif float(wav_min) > wvht:
            wav_min = wvht
            wav_tot.append(wvht)
        elif float(wav_max) < wvht:
            wav_max = lis[8]
            wav_tot.append(wvht)
        else:
            wav_tot.append(wvht)

# Best Surf WORKING

        best_mm,best_dd,best_hr,best_wvht,best_dpd = best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd)
        adj_mm = get_month_str(best_mm)
        
# Print WOKRING

    wav_avg = statistics.mean(wav_tot)
    wav_max = float(wav_max)
    wav_min = float(wav_min)
    print("\nWave Height in meters.")
    print("{:7s}: {:4.2f} m".format("average",wav_avg))
    print("{:7s}: {:4.2f} m".format("max",wav_max))
    print("{:7s}: {:4.2f} m".format("min",wav_min))
    
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(adj_mm,best_dd,best_hr,best_wvht,best_dpd))

# This Thing

if __name__ == "__main__": 
    main()
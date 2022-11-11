#############################################
# 
# CSE 231 Project 10
#
# Check Time
#   Checks to make sure time and duration are correct format
#   Checks that time is between certain times
#   Add duration to time before check
#
# Event Prompt
#   Prompts user for input on MENU
#   Reprompt until correct input
#
# Main
#   Creates calendar
#   While True
#       Calls event prompt
#       Does what event prompt returns
#       Error checks and returns invalid x for whatever is done
#       Quits on q
#
#############################################

from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

# Check Time

def check_time(time,duration):
    '''Checks to make sure time and duration are correct form'''
    
    # Time Checking
    try:
        if time != None:
            time_list = [int(x) for x in time.split(':')]
            if (360 <= (time_list[0]*60 + time_list[1] + duration) <= 1020):
                time = time
            else:
                time = None
    except:
        time = None
    
    # Duration Checking
    try:
        if duration > 0:
            duration = duration
        else:
            duration = None
    except:
        duration = None
        
    if time == None or duration == None:
        return False
    else:
        return True

# Event Prompt WORKING

def event_prompt():
    '''Prompts user for imput, returns input'''
    print(MENU)
    option = input("Select an option: ").lower()
    while True:
        if option == 'a' or option == 'd' or option == 'l' or option == 'q':
            return option
        else:
            print("Invalid option. Please try again.")
            option = input("Select an option: ").lower()
    
# Main
             
def main():
    calendar = P11_Calendar()
    while True:
        option = event_prompt()
        if option == 'a':
            date = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            duration = int(input("Enter the duration in minutes (int): "))
            cal_type = input("Enter event type ['meeting','event','appointment','other']: ")
            while True:
                event = P11_Event(date,time,duration,cal_type)
                if (check_time(time,duration) == True) and (calendar.add_event(event) == True):
                    print("Add Event")
                    print("Event successfully added.")
                    break
                else:
                    print("Invalid event. Please try again.")
                    date = input("Enter a date (mm/dd/yyyy): ")
                    time = input("Enter a start time (hh:mm): ")
                    duration = int(input("Enter the duration in minutes (int): "))
                    cal_type = input("Enter event type ['meeting','event','appointment','other']: ")
                    continue
     
        elif option == 'd':
            print("Delete Event")
            date = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            if (check_time(time,duration) == True) and (calendar.delete_event(date,time) == True):
                print("Event successfully deleted.")
            else:
                print("Event was not deleted.")
            
            
        elif option == 'l':
            print("List Events")
            date = input("Enter a date (mm/dd/yyyy): ")
            day_schedule = calendar.day_schedule(date)
            day_schedule.sort()
            if len(day_schedule) == 0:
                print("No events to list on ",date)
            else:
                for event in day_schedule:
                    print(event)
            
        elif option == 'q':
            break




# Thing to Make it Work

if __name__ == '__main__':
     main()

# WORKING ENITELY

class P11_Calendar():
    def __init__(self):
        '''Creates an event list to hold all events'''
        self.event_list = []
        
        
    def add_event(self,e):
        '''Adds event to event list if it does not have any conflicts'''
        if len(self.event_list) == 0:
            self.event_list.append(e)
            return True
        else:
            e_time_range = e.get_time_range()
            for event in self.event_list:
                event_time_range = event.get_time_range()
                if event_time_range[0] <= e_time_range[0] <= event_time_range[1]:
                    return False
                elif event_time_range[0] <= e_time_range[1] <= event_time_range[1]:
                    return False
                else:
                    self.event_list.append(e)
                    return True 
        
    
    def delete_event(self,date,time):
        '''Deletes an event from the event list if it exists'''
        n = 0
        for event in self.event_list:
            if (date == event.get_date()) and (time == event.get_time()): 
                self.event_list.pop(n)
                return True
            else:
                n += 1
                continue
        return False
    
    
    def day_schedule(self,date):
        '''Returns list of events from a given date'''
        date_event_list = []
        for event in self.event_list:
            if date == event.get_date():
               date_event_list.append(event)
               
        return date_event_list
   
        
    def __str__(self):
        '''Returns string of header and all events'''
        calendar_str = 'Events in Calendar:\n'
        for event in self.event_list:
            calendar_str += event.__str__()+'\n'
            
        return calendar_str
    
    
    def __repr__(self):
        '''Provided: returns a string of events on one line separated by semicolons'''
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True
        
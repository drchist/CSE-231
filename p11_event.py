CAL_TYPE = ['meeting','event','appointment','other']

# WORKING ENITELY

class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        '''Initializes and checks all variables in the class'''

        # Date Checking
        try:
            date_list = [int(x) for x in date.split('/')]
            if (1 <= date_list[0] <= 12) and (1 <= date_list[1] <=31) and (0 <= date_list[2] <= 9999):
                self.date = date
            else:
                self.date = None
        except:
            self.date = None
            
        # Time Checking
        try:
            if time != None:
                time_list = [int(x) for x in time.split(':')]
                if (0 <= time_list[0] <= 23) and (0 <= time_list[1] <= 59):
                    self.time = time
                else:
                    self.time = None
        except:
            self.time = None
        
        
        # Duration Checking
        try:
            if duration > 0:
                self.duration = duration
            else:
                self.duration = None
        except:
            self.duration = None
        
        
        # Type Checking
        if cal_type.lower() in CAL_TYPE:
            self.cal_type = cal_type
        else:
            self.cal_type = None

        # None Checking
        if (self.date == None) or (self.time == None) or (self.duration == None) or (self.cal_type == None):
            self.valid = False
        else:
            self.valid = True
    
    
    def get_date(self):
        '''Returns date'''
        return self.date
       
    
    def get_time(self):
        '''Returns time'''
        return self.time
        
     
    def get_time_range(self):
        '''Creates a tuple of start and end times for the event'''
        if self.duration != None:
            start_time = self.time
            start_time = start_time.split(':')
            start_min = int(start_time[0])*60 + int(start_time[1])
            return (start_min, start_min + self.duration)
        
    
    def __str__(self):
        '''Creates a string of the event data'''
        return '{}: start: {}; duration: {}'.format(self.date,self.time,self.duration)
   
 
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'


    def __lt__(self,e):
        '''Checks is self time is less than e time'''
        self_time = self.time
        self_time = self_time.split(':')
        self_min = int(self_time[0])*60 + int(self_time[1])
        
        e_time = e.time
        e_time = e_time.split(':')
        e_min = int(e_time[0])*60 + int(e_time[1])
        
        if self_min < e_min:
            return True
        else:
            return False
    
  
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and self.duration == e.duration and self.cal_type == e.cal_type # and self.status == e.status
      
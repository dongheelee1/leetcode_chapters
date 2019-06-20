class Solution:
    def nextClosestTime(self, time: str) -> str:
        '''
        # 00:00 = hour:minutes 
        
        #allowed digits 
        allowed_digits = {int(x) for x in time if x != ':'}
        
        
        #convert given time to minutes 
        time_minutes = 60*int(time[:2]) + int(time[3:])
        
        #simulate a clock 
        while True: #while we haven't found a time 
            
            #add 1 to the current time and check if it is valid 
            time_minutes = (time_minutes + 1) % (24*60)
            
            
            hour_first_digit = (time_minutes / 60) / 10 
            if hour_first_digit not in allowed_digits: 
                continue
            hour_second_digit = (time_minutes / 60) % 10  
            if hour_second_digit not in allowed_digits: 
                continue
            minutes_first_digit = (time_minutes % 60) / 10
            if minutes_first_digit not in allowed_digits: 
                continue
            minutes_second_digit = (time_minutes % 60) % 10 
            if minutes_second_digit not in allowed_digits: 
                continue
            return str(hour_first_digit) + str(hour_second_digit) + ":" + str(minutes_first_digit) + str(minutes_second_digit)
            
        '''
        import datetime
        digits = set(time)
        while True:
            time = (datetime.strptime(time, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:
                return time

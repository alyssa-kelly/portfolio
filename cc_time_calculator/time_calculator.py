def add_time(start_time, add_time, weekday = None):
    # creating variables from function input
    start_string = start_time.split(":")
    start_hour = int(start_string[0])
    start_piece = start_string[1]
    start_minute = int(start_piece.split()[0])
    start_meridiem = start_piece.split()[1]
    add_string = add_time.split(":")
    add_hour = int(add_string[0])
    add_minute = int(add_string[1])
    carry_hour = ""
    end_hour = ""
    end_minute = ""
    end_meridiem = ""
    days_later = 0
    if weekday:
        weekday = weekday.lower()
    
    # conversion to military time if start time is after noon
    if start_meridiem == "PM":
        start_hour = start_hour + 12
    
    # minute math
    sum_minute = start_minute + add_minute
     
    if sum_minute > 59:
        end_minute = sum_minute % 60    
        carry_hour = sum_minute // 60
    else:
        end_minute = sum_minute 
        carry_hour = 0
    
    # adds in 0s to minute display if necessary  
    if len(str(end_minute)) == 1:
        end_minute = "0" + str(end_minute)
    elif len(str(end_minute)) == 0:
        end_minute = "00"
    
    # hour math
    sum_hour = add_hour + carry_hour
    end_hour = start_hour + sum_hour
 
    # Reducing down hours when adding multiple days
    if end_hour >= 24:
        if sum_hour % 24 == 0:
            days_later = end_hour // 24
            end_hour = start_hour
        else:
            days_later = end_hour // 24
            end_hour = (end_hour % 24)

    # converts military back to standard if necessary & adds meridiem   
    if end_hour == 0:
        end_hour = "12"
        end_meridiem = "AM"
    elif end_hour == 12:
        end_meridiem = "PM"
    elif (12 < end_hour < 24):
        end_hour = int(end_hour) - 12
        end_meridiem = "PM"
    else:
        end_meridiem = "AM"
    
    # days of the week optional argument
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if weekday:
        start_index = weekdays.index(weekday)
        end_index = start_index + days_later

        if end_index > 6:
            end_index = (end_index % 7)
            
        end_day = weekdays[end_index]

    # basic return string
    end_time = str(end_hour) + ":" + str(end_minute) + " " + str(end_meridiem)
    end_string = end_time
    
    # return string w optional weekday argument
    if weekday != None:
        end_string = str(end_string) + ", " + str(end_day.capitalize())
    
    # adding days later parentheses when necessary
    if int(days_later) == 1:
        end_string = str(end_string) + " (next day)"
        
    if int(days_later) > 1:
        days_later_string = "(" + str(days_later) + " days later)"
        end_string = str(end_string) + " " + str(days_later_string)
        
    print(end_string)
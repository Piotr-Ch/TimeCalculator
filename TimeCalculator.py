def add_time(start_time, duration_time, *args):

    spl_starttime = start_time.split()
    spl_starttime2 = spl_starttime[0].split(':')
    #upgrade: iteration in start_time and duration_time, find only digits/append to list
    start_hour = spl_starttime2[0]
    start_minutes = spl_starttime2[1]
    start_AMPM = spl_starttime[1]

    spl_durationtime = duration_time.split(':')
    duration_hour = spl_durationtime[0]
    duration_minutes = spl_durationtime[1]

    #upgrade: make int() earlier; in start_hour, start_minutes, duration_hour, duration_minutes
    start_hour_int = int(start_hour)
    duration_hour_int = int(duration_hour)

    sum_hours = start_hour_int + duration_hour_int
    hour_start = 0

    if start_AMPM == 'AM':
        AMPM = 1
    else:
        AMPM = 2

    #counting hours
    number_of_days = duration_hour_int // 24
    if duration_hour_int > 24:
        hours_rest = duration_hour_int - number_of_days * 24
        #print(hours_rest)
        if hours_rest > 12:
            hours_rest1 = hours_rest - 12
            diff_hours = 12 - start_hour_int
            #print('A')
            if hours_rest1 < diff_hours:
                hour = start_hour_int + hours_rest1
                #print('1')
                if start_AMPM == 'PM' or hour == 11:
                    AMPM += 1
                    number_of_days += 1
                else:
                    AMPM += 0

            elif hours_rest1 == diff_hours:
                hour = start_hour_int + diff_hours
                #print('2')
                AMPM += 0
                number_of_days += 1

            else:
                hour = hour_start + hours_rest1 - diff_hours
                #print('3')
                if start_AMPM == 'PM':
                    AMPM += 0
                    number_of_days += 1
                else:
                    AMPM += 1

        elif hours_rest == 12:
            hour = start_hour_int
            #print(':')

        else:
            diff_hours = 12 - start_hour_int
            if hours_rest < diff_hours:
                hour = start_hour_int + hours_rest
                #print('A')
                if start_AMPM == 'PM':
                    AMPM += 0
                else:
                    AMPM += 1

            elif hours_rest == diff_hours:
                hour = start_hour_int + diff_hours
                #print('B')
                if start_AMPM == 'PM':
                    AMPM += 1
                    number_of_days += 1
                else:
                    AMPM += 0

            else:
                hour = hour_start + hours_rest-diff_hours
                if start_AMPM == 'PM':
                    AMPM += 1
                    number_of_days += 1
                else:
                    AMPM += 0
                #print('C')

    elif duration_hour_int == 24:
        number_of_days = 1
        hour = start_hour_int
        AMPM += 0
        #print('::')

    else:
        if sum_hours > 12: # sum_hours = start_hour_int + duration_hour_int
            diff_hours = sum_hours - 12 #maybe use recursion here?
            if diff_hours > 12:
                diff_hours = diff_hours - 12
                hour = hour_start + diff_hours
                #print('AA')
                if start_AMPM == 'PM':
                    AMPM += 0
                else:
                    AMPM += 1

            elif diff_hours == 12:
                hour = hour_start + diff_hours
                AMPM += 0
                #print('AB')
                number_of_days += 1

            else:
                hour = hour_start + diff_hours
                #print('AC')
                if start_AMPM == 'PM':
                    AMPM += 1
                    number_of_days += 1
                else:
                    AMPM += 0

        elif sum_hours == 12:
            hour = sum_hours
            #print('AD')
            AMPM += 1
            number_of_days += 1

        else:
            hour = sum_hours
            #print('AE')
            AMPM += 0



    #counting minutes
    minutes = int(start_minutes) + int(duration_minutes)
    if minutes > 60:
        #print(number_of_days)
        #print(AMPM)
        #print(hour)
        #print(start_hour_int)
        #print(duration_hour_int)
        if AMPM%2!=0 and  start_hour_int == 11 and start_hour_int + duration_hour_int > 10:
            hour += 1
            minutes -= 60
            AMPM += 1
            number_of_days += 0
            #print("aaaaa")
            #print(number_of_days)

        else:
            hour += 1
            minutes -= 60
            AMPM += 1
            number_of_days += 1
            #print('bbbbbb')
            #print(number_of_days)

    elif minutes == 60:
        hour += 1
        minutes = 0
        AMPM += 1


    #------AMPM MODULE------(checking AM or PM (AM=odd number, PM=even number))
    if AMPM%2==0:
        AMPM = 'PM'
    else:
        AMPM = 'AM'


    # ----- DAY MODULE----- ( to check which day is the ending one )
    day_key = 0

    week_table = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
                      6: 'Saturday', 7: 'Sunday'}
    week_table2 = {'monday': '1', 'tuesday': '2', 'wednesday': '3', 'thursday': '4', 'friday': '5',
                       'saturday': '6', 'sunday': '7'}

    if args:
        #if number_of_days >= 1: # maybe add this line to another AND condition in line below
        if number_of_days == 0:
            day_key = int(week_table2[args[0].lower()])

        elif number_of_days < 7 and number_of_days >=1:
            diff_day = 7 - int(week_table2[args[0].lower()])
            #print(diff_day)
            #print(number_of_days)
            if number_of_days > diff_day:
                diff = number_of_days - diff_day
                day_key += diff
            elif number_of_days == diff_day:
                day_key = int(week_table2[args[0].lower()]) + diff_day
            else:
                day_key = int(week_table2[args[0].lower()]) + number_of_days

        elif number_of_days == 7:
            day_key = int(week_table2[args[0].lower()])

        elif number_of_days > 7: # add this?: and number_of_days < 14
            number_of_days1 = number_of_days//7
            #print(number_of_days1)
            number_of_days2 = number_of_days1*7
            #print(number_of_days2)
            number_of_days3 = number_of_days - number_of_days2
            #print(number_of_days3)
            day_key = int(week_table2[args[0].lower()]) + number_of_days3
            #print(day_key)

        #elif number_of_days == 0:

            if day_key > 7:
                day_key1 = day_key // 7
                #print(day_key1)
                day_key2 = day_key1 * 7
                #print(day_key2)
                day_key3 = day_key - day_key2
                day_key = day_key3

            #elif day_key == 7:
        day = week_table[day_key]
        #print(day)

#------COUNTING DAY MODULE------(checking day)
    if number_of_days == 0:
        count_day = ''
    elif number_of_days == 1:
        count_day = '(next day)'
    elif number_of_days > 1:
        count_day = '(%d days later)' % number_of_days


    #---------RESULT------------
    #checking if minutes is single or double digit and convert it: 1->01
    zero = 0
    minutes_str = str(minutes)
    if len(minutes_str) == 1:
        zm = '{}{}'
        minutes_cv = zm.format(zero, minutes)
    else:
        minutes_cv = minutes

#------FORMATTING HOUR MODULE-------( format hour: X:YZ or XY:ZQ - without space between)
    if args and number_of_days==0:
        string = '{}{}{} {}{} {}'
        print(string.format(hour, ':', minutes_cv, AMPM, ',', day))

    elif args and number_of_days!=0:
        string = '{}{}{} {}{} {} {}'
        print(string.format(hour, ':', minutes_cv, AMPM, ',', day, count_day))

    elif number_of_days!=0:
        string = '{}{}{} {} {}'
        print(string.format(hour, ':', minutes_cv, AMPM, count_day))

    elif number_of_days==0:
        string = '{}{}{} {}'
        print(string.format(hour, ':', minutes_cv, AMPM))

    #print('--', number_of_days, '--')

#copy test conditions below
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
add_time("3:30 PM", "2:12")
#"5:42 PM"
add_time("11:55 AM", "3:12")
#"3:07 PM"
add_time("9:15 PM", "5:30")
#"2:45 AM (next day)"
add_time("11:40 AM", "0:25")
#"12:05 PM"
add_time("2:59 AM", "24:00")
#"2:59 AM (next day)"
add_time("11:59 PM", "24:05")
#"12:04 AM (2 days later)"
add_time("8:16 PM", "466:02")
#"6:18 AM (20 days later)"
add_time("5:01 AM", "0:00")
#"5:01 AM"
add_time("3:30 PM", "2:12", "Monday")
#"5:42 PM, Monday"
add_time("2:59 AM", "24:00", "saturDay")
#"2:59 AM, Sunday (next day)"
add_time("11:59 PM", "24:05", "Wednesday")
#"12:04 AM, Friday (2 days later)"
add_time("8:16 PM", "466:02", "tuesday")
#"6:18 AM, Monday (20 days later)"
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)





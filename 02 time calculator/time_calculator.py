def add_time(start, duration, weekday = ""):

    if duration == "0:00": return start
    
    oneMinute = 60
    new_period = "AM"
    strInfo = ""
    qtdDays = 0
    qtdTotNextDays = 0

    # get start in 24hours
    lstStart_24h = get_start_24h(start)
    hourStart = lstStart_24h[0]
    minuteStart  = lstStart_24h[1]

    # get duration in minutes
    intDuration_mm = get_duration_mm(duration)
    intDifDuration_mm = int(intDuration_mm) - (int(oneMinute) - int(minuteStart)) # (K)

    hourFullStart = int(hourStart) + 1 # complete full hour (M)
    difComplete24h = 24 - int(hourFullStart) # difference to complete 24:00 (O)
    qtdHoursAdd = int(intDifDuration_mm / 60) # number of hours to be added (P)

    if intDifDuration_mm >  (difComplete24h * 60): # (K > O : next day)

        # number of hours to add - number of hours to complete 24 hours (Q = P - O)
        difHoursNextDay = qtdHoursAdd - difComplete24h 

        if (hourFullStart + difComplete24h) >= 24: qtdDays = 1 # (M + O >= 24 (S))
        qtdNextDaysAdd = int(difHoursNextDay / 24) # qtd next days (T)
        qtdTotNextDays = qtdDays + qtdNextDaysAdd # (U = S + T)
  
        new_hh = int((intDifDuration_mm - (difComplete24h * 60) - (qtdNextDaysAdd * 24 * 60))/60)
        new_mm = intDifDuration_mm - (qtdHoursAdd * 60)

        if qtdTotNextDays == 1:
            strInfo = " (next day)"
        else:
            strInfo = " (" + str(qtdTotNextDays) + " days later)"

    else: # same day
        new_hh = hourFullStart + qtdHoursAdd #( M + P)
        new_mm = intDifDuration_mm - (qtdHoursAdd * 60)

    if new_hh >= 12: new_period = "PM"

    if new_hh > 12:  
        new_hh = get_12_24_hs(new_hh, 12)
    elif new_hh == 0: 
        new_hh = 12

    if weekday != "":
        new_weekday = get_weekday(weekday, qtdTotNextDays)
        new_period += ", " + new_weekday 

    new_time = str(new_hh) + ":" + str(new_mm).zfill(2) + " " + new_period + strInfo

    return(new_time)

def get_start_24h(hhmm):
    #-------------------------- 
    # get start in 24hours

    lst_start_24h = []
    lst_ret_hh12_mm = get_hh12_mm(hhmm, 0)

    if lst_ret_hh12_mm[2] == "PM":
       hh = get_12_24_hs(lst_ret_hh12_mm[0], 24)
       lst_start_24h.append(hh)
    else:
       lst_start_24h.append(lst_ret_hh12_mm[0])
    
    lst_start_24h.append(lst_ret_hh12_mm[1]) 

    return (lst_start_24h)

def get_hh12_mm(hhmm, type):
    #-------------------------- 
    # get hh, mm, and period separately
    # hhmm >>> hhh:mm
    # type >>> 0-start | 1-duration
    # return lst_hh12_mm[0]=hh | lst_hh12_mm[1]=mm | lst_hh12_mm[3]="AM | PM | ''" 
  
    lst_hh12_mm = []

    ipos = (hhmm.find(":"))
    hh = hhmm[:ipos]

    if type == 0:
        mm = hhmm[ipos+1:5]
    else:
        mm = hhmm[ipos+1:]

    lst_hh12_mm.append(hh)
    lst_hh12_mm.append(mm)
    
    if type == 0: # ddmm start "PM or AM"
        ampm = hhmm[-2:]
        lst_hh12_mm.append(ampm)
    else:          # ddmm duration
        lst_hh12_mm.append("")
   
    return(lst_hh12_mm)

def get_12_24_hs(hh, type):
    #--------------------------   
    # type=12 return hh 24hs| type = 24 return hh 12hs

    dct_12_24h = {
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "24"  
    }

    if type == 24:    # return hh format 24h
        converthhmm = dct_12_24h[hh]

    elif type == 12:  # return hh format 12h   
        # list out keys and values separately
        key_list = list(dct_12_24h.keys())
        val_list = list(dct_12_24h.values())

        position = val_list.index(str(hh))
        converthhmm = key_list[position]
  
    return(converthhmm)

def get_duration_mm(hhmm):
    #-------------------------- 
    # get duration in minutes    

    duration_mm = 0
  
    lst_ret_hh12_mm = get_hh12_mm(hhmm, 1)

    hh = lst_ret_hh12_mm[0]
    mm = lst_ret_hh12_mm[1]

    duration_mm = (int(hh) * 60) + int(mm)
  
    return(duration_mm)

def get_weekday(weekdayStart, days):
    #-------------------------- 
    # return new weekday added of days 
    #    
    # Monday     2 +  0 d = 2  ==> 2%7  = 2 Monday
    # Saturday   7 +  1 d = 8  ==> 8%7  = 1 Sunday
    # Wednesday  4 +  2 d = 6  ==> 6%7  = 6 Friday
    # Tuesday    3 + 20 d = 23 ==> 23%7 = 2 Monday

    dct_weekday = {
        "sunday": "1",
        "monday": "2",
        "tuesday": "3",
        "wednesday": "4",
        "thursday": "5",
        "friday": "6",
        "saturday": "7"
    }

    numWeek = int(dct_weekday[weekdayStart.lower()])
    numWeek += days
    remainder = (numWeek % 7) 

    if days == 0 or remainder == 0: return weekdayStart
    
    # list out keys and values separately
    key_list = list(dct_weekday.keys())
    val_list = list(dct_weekday.values())

    position = val_list.index(str(remainder))
    new_WeekDay = (key_list[position]).capitalize()
  
    return(new_WeekDay)

    #--------------------------    

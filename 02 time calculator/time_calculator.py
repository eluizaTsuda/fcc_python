def add_time(start, duration, weekday = ""):
    print(">>>>>>>>>>>>>>>>>>>> NEW = start: " + str(start) + " duraton: " + str(duration))
    if duration == "0:00":
      return start
    
    oneMinute = 60
    new_period = ""

    # get start in 24hours
    lstStart_24h = get_start_24h(start)
    hourStart = lstStart_24h[0]
    minuteStart  = lstStart_24h[1]

    # get duration in minutes
    intDuration_mm = get_duration_mm(duration)
    intDifDuration_mm = int(intDuration_mm) - (int(oneMinute) - int(minuteStart)) # (K)

    print("retorno da funcao get_start_24h (C:D) >>> " + lstStart_24h[0] + " " + lstStart_24h[1])
    print("retorno da funcao get_duration_mm (H) >>> " + str(intDuration_mm))
    print("Minutos a serem adcs              (K) >>> " + str(intDifDuration_mm))

    hourFullStart = int(hourStart) + 1 # complete full hour (M)
    difComplete24h = 24 - int(hourFullStart) # difference to complete 24:00 (O)
    qtdHoursAdd = int(intDifDuration_mm / 60) # number of hours to be added (P)

    print("M...................................  >>>" + str(hourFullStart))
    print("O...................................  >>>" + str(difComplete24h))
    print("P...................................  >>>" + str(qtdHoursAdd))


    if intDifDuration_mm >  (difComplete24h * 60): # (K > O : next day)
        
        difHoursNextDay = qtdHoursAdd - difComplete24h # number of hours to add - number of hours to complete 24 hours (Q = P - O)

        print("Q..Diferença de horas para o next day >>> " + str(difHoursNextDay))

        if (hourFullStart + difComplete24h) >= 24:  # (M + O)
            qtdDays = 1
    
        new_hh = "00"
        new_mm = "00"
        new_time = (new_hh) + ":" + (new_mm)

    else: # same day
        new_hh = hourFullStart + qtdHoursAdd #( M + P)

        if new_hh >= 12: new_period = "PM"
        if new_hh > 12:  new_hh = get_12_24_hs(new_hh, 12) 
           
        new_mm = str(intDifDuration_mm - (qtdHoursAdd * 60)).zfill(2)
        new_time = str(new_hh) + ":" + str(new_mm) + " " + new_period

 
    return(new_time)


def get_hh12_mm(hhmm, type):
   #--------------------------------------------
   # hhmm >>> hhh:mm
   # type >>> 0-start | 1-duration
  
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

def get_start_24h(hhmm):
#----------------------------------------------------
    lst_start_24h = []
    #ipos = (hhmm.find(":"))
    #hh = hhmm[:ipos]
    #mm = hhmm[ipos+1:5]
    #ampm = hhmm[-2:]

    lst_ret_hh12_mm = get_hh12_mm(hhmm, 0)

    if lst_ret_hh12_mm[2] == "PM":
       hh = get_12_24_hs(lst_ret_hh12_mm[0], 24, lst_ret_hh12_mm[2],)
       lst_start_24h.append(hh)
    else:
       lst_start_24h.append(lst_ret_hh12_mm[0])
    
    lst_start_24h.append(lst_ret_hh12_mm[1]) 

    return (lst_start_24h)

def get_12_24_hs(hh, type, period="PM"):
#----------------------------------------------------    
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

    #if period == "PM":
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
    duration_mm = 0
  
    lst_ret_hh12_mm = get_hh12_mm(hhmm, 1)

    hh = lst_ret_hh12_mm[0]
    mm = lst_ret_hh12_mm[1]

    #print("in get_duration ===== " + hhmm)
    #print("in get_duration ===== hh: " + hh)
    #print("in get_duration ===== mm: " + hh)
        
    duration_mm = (int(hh) * 60) + int(mm)
  
    return(duration_mm)

#----------------------------------------------------   
def get_add_hhmm(intDifDuration_mm):
    #Converte mm em dd e min

    lstTotAdd_hhmm = []

    hh_add = int(intDifDuration_mm / 60)
    mm_add = int(intDifDuration_mm % 60)
 
    #print("get_add_hhmm --------- hh_add: " + str(hh_add))
    #print("get_add_hhmm --------- mm_add: " + str(mm_add))

    lstTotAdd_hhmm.append(int(hh_add))
    lstTotAdd_hhmm.append(int(mm_add))

    return(lstTotAdd_hhmm)


def qtdDaysAdd(hh):

    intDaysAdd = int(int(hh) / 24)
    return(intDaysAdd)
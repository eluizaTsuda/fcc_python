def add_time(start, duration, weekday = ""):
    #add_time("11:06 PM", "2:02")
    #add_time("3:30 PM", "2:12", "Monday")

    contDays = 0
    minute = 60
    hour = 24
    minStart = 0
  
    lstStart_24h = get_start_24h(start)
    intDuration_mm = get_duration_mm(duration)
    print("retorno da funcao get_start_24h  >>> " + lstStart_24h[0] + " " + lstStart_24h[1])
    print("retorno da funcao get_duration_mm>>> " + str(intDuration_mm))
    
    hourStart = lstStart_24h[0]
    minStart  = lstStart_24h[1]

    intDifDuration_mm = int(intDuration_mm) - (int(minute) - int(minStart))
    contDays += 1
    print("1 - diference minutes: *** intDifDuration *** - ok " + str(intDifDuration_mm))

    intHourAdd = get_add_hh(intDifDuration_mm)









    new_time = start
    return new_time

def get_hh12_mm(hhmm, ident):
   #--------------------------------------------
   # hhmm >>> hhh:mm
   # ident >>> 0-start | 1-duration
  
    lst_hh12_mm = []

    ipos = (hhmm.find(":"))
    hh = hhmm[:ipos]
    mm = hhmm[ipos+1:5]

    lst_hh12_mm.append(hh)
    lst_hh12_mm.append(mm)
    
    if ident == 0: # ddmm start
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
    hh = get_12_24_hs(lst_ret_hh12_mm[0], lst_ret_hh12_mm[2])
    lst_start_24h.append(hh)
    lst_start_24h.append(lst_ret_hh12_mm[1])

    return (lst_start_24h)

def get_12_24_hs(hh, period):
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

    if period == "PM":
        converthh = dct_12_24h[hh]
    
    return(converthh)

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
def get_add_hh(intDifDuration_mm):
    #Converte mm em dd e min

    lstTotAdd_hhmm = []

    return(lstTotAdd_hhmm)
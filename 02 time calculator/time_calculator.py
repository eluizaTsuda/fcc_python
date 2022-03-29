def add_time(start, duration, weekday = ""):
    #add_time("11:06 PM", "2:02")
    #add_time("3:30 PM", "2:12", "Monday")
    print(">>>>>>>>>>>>>>>>>>>> NEW = start: " + str(start) + " duraton: " + str(duration))
    contDays = 0
    minute = 60
    hour = 24
    minStart = 0

    if duration == "0:00":
      return start
  
    lstStart_24h = get_start_24h(start)
    intDuration_mm = get_duration_mm(duration)
    print("retorno da funcao get_start_24h  >>> " + lstStart_24h[0] + " " + lstStart_24h[1])
    print("retorno da funcao get_duration_mm>>> " + str(intDuration_mm))
    
    hourStart = lstStart_24h[0]
    minStart  = lstStart_24h[1]

    intDifDuration_mm = int(intDuration_mm) - (int(minute) - int(minStart))
    contDays += 1
    
       
    print("1 - diference minutes: *** intDifDuration *** - ok " + str(intDifDuration_mm))

    intTotAdd_hhmm = get_add_hhmm(intDifDuration_mm)
    hourAdd = intTotAdd_hhmm[0]
    minuteAdd = intTotAdd_hhmm[1]
    
    print("Amount hours ======= " + str(hourAdd) + " | " + str(hourStart))

  
    if int(hourStart) == 23:
      new_time = str(hourAdd) + ":" + (str(minuteAdd).rjust(2, '0')) + " AM"
    
    elif (24 - int(hourStart)) > int(hourAdd):
      # same day
      new_time = str(int(hourStart) + int(hourAdd) + 1)
      if int(new_time) > 12:
         new_time = get_12_24_hs(new_time, "PM", 12)

    else:
      # next day 
      new_time="??"
      print("change to next day ") 


    new_time += ":" + (str(minuteAdd).rjust(2, '0')) + " PM"   
    #print(" >>>>>>>>>>> new_time <<<<<<<<<< " + str(new_time))





    


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
    hh = get_12_24_hs(lst_ret_hh12_mm[0], lst_ret_hh12_mm[2], 24)
    lst_start_24h.append(hh)
    lst_start_24h.append(lst_ret_hh12_mm[1])

    return (lst_start_24h)

def get_12_24_hs(hh, period, type):
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

    converthhmm = hh

    if period == "PM":
      if type == 24:    # return hh format 24h
        converthhmm = dct_12_24h[hh]
      elif type == 12:  # return hh format 12h   
        # list out keys and values separately
        key_list = list(dct_12_24h.keys())
        val_list = list(dct_12_24h.values())
        
        position = val_list.index(hh)
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
def add_time(start, duration):
    #add_time("11:06 PM", "2:02")

    lstStart_24h = get_start_24h(start)
    print("retorno da funcao >>> " + lstStart_24h[0] + " " + lstStart_24h[1])
    intDuratio_mm = get_duration_mm(duration)





    new_time = 0
    return new_time

def get_hh12_mm(hhmm):
    lst_hh12_mm = []

    return(lst_hh12_mm)

def get_start_24h(hhmm):
#----------------------------------------------------
    lst_start_24h = []
    ipos = (hhmm.find(":"))
    hh = hhmm[:ipos]
    mm = hhmm[ipos+1:5]
    ampm = hhmm[-2:]

    hh = get_12_24_hs(hh, ampm)
    lst_start_24h.append(hh)
    lst_start_24h.append(mm)

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
    uration_mm = 0

    return(duration_mm)

#----------------------------------------------------   
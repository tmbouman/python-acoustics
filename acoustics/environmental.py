def time_to_minutes(time_str):
   """
   Convert time in 24-hour format (e.g. 17:30) to minutes.
   """
   hours, minutes = map(int, time_str.split(':'))
   return 60 * hours + minutes

def LDN(night_gauge_str, night_end_str, time_str, dBinput, penalty):
    """
    ----------
    INPUT
    night_gauge_str: The time in the PM (in 24-hour time ex. 17:00) when the nightime penalty comes into effect
    night_end_str: The time in the AM (in 24-hour time ex. 9:00) when the nighttime penalty is removed
    time_str: The vector with variables (in 24-hour time) coordinating to each dB reading
    dBinput: The vector of dB readings which coordinate with the time variables
    penalty: The associated dB penalty of noises in the nighttime
    example of a proper input is LDN('20:00','7:00',['6:00','8:00','12:00','18:00','24:00'],[42,54,52,59,50],10)
    Time is split at each input NOT between two inputs
    -------
    OUTPUT
    The output should be the sum of the LDN
    """
    import math 
    night_gauge = time_to_minutes(night_gauge_str)
    night_end = time_to_minutes(night_end_str)
    time = []
    for t in time_str:
        time.append(time_to_minutes(t))
    if len(dBinput) != len(time_str):
        return print('Difference in time inputs and dB inputs')
    #Appends a midnight value onto strings which do not end at midnight with the dB value of the previous input
    if time[-1] < 1440:
        time.append(1440)
        dBinput.append(dBinput[-1])
    i = 0
    dBtot = []
    while i < len(time):
        if i < len(time)-1:
            duration = time[i+1] - time[i]
        excess = 0
        #For penalty calculations in early morning
        if time[i] <= night_end:
            if time[i+1] > night_end:
                excess = night_end - time[i+1] 
                dBtot.append((10**(dBinput[i]/10)*excess)+10**((dBinput[i]+penalty)/10)*(duration-excess))
        #For penalty calculations in late night
        elif time[i] >= night_gauge:
            if time[i-1] < night_gauge and time[i]> night_gauge:
                excess = time[i] - night_gauge
                dBtot.append((10**(dBinput[i]/10)*excess)+10**((dBinput[i]+penalty)/10)*(duration-excess))
        #For normal calculations without penalty
        elif time[i] > night_end and time[i] < night_gauge:
            dBtot.append(dBinput[i])
            dBtot[i] += 10**(dBinput[i]/10)*(duration-excess)
        if i==len(time):
            break 
        i = i+1
    #Final Calculations for LDN
    finalsum = 10*math.log10(1/1440*sum(dBtot))
    return finalsum

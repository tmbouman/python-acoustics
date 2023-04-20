def SIL(speechlevels,background):
    """
    ----------
    INPUT
    speechlevels : A vector of SPL at frequencies 500, 1000, 2000 for SIL3 or 500, 1000, 2000, 4000 for SIL4
    background: The single value of background noise in dBA
    -------
    OUTPUT
    Either SIL3 or SIL4 depending on the amount of given data
    """
    numspeech=speechlevels
    #SIL4 Value Calculator
    if len(numspeech)==4:
        sils = []
        for i in range(4):
            sil = numspeech[i]
            sils.append(sil)
        # Calculate the average SIL4 value across the frequency bands
        sil4 = sum(sils) / len(sils)  
        return background-sil4
    #SIL3 Value Calculator
    elif len(numspeech)==3:
    # Calculate the SIL values for each frequency band
        sils = []
        for i in range(3):
            sil = numspeech[i]
            sils.append(sil)
        # Calculate the average SIL3 value across the frequency bands
        sil3 = sum(sils) / len(sils)    
        return background-sil3
    elif len(numspeech)>4:
        print("Too many inputted Values")
    elif len(numspeech)<3:
        print("Too few inputted Values")

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


def calculate_AI():
    """
    Input 1/3 octave frequency[200 Hz -5000 Hz] noise levels and speech levels 
    Input format:
    
    Speech_levels= [] seperate each entry with comma
    noise_levels= [] seperate each entry with comma
    
    result = calculate_AI(speech_levels, noise_levels)
    print(result)
    
    Output:
    Articulation Index Value
    """
    # Define the frequency set
    frequencies = [200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]

    # Display the frequency vector
    print("Frequency Vector: ", frequencies)

    # Define the weight array
    weight = [0.004, 0.0010, 0.0010, 0.0014, 0.0014, 0.0020, 0.0020, 0.0024, 0.0030, 0.0037, 0.0038, 0.0034, 0.0034, 0.0024, 0.0020]

    # Prompt the user to input the speech level values for all frequencies
    speech_levels = []
    speech_levels_input = input("Enter the speech level values for all frequencies (in dB re 20 μPa), separated by a comma: ")
    speech_level_values = speech_levels_input.split(",")
    for i in range(len(speech_level_values)):
        speech_levels.append(float(speech_level_values[i]))

    # Prompt the user to input the noise level values for all frequencies
    noise_levels = []
    noise_levels_input = input("Enter the noise level values for all frequencies (in dB re 20 μPa), separated by a comma: ")
    noise_level_values = noise_levels_input.split(",")
    for i in range(len(noise_level_values)):
        noise_levels.append(float(noise_level_values[i]))

    # Create empty list to store the SNR values
    SNRs = []

    # Calculate SNR values for all frequencies
    for i in range(len(frequencies)):
        SNR = speech_levels[i] - noise_levels[i]
        SNRs.append(max(0, SNR))  # Change negative SNRs to zero

    # Multiply weight to SNRs to get AI
    AI = [weight[i] * SNRs[i] for i in range(len(weight))]

    # Calculate the sum of all elements in AI and store it in a variable named Articulation_Index
    Articulation_Index = sum(AI)

    # Round off the Articulation_Index variable value to 2 decimal places
    Articulation_Index = round(Articulation_Index, 2)
    return "Articulation Index = " + str(Articulation_Index)
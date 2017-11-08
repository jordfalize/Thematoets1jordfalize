# Jord Falize
# Bin-1a
# 8-11-2017

def main():         # Functie om alle andere functies op te roepen.
    read_file()
    not_validated()
    ion_involved()

    Rest, num, Accesiecodes = not_validated()
    counter, ioncode = ion_involved()

    print ('Number of unverified genes: ',num)              # Print het aantal "unverified genes".
    print ('Number of involved ion processes:', counter)    # Print het aantal "involved ion" processen.
    print (40*'-')                                          
    print ('First 10 acc.codes of unverified genes:')       # Print de eerste 10 "unverified genes" codes.
    for i in range (0,10):                                  # Het zijn er teveel om in een keer te printen.
        print (Accesiecodes[i])                              
    print (40*'-')                                           
    print ('First 10 acc.codes of ion involved genes:')     # Print de eerste 10 "involved ion" codes.
    for i in range (0,10):                                  # Het zijn er teveel om in een keer te printen.
        print (ioncode[i])                                  
    

def read_file():
    bestand = open('yeast_genes.csv')       # Bestand wordt geopend. 

    lijst = []                                      # Bestand wordt gesplitst op komma, en toegevoegd aan
    for i in bestand:                               # een 2d lijst
        sublijst = i.replace("\n","").split(",")
        lijst.append(sublijst)

    lijst.remove(lijst[0])
    return lijst                            


def not_validated():
    lijst = read_file()             
    
    Verified = []
    Rest = []
    Accesiecodes = []
    
    num = 0
    
    for i in lijst:                 # Bestand wordt gescheiden op 'verified', en toegevoegd aan
        if 'Verified' in i:         # verschillende lijsten.
            Verified += i
        else:
            Rest.append(i)
            num += 1
    for i in Rest:
        Accesiecodes.append(i[0])
    
    
    counter = num

    return Rest, num, Accesiecodes      

def ion_involved():
    Rest, num, Accesiecodes = not_validated()   
                            
    ion = []
    counter = 0
                                    # Rest lijst wordt gescheiden op ion aanwezigheid.     
    for i in Rest:
        if 'ion' in i:
            ion.append(i)
            counter += 1

    #print (ion)

    ioncode = []                    # Ion accesiecodes worden toegevoegd aan een lijst.
    
    for i in ion:
        ioncode.append(i[0])

    #print (ioncode)

    return counter, ioncode

main()                              # Roep alle functies in het script op.

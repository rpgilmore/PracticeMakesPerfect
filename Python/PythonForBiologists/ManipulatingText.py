'''These exercises go over how to use Python to create
   reverse complements and other easy tasks with strings '''
   
#remember to run using python3
import re
def ATContent (seq):
    fullLen = len(seq)
    ATnum = seq.count('A') + seq.count('T')
    AT = round((ATnum/fullLen)*100, 2) 
    
    print ("AT content is " +str(AT)+"%") #come back and make this a formatted string
    
    
def RevComp(seq):
    baseComp = {'A':'T',
                'C':'G',
                'G':'C',
                'T':'A'
                }
    
    compTable = seq.maketrans(baseComp)
    comp = seq.translate(compTable)
    
    print("Reverse Complement is " + comp[::-1]) #This basically means, give me a substring from the beginning to 
                                                 #the very end, but go backwards.
    
    
def RFragLen(seq, Rseq):
    start = 0
    end = len(seq)
    siteSet = set()
    #Is it faster to advance by the slice technique or by incrementing by one each time? 
    #How do you test for efficiency and stuff, aka, run 1 billion times and get average runtime?
    while start < end:
        site = seq.find(Rseq, start, end)

        if site != -1:
            siteSet.add(site)
        
        start += 1 
            
    print (siteSet)
        

    
RFragLen('ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGAATTCAT', 'GAATTC')
#ATContent('ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT')

#RevComp('ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT')
import sys

def transcribe(filepath):
    
    out = open("transcript.txt", "w")
    
    #Create a dict with T:U replacement
    #Don't need to create a maketrans method for each line
    #since the replacement will always be the same. Must use ASCII
    TtoU = {84:85}
    with open(filepath) as dna:
        lines = dna.readlines()
        
        for line in lines:
            line = line.upper()
            line = line.translate(TtoU)
            out.write(line+"\n")
    out.close()
            
transcribe(sys.argv[1])
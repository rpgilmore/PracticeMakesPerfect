import sys

def countNuc(filepath):
    
    with open(filepath) as nucFile:
        lines = nucFile.readlines()
        
        countA = 0
        countC = 0
        countG = 0
        countT = 0
        
        for line in lines:
            line = line.upper()
            countA += line.count('A')
            countC += line.count('C')
            countG += line.count('G')
            countT += line.count('T')
            
        results = [str(countA), str(countC), str(countG), str(countT)]
        
        print(" ".join(results))
        
        
countNuc(sys.argv[1])
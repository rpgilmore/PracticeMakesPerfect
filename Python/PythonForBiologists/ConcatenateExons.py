''' Removes introns from a genomic sequence and outputs a text file of
concatenated exons. 
    
Takes 2 filepaths as an argument; one to a file with start and stop 
positions, the second to the genomic input text.
'''

def concatExon(exonPath, genPath):
    output = open("concatenated_exons.txt", "w")
    
    with open(exonPath) as ex, open(genPath) as gen:
        ex = ex.readlines()
        gen = gen.read()
        exonList = []
        
        for line in ex:
            exPos = line.split(",")
            substring = gen[int(exPos[0]):int(exPos[1])]
            exonList.append(substring)
        
        output.write("".join(exonList))
    
    output.close()
            
    
concatExon("/home/ubuntu/workspace/Python/PythonForBiologists/lists_and_loops_exercise_files/exons.txt",
           "/home/ubuntu/workspace/Python/PythonForBiologists/lists_and_loops_exercise_files/genomic_dna.txt")

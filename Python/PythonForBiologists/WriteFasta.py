def checkInput(line_array):
    header = line_array[0]
    seq = line_array[1]

    final_head = ">"+header
    
    seq = seq.replace("-","")
    final_seq = seq.upper()
    
    return [final_head, final_seq]

def writeFasta(filepath):
    
    fasta = open("genomic_dna.fasta", "w")
    
    with open(filepath) as geneFile:
        lines = geneFile.readlines()
    
        for line in lines:
            line = line.split("\t")
            line_chk = checkInput(line)
            
            fasta.write("\n".join(line_chk))

    geneFile.closed
    fasta.close()
    
writeFasta("/home/ubuntu/workspace/Python/PythonForBiologists/genomic_dna.txt")
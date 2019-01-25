def trimInput (filepath, adapter):
    trimmed = open("trimmed_input.txt", "w")
    
    with open(filepath) as input:
        outseqs = []
        #Write error checking for things like file not found
        seqs = input.readlines()
        for seq in seqs:
            output = seq.replace(adapter, "")
            outseqs.append(output)
        
        trimmed.write("".join(outseqs))
    
    input.closed
    trimmed.close()    
        
trimInput("/home/ubuntu/workspace/Python/PythonForBiologists/lists_and_loops_exercise_files/input.txt", "ATTCGATTATAAGC")
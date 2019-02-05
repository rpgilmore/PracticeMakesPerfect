import sys
import itertools


def translateInput(seq):
    seq = sys.argv[1].upper()
    
    unamb = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    ambig = {
        'Y':['C','T'], 'R':['A','G'], 'W':['A','T'],
        'S':['G','C'], 'K':['T','G'], 'M':['C', 'A'],
        'D':['A','G','T'], 'V':['A','C','G'], 'H':['A','C','T'],
        'B':['C','G','T'], 'X':['A','C','G','T'], 'N':['A','C','G','T'],
    }

    #Step should always be 3 since we are considering codons
    step = 3
    codons = [seq[i:i+step] for i in range(0, len(seq), step)]
    
    def lookupCodon(cd):

        #if key is not found you will get a KeyError
        if cd not in unamb:
            bases = list(cd)
        
            lob = [ambig[base] if base in ambig else [base] for base in bases]
            
            #Is like a generator object. returns tuples of combinations
            new_cd = list(itertools.product(*lob))
            concat = ["".join(codon) for codon in new_cd]
            
            ambig_aa = [unamb[codon] for codon in concat]
            ambig_aa = list(set(ambig_aa))
            ambig_aa = "["+"/".join(ambig_aa)+"]" if len(ambig_aa) > 1 \
                         else "".join(ambig_aa)
                
            return (ambig_aa)
            
        else:
            return (unamb[cd])    
    
    
    trans = [lookupCodon(codon) if len(codon) is step else codon.lower() 
             for codon in codons]
    
    print ("".join(trans))

translateInput(sys.argv)
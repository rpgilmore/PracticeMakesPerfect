'''Doc string goes here

'''
#Order of CSV file
#species name, sequence, gene name, expression level.
#a fxn to read the csv, return list of tuples, fxn to run test print result
#a fxn to write the results to a file.
def readCSV (filepath):
    
    list_tuples = []
    
    with open(filepath) as expr:
        lines = expr.readlines()
        
        for line in lines:
            line = line.rstrip("\n")
            expr_data = line.split(",")
            list_tuples.append(tuple(expr_data))
        
    expr.closed

    return list_tuples


#Can I refactor this using decorators? Probably

def checkSpecies(list_tuples): #checked, it works
    
    dros_genes = []
    
    for gene in list_tuples:
        species = gene[0]
        gene_name = gene[2]
        
        if ("melanogaster" in species) or ("simulans" in species):
            dros_genes.append(gene_name)

    return dros_genes


def checkLen(list_tuples): #checked, it works
    
    dros_genes = []
    
    for gene in list_tuples:
        gene_nuc = gene[1]
        gene_name = gene[2]
        
        if len(gene_nuc) >= 90 and len(gene_nuc) <=110:
            dros_genes.append(gene_name)
    
    return dros_genes


def checkAT(list_tuples): #checked, works
    dros_genes = []
    
    for gene in list_tuples:
        gene_name = gene[2]
        gene_nuc = gene[1]
        gene_expr = int(gene[3])
        AT_count = gene_nuc.count('a') + gene_nuc.count('t')
        AT_content = round(AT_count/len(gene_nuc), 2)
        
        if AT_content < 0.5 and gene_expr > 200:
            dros_genes.append(gene_name)

    return dros_genes


def complexCondition(list_tuples): #checked, works
    dros_genes = []
    
    for gene in list_tuples:
        species = gene[0]
        gene_name = gene[2]
        
        if ((gene_name.startswith('k') or gene_name.startswith('h')) 
            and not "melanogaster" in species):
            dros_genes.append(gene_name)
    
    return dros_genes

def hiMedLo(list_tuples): #works, but returns a list of tuples instead of a straight list
    dros_genes = []
    
    for gene in list_tuples:
        gene_nuc = gene[1]
        gene_name = gene[2]
        AT_count = gene_nuc.count('a') + gene_nuc.count('t')
        AT_content = round(AT_count/len(gene_nuc), 2)
        
        if AT_content > 0.65:
            dros_genes.append(gene_name + " The AT content is high")
        elif AT_content >= 0.45:
            dros_genes.append(gene_name + " The AT content is moderate")
        else:
            dros_genes.append(gene_name + " The AT content is low")
    
    return dros_genes



def writeConditions():
    
    output = open("expression_data.txt", "w")
    
    gene_tuples = readCSV("/home/ubuntu/workspace/Python/PythonForBiologists"
                          +"/conditional_tests/data.csv")
    #write a fxn for each test? Then each returned list gets printed in a
    #result?
    all_lists = []
    
    name_by_species = checkSpecies(gene_tuples)
    name_by_species.insert(0, "Results of Check Species")
    
    name_by_len = checkLen(gene_tuples)
    name_by_len.insert(0, "Results of Check Length")
    
    name_by_AT = checkAT(gene_tuples)
    name_by_AT.insert(0, "Results of Check AT Content")
    
    name_by_complex = complexCondition(gene_tuples)
    name_by_complex.insert(0, "Results of Complex Condition")
    
    amount_AT = hiMedLo(gene_tuples)
    amount_AT.insert(0, "Results of Amount AT Content")

    all_lists.extend(name_by_species+name_by_len+name_by_AT
                     +name_by_complex+amount_AT)
    
    output.write("\n".join(all_lists))
    
    output.close()
    
    
    
writeConditions()

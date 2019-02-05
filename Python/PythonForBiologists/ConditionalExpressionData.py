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


def returnList(checkFunc):
    def wrapper (gene_tuple):
        dros_genes = []
        for gene in gene_tuple:

            dros_genes.append(checkFunc(gene))
        
        dros_genes = [d_gene for d_gene in dros_genes if d_gene]
        dros_genes.append("") #Not sure if that's a good idea stylistically
        return dros_genes
    
    return wrapper


@returnList
def checkSpecies(gene):  
    species = gene[0]
    gene_name = gene[2]
        
    if ("melanogaster" in species) or ("simulans" in species):
        return gene_name
   
    else:
        pass


@returnList
def checkLen(gene):

    gene_nuc = gene[1]
    gene_name = gene[2]
        
    if len(gene_nuc) >= 90 and len(gene_nuc) <=110:
        return gene_name
    
    else:
        pass


@returnList
def checkAT(gene):

    gene_name = gene[2]
    gene_nuc = gene[1]
    gene_expr = int(gene[3])
    AT_count = gene_nuc.count('a') + gene_nuc.count('t')
    AT_content = round(AT_count/len(gene_nuc), 2)
    
    if AT_content < 0.5 and gene_expr > 200:
        return gene_name
    
    else:
        pass


@returnList
def complexCondition(gene):
    species = gene[0]
    gene_name = gene[2]
    
    if ((gene_name.startswith('k') or gene_name.startswith('h')) 
        and not "melanogaster" in species):

        return gene_name
    
    else:
        pass


@returnList
def hiMedLo(gene):

    gene_nuc = gene[1]
    gene_name = gene[2]
    AT_count = gene_nuc.count('a') + gene_nuc.count('t')
    AT_content = round(AT_count/len(gene_nuc), 2)
        
    if AT_content > 0.65:
        return (gene_name + " The AT content is high")
    elif AT_content >= 0.45:
        return (gene_name + " The AT content is moderate")
    else:
        return (gene_name + " The AT content is low")


def writeConditions():
    
    output = open("expression_data.txt", "w")
    
    gene_tuples = readCSV("/home/ubuntu/workspace/Python/PythonForBiologists"
                          +"/conditional_tests/data.csv")

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

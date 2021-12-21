def status(file):
    """Lees de validation af uit het bestand door,
    elke keer op dezelfde positie, op een andere regel.
    Zet de validation in een lijst.
    Input: file - csv bestand - genen annotatie
    Output: data_list - lijst met  statussen
    """
    info_list = []
    data_list = []
    open_file = open(file)
    open_file.readline()
    for i in open_file:
        line = i.replace("\n", "").split(",")
        info_list.append(line)
        # In iedere regel, tweede positie.
        validation = line[1]
        data_list.append(validation)

    open_file.close()

    return data_list

def gene_status(data_list):
    """Telt het aantal van iedere validation status.
    Input: data_list
    Output: count_list
    """
    validation_list = []
    count_list = []
    count = 0
    for j in data_list:
        if j not in validation_list:
            validation_list.append(j)
        else:
            continue
    length = len(validation_list)
    print(validation_list)

    # r is aantal verschillende validation.
    # i voor elk woord in de lijst.
    # als het woord gelijk is als het woord van validation tel bij op.
    for r in range(length):
        for i in data_list:
            if i == validation_list[r]:
                count += 1
        if count != 0:
            count_list.append(count)
            count = 0

    return count_list



def main():
    data_list = status("yeast_genes.csv")
    count_list = gene_status(data_list)
    print(count_list)

main()

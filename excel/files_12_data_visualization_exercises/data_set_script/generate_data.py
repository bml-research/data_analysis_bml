import random

def get_fam_data(file_name):
    with open(file_name) as f:
        all_data = []
        for line in f:
            line = line.strip()
            line = line.replace(u'\xa0', u' ')
            line = line.split("\t")    
            all_data.append((line[0], line[1]))
    return all_data


def get_gene_names(file_name):
    with open(file_name) as f:
        all_data = []
        for line in f:
            line = line.strip()
            line = line.replace(u'\xa0', u' ')
            all_data.append(line)
    return all_data


def write_csv(gene_names, fam_names):
    sep = random.choice(["\t", ";", ","])
    header = "".join(["NM number", sep, "Gene name", sep, "Gene Family", sep, "Category", sep, "Expression Value - stimulus", sep, "Expression Value + stimulus", "\n"])
    with open("output.csv", "w") as f:
        f.write(header)
        for gene_name in gene_names:
            #print(gene_name)
            expression_val_min_stimulus = round(random.random(), 3)
            factor = random.uniform(1, 10)/100  # Random percentage between 1 and 10
            factor = factor * (random.choice([1, -1]))
            expression_val_plus_stimulus = round(expression_val_min_stimulus * factor + expression_val_min_stimulus, 3)
            #print(expression_val)
            NM_ID = "NM_000" + str(random.randint(1000, 9999))
            #print(NM_ID)
            fam_cat = random.choice(fam_names)
            fam = fam_cat[0]
            cat = fam_cat[1]
            if fam == "Hox gene family":
                expression_val_min_stimulus = round(random.uniform(0.5, 1.0), 3)
                if expression_val_min_stimulus < 0.9:
                    expression_val_plus_stimulus = round(expression_val_min_stimulus * abs(factor) + expression_val_min_stimulus, 3)
            elif fam == "Nuclear receptor":
                expression_val_min_stimulus = round(random.uniform(0.7, 1.0), 3)
                expression_val_plus_stimulus = round(expression_val_min_stimulus * abs(factor) + expression_val_min_stimulus, 3)
            #print(expression_val)
            line = [NM_ID, sep, gene_name, sep, fam, sep, cat, sep, str(expression_val_min_stimulus), sep, str(expression_val_plus_stimulus), "\n"]
            line = "".join(line)
            f.write(line)

def main():
    file_name_family = "gene_family.txt"
    file_name_genes = "gene_names.txt"
    gene_names = get_gene_names(file_name_genes)
    fam_names = get_fam_data(file_name_family)
    write_csv(gene_names, fam_names)
    print("done")


if __name__ == "__main__":
    main()
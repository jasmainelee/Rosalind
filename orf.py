start_codon = ("ATG")
#stop_codon = ("TAG", "TGA", "TAA")

dna = open("/home/daniel/Downloads/rosalind_orf.txt", "r").read().strip()
#print(dna)

start_pos = []
for position in range(len(dna)):
    if dna[position:].startswith(start_codon):
        start_pos.append(position)
#print(start_pos)

# for position in range(len(dna)):
#     if dna[position:].startswith(stop_codon):
#         print("stop codon positions = " + str(position+1))

complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
revcomp = "".join(complement.get(base, base) for base in reversed(dna))
#print(revcomp)

rev_start_pos = []
for position in range(len(revcomp)):
    if revcomp[position:].startswith(start_codon):
        rev_start_pos.append(position)
#print(rev_start_pos)

# for position in range(len(revcomp)):
#     if revcomp[position:].startswith(stop_codon):
#         print("reverse complement stop codon positions =" + str(position+1))

dna_code = open("/home/daniel/proj/jas/dna_codon.txt", "r").readlines()
dna_codon= {}
for line in dna_code:
    key, value = line.strip().split(' ')
    dna_codon[key] = value

proteins = []

for j in start_pos:
    protein = ""
    for i in range(j, len(dna), 3):
        if len(dna[i:i+3]) < 3 or dna_codon[dna[i:i+3]] == "Stop":
            break
        protein += dna_codon[dna[i:i+3]]
    proteins.append(protein)

for j in rev_start_pos:
    protein = ""
    for i in range(j, len(revcomp), 3):
        if len(revcomp[i:i+3]) < 3 or dna_codon[revcomp[i:i+3]] == "Stop":
            break 
        protein += dna_codon[revcomp[i:i+3]]
    proteins.append(protein)

def get_unique_proteins(proteins):
    list_of_unique_prot = []
    unique_proteins = set(proteins)
    for proteins in unique_proteins:
        list_of_unique_prot.append(proteins)
    return list_of_unique_prot
#print(get_unique_proteins(proteins))

for unique_proteins in get_unique_proteins(proteins):
    print(unique_proteins)
from Bio.SeqUtils import molecular_weight
from Bio.Seq import Seq

# Define a function to calculate the molecular weight of a protein sequence
def calculate_molecular_weight(protein_sequence):
    seq = Seq(protein_sequence)
    return molecular_weight(seq, "protein")

# Provide the protein sequence as a string
protein_sequence = input('Enter Sequence: ')

# Calculate the molecular weight
mw = calculate_molecular_weight(protein_sequence)

print(f"Molecular Weight of the protein: {mw:.2f} g/mol")

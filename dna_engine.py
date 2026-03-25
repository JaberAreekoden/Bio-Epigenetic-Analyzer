from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, molecular_weight

def process_genetic_data(sequence_string):
    dna = Seq(sequence_string.upper())
    
    # Feature 1: GC Content (Methylation potential)
    gc_val = gc_fraction(dna) * 100
    
    # Feature 2: Molecular Weight (Physical property)
    weight = molecular_weight(dna)
    
    # Feature 3: Translation (Biological Decoding)
    protein = dna.translate(to_stop=True)
    
    return {
        "gc_content": round(gc_val, 2),
        "molecular_weight": round(weight, 2),
        "protein_sequence": str(protein),
        "is_cpg_island": gc_val > 55  # High GC areas are epigenetic "switches"
    }
    
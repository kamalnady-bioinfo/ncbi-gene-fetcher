from Bio import Entrez, SeqIO

def calc_gc(seq):
    N=len(seq)
    Gcontent=seq.count("G")
    Ccontent=seq.count("C")
    plus=Gcontent+Ccontent
    total=plus/N
    return total

Entrez.email="kamalnagy960@gmail.com"
handle=Entrez.efetch(
    db="nucleotide",
    id="NM_007294",
    rettype="fasta",
    retmode="text"
)
record=SeqIO.read(handle,"fasta")
print(f"name:- {record.id}")
print(f"length:- {len(record.seq)}")
print(f"first 50 nucleotides:- {record.seq[:50]}")
print(f"gc content:- {calc_gc(record.seq)}")
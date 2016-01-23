#input
#AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

#output
#MAMAPRTEINSTRING

import sys

with open(sys.argv[1]) as fh:
	rna = fh.next().strip()

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

codons = list()
len = len(rna)/3
for i in range(0,len):
	codon = rna[i*3:i*3+3]
	codons.append(codon)

protein = ""
for codon in codons:
	if (map[codon] != "STOP"):
		protein = protein + map[codon]

print protein


# TRANSLATE
def translate(rnaSeq):
    map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    codons = list()
    len = len(rna)/3
    for i in range(0,len):
        codon = rna[i*3:i*3+3]
        codons.append(codon)

    protein = ""
    for codon in codons:
        if (map[codon] != "STOP"):
            protein = protein + map[codon]

    return protein

# TRANSCRIBE
def transcribe(dnaSeq):
    return dnaSeq.replace('T', 'U')

# REVERSE_TRANSCRIBE
def reverseTranscribe(dnaSeq):
    dnaSeq = dnaSeq.replace('T','P')
    dnaSeq = dnaSeq.replace('A','U')
    dnaSeq = dnaSeq.replace('P','A')

    dnaSeq = dnaSeq.replace('C','Q')
    dnaSeq = dnaSeq.replace('G','C')
    dnaSeq = dnaSeq.replace('Q','G')

    return dnaSeq;

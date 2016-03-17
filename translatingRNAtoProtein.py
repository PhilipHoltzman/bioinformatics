#! Python3

# Translating RNA to a protein

rnaCodonTable = {
	'UUU':'F',    'AUU':'I',
	'UUC':'F',    'AUC':'I',
	'UUA':'L',    'AUA':'I',
	'UUG':'L',    'AUG':'M',
	'UCU':'S',    'ACU':'T',
	'UCC':'S',    'ACC':'T',
	'UCA':'S',    'ACA':'T',
	'UCG':'S',    'ACG':'T',
	'UAU':'Y',    'AAU':'N',
	'UAC':'Y',    'AAC':'N',
	'UAA':'Stop', 'AAA':'K',
	'UAG':'Stop', 'AAG':'K',
	'UGU':'C',    'AGU':'S',
	'UGC':'C',    'AGC':'S',
	'UGA':'Stop', 'AGA':'R',
	'UGG':'W',    'AGG':'R',
	'CUU':'L',    'GUU':'V',
	'CUC':'L',    'GUC':'V',
	'CUA':'L',    'GUA':'V',
	'CUG':'L',    'GUG':'V',
	'CCU':'P',    'GCU':'A',
	'CCC':'P',    'GCC':'A',
	'CCA':'P',    'GCA':'A',
	'CCG':'P',    'GCG':'A',
	'CAU':'H',    'GAU':'D',
	'CAC':'H',    'GAC':'D',
	'CAA':'Q',    'GAA':'E',
	'CAG':'Q',    'GAG':'E',
	'CGU':'R',    'GGU':'G',
	'CGC':'R',    'GGC':'G',
	'CGA':'R',    'GGA':'G',
	'CGG':'R',    'GGG':'G',
}

gString = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
 
output = ''


for p in gString:
	if p in rnaCodonTable.keys():
		output += rnaCodonTable[p]

print(type(output))
print(output)
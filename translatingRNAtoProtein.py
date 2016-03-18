#! Python3

# Translating RNA to a protein

rnaCodonTable = {
	'F':'UUU',    'I':'AUU',
	'F':'UUC',    'I':'AUC',
	'L':'UUA',    'I':'AUA',
	'L':'UUG',    'M':'AUG',
	'S':'UCU',    'T':'ACU',
	'S':'UCC',    'T':'ACC',
	'S':'UCA',    'T':'ACA',
	'S':'UCG',    'T':'ACG',
	'Y':'UAU',    'N':'AAU',
	'Y':'UAC',    'N':'AAC',
	'Stop':'UAA', 'K':'AAA',
	'Stop':'UAG', 'K':'AAG',
	'C':'UGU',    'S':'AGU',
	'C':'UGC',    'S':'AGC',
	'Stop':'UGA', 'R':'AGA',
	'W':'UGG',    'R':'AGG',
	'L':'CUU',    'V':'GUU',
	'L':'CUC',    'V':'GUC',
	'L':'CUA',    'V':'GUA',
	'L':'CUG',    'V':'GUG',
	'P':'CCU',    'A':'GCU',
	'P':'CCC',    'A':'GCC',
	'P':'CCA',    'A':'GCA',
	'P':'CCG',    'A':'GCG',
	'H':'CAU',    'D':'GAU',
	'H':'CAC',    'D':'GAC',
	'Q':'CAA',    'E':'GAA',
	'Q':'CAG',    'E':'GAG',
	'R':'CGU',    'G':'GGU',
	'R':'CGC',    'G':'GGC',
	'R':'CGA',    'G':'GGA',
	'R':'CGG',    'G':'GGG'
}

gString = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'


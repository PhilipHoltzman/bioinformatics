#! Python3

# producing complementary strands of data


print('\n\n..:DNA Replication Engine:.\n')

# initial strand
iStrand = 'AATGCCTATGGC'
# complimentary strand
cStrand = ''

for i in iStrand:
	if i == 'A':
		cStrand +='T'
	if i == 'T':
		cStrand +='A'
	if i == 'G':
		cStrand +='C'
	if i == 'C':
		cStrand +='G'


print('\n\n Initial Sequence Strand:\n\n ' + iStrand+ '\n')


print(' Complimentary Base Pair Sequence:\n\n ' + cStrand + '\n\n')


import random

alphabet = 'ACGT'

f = open('input.fa','w')
for i in range(1,101):
	string = ''
	f.write('>seq'+str(i)+'\n')
	rand_seq_len = random.randrange(5,50)
	for j in range(rand_seq_len):
		string+=random.choice(alphabet)
	f.write(string+'\n')
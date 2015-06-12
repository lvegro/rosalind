from string import maketrans

with open('rosalind_revc.txt', 'r') as f:
    string = f.read()

# translation table
intab = "ATCG"
outtab = "TAGC"
transtab = maketrans(intab, outtab)
comp = string.translate(transtab)
# dall'inizio alla fine a passo = -1
revc = comp[::-1]

out = open('test.txt', 'w')
out.write(revc)

out.close()

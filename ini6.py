# creiamo un dictionary vuoto per riempirlo dinamicamente
d = {}
with open("rosalind_ini6.txt", "r") as f:
        string = f.read()
        # si usa .read e non .readline perché .readline restituisce una lista
        # e non una stringa
        for word in string.split(' '):
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
out = open("out6.txt", "w")
for key, value in d.items():
    print key, value
out.close()

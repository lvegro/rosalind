out_file = open("out.txt","w")
i = 1
with open("rosalind_ini5.txt", "r") as f:
        for line in f.readlines():
            if i % 2 == 0:
                out_file.writelines(line)
            i += 1
out_file.close()

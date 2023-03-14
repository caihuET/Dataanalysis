f2 = open("./files/table2.csv", "a")
f1 = open("./files/table1.csv")

i = 1
while i <= 4:
    csv = f1.readline()
    f2.write(csv)
    if not csv:
        i += 1
        f1.seek(0)

f2.close()
f1.close()

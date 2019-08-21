tres = []
for i in range(0,31):
    tres.append(i)

for i in range(1,len(tres)):
    if tres[i] % 3 == 0:
        tres[i] = "Achei"
    if str(tres[i])[-1] == "3":
        tres[i] = "Achei"

for i in range(0,31):
    print(tres[i])
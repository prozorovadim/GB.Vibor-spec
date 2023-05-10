list = []
dlina = int(input())
for j in range (dlina):
    a=input()
    list.append(a)
new = []
for i in range (len (list)):
    if len(list[i])<=3:
        new.append(list[i])
print(new)

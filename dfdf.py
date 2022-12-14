lista=[1,2,3,4,5,6,7,8,9,10]
to_find=5
found = False
for i in range (len(lista)):
    found=lista[i]==to_find
    print(found)
    if found:
        break


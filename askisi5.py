f=open("asdasd.txt","r")
contents=f.read()
print contents
lekseis=contents.split()
print lekseis
for x in lekseis:
    if len(x)> 3:
        leksi=x
        prwto_gramma=leksi[0]
        nea_leksi=leksi+prwto_gramma+"ay"
        nea_leksi=nea_leksi[1:len(nea_leksi)]
        print nea_leksi
#τα print στις γραμμές 3 και 5 είναι προαιρετικά και τα έβαλα για έλεγχο 
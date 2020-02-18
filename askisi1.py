keimeno=open("asdasd.txt","r")
x=keimeno.read()
lekseis=x.split()
print lekseis
y=len(lekseis)
lista=sorted(lekseis, key=len)
print lista
del lista[:y-5]
print lista
for i in range (0,5) :
  nealeksi=""
  for j in lista[i]:
    if j not in "aeiouAEIOU":
      nealeksi =j+nealeksi
  lista[i]=nealeksi
print lista

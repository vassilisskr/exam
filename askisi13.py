cardnum=raw_input("Eisagete ton arithmo tis kartas sas")
while len(cardnum)!=16:
 print "Den eisagate swsta ton arithmo tis kartas : "
 cardnum=raw_input("Eisagete ksana ton arithmo tis kartas sas : ")
print "To plithos twn arithmwn tis kartas einai swstos"
psifia=map(int ,str(cardnum))
athrisma1=sum(psifia[-1::-2])
athrismadiplasiwn=sum([sum(divmod(2*i,10)) for i in psifia[-2::-2]])
if (athrisma1+athrismadiplasiwn)%10==0:
 print"o arithmos tis kartas einai o swstos"
else:
 print"o arithmos tis kartas einai lathos"
 

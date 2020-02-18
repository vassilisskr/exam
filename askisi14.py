import numpy as np
data=np.genfromtxt("qwerty.txt", delimiter=" " ,dtype=int)
print data
orizousa=np.linalg.det(data)
print orizousa
#το πρώτο print ειναι προαιρετικό

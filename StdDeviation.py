import math

#Enter your Values here
D01 = 0.04552200201545183
D02 = 0.11092790879050969

C1 = -4.812205549522938e-08
C2 = -1.675580998402424e-08

L01 = 2.962820849496133e-07
L02 = 1.780563251595567e-07

def stdDev(X,Y):
    Av=(X+Y)/2
    f1=(X-Av)*(X-Av)
    f2=(Y-Av)*(Y-Av)
    Var=(f1+f2)/2
    Dev=math.sqrt(Var)
    return Dev


A = stdDev(D01,D02)
B = stdDev(C1,C2)
D = stdDev(L01,L02)
print("Deviation in d0 = ",stdDev(D01,D02),"\nProbable Error = ", 0.6745*float(A),"\n")
print("Deviation in C = ", stdDev(C1,C2),"\nProbable Error = ", 0.6745*float(B),"\n")
print("Deviation in l0 = ", stdDev(L01,L02),"\nProbable Error = ", 0.6745*float(D))








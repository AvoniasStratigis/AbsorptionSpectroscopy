#Standard Values of Mercury Lamp Wavelengths
L1 = 612E-9      #Orange
L2 = 576.96E-9    #Yellow
L3 = 546.10E-9    #Green
L4 = 491.60E-9    #Cyan
L5 = 435.83E-9    #Blue
L6 = 407.78E-9    #Violet


"""D1 = float(input("What is D Orange?"))    #Orange 16.4E-2
D2 = float(input("What is D Yellow?"))    #Yellow 16.8E-2
D3 = float(input("What is D Green?"))    #Green 17.8E-2
D4 = float(input("What is D Cyan?"))    #Cyan 19.9E-2
D5 = float(input("What is D Blue?"))    #Blue 23.1E-2
D6 = float(input("What is D Violet?"))    #Violet 25.5E-2"""

#Scale Readings for the Mercury Spectrum (Replace the readings here)
D1 = 16.4E-2      #Orange
D2 = 16.8E-2      #Yellow
D3 = 17.8E-2    #Green
D4 = 19.9E-2    #Cyan
D5 = 23.1E-2    #Blue
D6 = 25.5E-2    #Violet

#Scale Readings for the Absorption Bands
k1 = 16.5E-2    #Band1 Left
k2 = 16.7E-2    #Band1 Right
k3 = 17.5E-2    #Band2 Left
k4 = 18E-2  #Band2 Right
k5 = 18.4E-2    #Band3 Left
k6 = 18.6E-2    #Band3 Right
k7 = 19E-2  #Band4 Left
k8 = 19.5E-2    #Band4 Right

#Assign variables to switch for different values
Question = float(input("Enter 0 \n(for calculating BLUE,GREEN and ORANGE) \nor Enter 1 \n(for calculating VIOLET, GREENISH-BLUE and YELLOW):"))
bandwidth = float(input("Do you want to calculate the bandwidth of absorption spectrum? \n(0 == NO, 1 == YES)"))
MasterControl = Question
if MasterControl == 0:
    l1 = L6
    l2 = L4
    l3 = L2
    d1 = D6
    d2 = D4
    d3 = D2
    dwav = D5
else:
    l1  =   L5
    l2  =   L3
    l3  =   L1
    d1  =   D5
    d2  =   D3
    d3  =   D1

d0 = (((l1-l2)*(d2-d3)*d1)-((l3-l2)*(d2-d1)*d3))/(((l1-l2)*(d2-d3))-((l3-l2)*(d2-d1)))
C = (l3-l2)*(d3-d0)*(d2-d0)/(d3-d2)
l0 = l1 - (C/(d0-d1))

if MasterControl==0:
# For Blue
    Wav = l0 + (C/(d0-D5))
    print ("Wavelength of Blue = ", Wav)

    Err = ((Wav - L5)/L5)*100
    print ("Error = ", Err,"%", "\n")

#For Green
    Wav2 = l0 + (C/(d0-D3))
    print ("Wavelength of Green = ", Wav2)

    Err2 = ((Wav2 - L3)/L3)*100
    print ("Error = ", Err2,"%", "\n")

#For Orange
    Wav3 = l0 + (C/(d0-D1))
    print ("Wavelength of Orange = ", Wav3)

    Err3 = ((Wav3 - L1)/L1)*100
    print ("Error = ", Err3,"%", "\n")
else:
    # For Violet
    Wav = l0 + (C/(d0-D6))
    print ("Wavelength of Violet = ", Wav)

    Err = ((Wav - L6)/L6)*100
    print ("Error = ", Err,"%", "\n")

    #For Cyan
    Wav2 = l0 + (C/(d0-D4))
    print ("Wavelength of Cyan = ", Wav2)

    Err2 = ((Wav2 - L4)/L4)*100
    print ("Error = ", Err2,"%", "\n")

    #For Yellow
    Wav3 = l0 + (C/(d0-D2))
    print ("Wavelength of Yellow = ", Wav3)

    Err3 = ((Wav3 - L2)/L2)*100
    print ("Error = ", Err3,"%", "\n")

print("\n Parameters")
print("d0 = ",d0)
print("C = ",C)
print("l0 = ", l0,"\n")

K = [k1,k2,k3,k4,k5,k6,k7,k8]
Kw = ["Left Band#1","Right Band#1","Left Band#2","Right Band#2","Left Band#3","Right Band#3","Left Band#4","Right Band#4"]
Y = []

if bandwidth==1:
 for x in range(0,8):
    y = K[x]
    z = l0 + (C/(d0-y))
    Y.append(z)
    print ("Wavelength of",Kw[x],"=",Y[x])

    if x==1:
        print("Bandwidth = ",Y[0]-Y[1])
        print("\n")
    elif x==3:
        print("Bandwidth = ",Y[2]-Y[3])
        print("\n")
    elif x==5:
        print("Bandwidth = ",Y[4]-Y[5])
        print("\n")
    elif x==7:
        print("Bandwidth = ", Y[6]-Y[7])


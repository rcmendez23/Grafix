
#Constant Variables
PLATE_MAX = 75 #in mm
PLATE_MIN = -75 #in mm

#User Input
funcType = input("Enter Function Type f=cartesian, p=polar, pa=parametric: ")

#Polynomial Functions
if funcType == "f":
    while True:
        XMin = float(input("X Min: ")) #Minimum X value
        XMax = float(input("X Max: "))
        if XMin >= XMax:
            print ('Please enter max value that is greater than min value.')
        else:
           break
    funcRange = (XMax - XMin) #Window Range
    step =(funcRange)/10.0 #x increment
    print('step: ', step)
    funcStr = input("Enter Function using x as variable and ** for exponentiation: ")
    funcTable = [[],[]] #create empty 2d list for function coordinates
    machCoords=[[],[]] #create empty 2d list for machine coordinates
    x=XMin #Set counter to minimum X value
    while((x>=XMin) & (x<=XMax)): #For each X coordinate
        y = eval(funcStr) #Convert funcStr to executable function of x
        funcTable[0].append(x) #Save points to array
        funcTable[1].append(y) #Save points to array
        x+=step #Increment x by step
    print(funcTable) #debug
else: #If user does not enter 'f'
    print("Sorry, we only have cartesian 'f' capability at the moment.")
    

#Scale points to mm coords on build plate
plateRange = (PLATE_MAX - PLATE_MIN) 
for n in range(len(funcTable[0])):
    machCoords[0].append((((funcTable[0][n] - XMin) * plateRange) / funcRange) + PLATE_MIN) #Scale funcTable values into machCoords table
    machCoords[1].append((((funcTable[1][n] - XMin) * plateRange) / funcRange) + PLATE_MIN) #Scale funcTable values into machCoords table
    print(machCoords[0][n],"    ", machCoords[1][n]) #debug
    
#Create GCode File
f = open('gcode_file.gcode', 'w') #Open G-Code File to Write
f.write("G21 G01 F10 X0 Y0\n") #units set to mm go to center to start
for i in range(len(machCoords[0])):
    X = machCoords[0][i]
    Y = machCoords[1][i]
    f.write("G01 ")
    f.write("X"+ str(X))
    f.write(" Y"+ str(Y))
    f.write("\n")

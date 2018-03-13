'''
G-Code File Generator for Grafix Accessible CNC Calculator
By Rebecca Mendez
User inputs a mathematical function. A table of points for that function is generated, scaled to workspace size and GCode is then generated. 
Only supports polynomial functions right now.
TODO: 
- Copy past GCode Files to a separate "history" folder.
'''

PLATE_MAX = 100
PLATE_MIN = -100

#User Input
funcType = input("Enter Function Type (poly): ")

#Polynomial Functions
if funcType == "poly":
    XMin = input("X Min: ") #Minimum X value
    XMax = input("X Max:" )
    funcRange = (XMax - XMin) #Window Range
    step = (funcRange)/30 #x increment
    funcStr = input("Enter Function using x as variable and ^ for powers: ")
    funcTable = [[],[]] #create empty 2d list
    for x in range(XMin, XMax, step): #For each X coordinate
        y = exec(funcStr) #Convert funcStr to executable function of x
        funcTable[0].append(x) #Save points to array
        funcTable[1].append(y) #Save points to array
        print(funcTable[n][k]) #debug

#Scale points to mm coords on build plate
plateRange = (PLATE_MAX - PLATE_MIN) 
for n in range(len(funcTable[0]))
    for k in range(len(funcTable[1]))
        machCoords[n][k].append((((funcTable[n][k] - XMin) * plateRange) / funcRange) + PLATE_MIN) #Scale funcTable values into machCoords table
        print(machCoords[n][k]) #debug
    
#Create GCode File
f = open('gcode_file', 'w') #Open G-Code File to Write
f.write("G21 G0 X0 Y0") #units set to mm go to center to start
for i in range(len(machCoords[0]))
    for j in range(len(machCoords[1]))
        X = machCoords[i]
        Y = machCoords[j]
        f.write("X"+ str(X))
        f.write("Y"+ str(Y))
        f.write("\n")
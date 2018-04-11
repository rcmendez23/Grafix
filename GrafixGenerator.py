'''
G-Code File Generator for Grafix Accessible CNC Calculator
By Rebecca Mendez
3/14/18
Last Updated: 3/17/18
User inputs a mathematical function. A table of points for that function is generated, scaled to workspace size and GCode is then generated. 
Only supports polynomial functions right now.
TODO: 
- Copy past GCode Files to a separate "history" folder.
'''
#Constant Variables
PLATE_MAX = 150 #in mm
PLATE_MIN = 0 #in mm
run = 1 #is program running?
e = 2.17 #numeric definition of e

while(run == 1):
    #User Input
    funcType = input("Enter Function Type f=cartesian, p=polar, pa=parametric: ")

    #Polynomial Functions
    if funcType == "f":
        XMin = float(input("X Min: ")) #Minimum X value
        XMax = float(input("X Max:" ))
        if(XMin >= XMax): #if XMin is greater than 
            print("XMin must be less than XMax.")
        funcXRange = (XMax - XMin) #Window Range
        step =(funcXRange)/10.0 #x increment
        print('step: ', step)
        funcStr = input("Enter Function using x as variable and ** for powers: ")
        funcTable = [[],[]] #create empty 2d list for function coordinates
        machCoords=[[],[]] #create empty 2d list for machine coordinates
        x=XMin #Set counter to minimum X value
        while((x>=XMin) & (x<=XMax)): #For each X coordinate
            y = eval(funcStr) #Convert funcStr to executable function of x
            funcTable[0].append(x) #Save points to array
            funcTable[1].append(y) #Save points to array
            x+=step #Increment x by step
        for i in range(len(funcTable[0])):
            print(funcTable[0][i],"    ", funcTable[1][i]) #debug
        print("------------------------")
    
        YMin = min(funcTable[1]) #Find first Y value (minimum Y) using funcTable array
        YMax = max(funcTable[1])
        print("Y Min: ",YMin) #debug
        print("len(funcTable): ",len(funcTable[1])) #debug
        funcYRange = abs(YMax-YMin) #get range of Y values
        print("funcYRange ",funcYRange) #debug

        #Scale points to mm coords on build plate
        plateRange = (PLATE_MAX - PLATE_MIN) 
        for n in range(len(funcTable[0])):
            machCoords[0].append((((funcTable[0][n] - XMin) * plateRange) / funcXRange) + PLATE_MIN) #Scale funcTable values into machCoords table
            machCoords[1].append((((funcTable[1][n] - YMin) * plateRange) / funcYRange) + PLATE_MIN) #Scale funcTable values into machCoords table
            print(machCoords[0][n],"    ", machCoords[1][n]) #debug
            
        #Create GCode File
        f = open('grafix.gcode', 'w') #Open G-Code File to Write
        f.write("G21 G01 F70\n") #units set to mm go to center to start
        for i in range(len(machCoords[0])):
            X = machCoords[0][i]
            Y = machCoords[1][i]
            f.write("G01 ")
            f.write("X"+ str(X))
            f.write(" Y"+ str(Y))
            f.write("\n")
            #If user does not enter 'f'
    else:
        print("Sorry, we only have cartesian 'f' capability at the moment.")
    run = 0
import turtle
import math
edges = {}
currentEdge = ''
endEdge = ''
nextX = 0
nextY = 0

#draws the net of a cube with dimension x
def prism(x,y,z):
    global edges



    #A dictionary of all the edges of a cube
    #format:(x1,y1, x2,y2, turtle.heading, edges that share a face)
    #Note that there are 2 edges per letter, these edges correspond to each other
    edges = {'A0' : (0, 0, x, 0, 0,   'F1', 'B0', 'H0'),
             'A1' : (0, 2*z+2*y, x, 2*z+2*y, 0,'E0', 'J1', 'D1'),
             'B0' : (x, 0, x, y, 90,   'A0', 'F1', 'H0'),
             'B1' : (x+z, 2*y+z, x+z, y+z, 270, 'D0', 'L1', 'C1'),
             'C0' : (x, y, x, y+z, 90,  'I0', 'G1', 'H1'),
             'C1' : (x+z, y+z, x, y+z, 180, 'L1', 'B1', 'D0'),
             'D0' : (x, 2*y+z, x+z, 2*y+z, 0,  'L1', 'C1', 'B1'),
             'D1' : (x, 2*y+z, x, 2*y+2*z, 90, 'E0', 'A1', 'J1'),
             'E0' : (0, 2*y+2*z, 0, 2*y+z, 270, 'A1', 'D1', 'J1'),
             'E1' : (0-z, 2*y+z, 0, 2*y+z, 0,  'F0', 'G0', 'K0'),
             'F0' : (0-z, 2*y+z, 0-z, y+z, 270, 'E1', 'K0', 'G0'),
             'F1' : (0, 0, 0, y, 90,   'H0', 'B0', 'A0'),
             'G0' : (0-z, y+z, 0, y+z, 0, 'F0', 'K0', 'E1'),
             'G1' : (0, y, 0, y+z, 90,  'H1', 'C0', 'I0'),
             'H0' : (0, y, x, y, 0,  'F1', 'B0', 'A0'),
             'H1' : (0, y, x, y, 0,  'G1', 'C0', 'I0'),
             'I0' : (0, z+y, x, z+y, 0,   'G1', 'H1', 'C0'),
             'I1' : (0, z+y, x, z+y, 0,   'K1', 'L0', 'J0'),
             'J0' : (0, 2*y+z, x, 2*y+z, 0,  'K1', 'L0', 'I1'),
             'J1' : (0, 2*y+z, x, 2*y+z, 0,  'E0', 'A1', 'D1'),
             'K0' : (0, y+z, 0, 2*y+z, 90,  'E1', 'F0', 'G0'),
             'K1' : (0, y+z, 0, 2*y+z, 90,  'J0', 'L0', 'I1'),
             'L0' : (x, y+z, x, 2*y+z, 90,  'J0', 'K1', 'I1'),
             'L1' : (x, y+z, x, 2*y+z, 90,  'D0', 'B1', 'C1'),
             }
    #For each edge in the edge table, the edge is drawn
    
    for edge in edges:
        print(edge)
        turtle.pu()
        turtle.goto(edges[edge][0], edges[edge][1])
        turtle.pd()
        turtle.goto(edges[edge][2], edges[edge][3])
    

#returns the distance between two points
def distance(x1,y1,x2,y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist

#Inputs: current edge, a position, and an angle
#Result: finds the edge on the same face which a ray would intersect
def setNext(edge, x0, y0, theta):
    global endEdge, nextX, nextY
    #tests each of the edges which a given edge shares a face with
    for i in range(5, len(edges[edge])):
        potentialEdge = edges[edge][i]
        x1= edges[potentialEdge][0]
        y1= edges[potentialEdge][1]
        x2= edges[potentialEdge][2]
        y2= edges[potentialEdge][3]
        #calculating intersection pt of each set of lines, sets this as x and y
        m1 = math.tan(math.radians(theta))
        if(x2==x1):
            x=x1
        else: 
            m2 = ((y2-y1)/(x2-x1))
            x = ((m1*x0 - x1*m2 + y1 - y0)/(m1-m2))
        y = m1*(x-x0)+y0
        print(x)
        print(y)
        #setting nextEdge, nextX, nextY if the solution (x,y) for an edge is between (x1,y1) and (x2,y2)
        if((min(y1,y2)-1e-10)<= y <=(max(y1,y2)+1e-10)) and (min(x1,x2) <= x <= max(x1,x2)):
            endEdge = potentialEdge
            nextX=x
            nextY=y
            print(endEdge)
            print(str(nextX) + "," + str(nextY))
  
            

            
            
        
def jump(edge, length, angle):
    
    global currentEdge
    currentEdge = edge
    #Moving into position
    turtle.pu()
    #Go to length on edge
    turtle.goto(edges[edge][0]+length*math.cos(math.radians(edges[edge][4])),edges[edge][1]+length*math.sin(math.radians(edges[edge][4])))
    turtle.setheading(angle)
    turtle.pd()
    print("jumped to:" + str(turtle.xcor()) + ", " + str(turtle.ycor()))
    
    setNext(currentEdge, turtle.xcor(), turtle.ycor(), angle)
    turtle.goto(nextX, nextY)
    print("went to:" + str(nextX) + ", " + str(nextY))
    nextEdge = str(endEdge[0])+ str((int(endEdge[1])+1)%2)
    nextLength = distance(turtle.xcor(), turtle.ycor(), edges[endEdge][0], edges[endEdge][1])
    nextAngle = ((edges[nextEdge][4] - edges[endEdge][4] + angle)%360)
    print("jump(" + str(nextEdge) + ", " + str(nextLength) + ", " + str(nextAngle) + ")")
    jump(nextEdge, nextLength, nextAngle)
    
    



prism(50,50,50)
jump('A0', 25, 30)


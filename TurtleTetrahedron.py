import turtle
import math
edges = {}
currentEdge = ''
endEdge = ''
nextX = 0
nextY = 0


def square(x):
    for edge in range(4):
            turtle.forward(x)
            turtle.left(90)
            

#draws 4 squares around origin as a reference point           
def markOrigin(x):
    turtle.pu()
    turtle.goto(0, 0)
    turtle.pd()
    square(x)
    for squares in range(4):
        square(x)
        turtle.left(90)
    return

#draws the net of a cube with dimension x
def tetrahedron(x):
    global edges

    #markOrigin() is a function for the viewer to have a frame of reference
    #markOrigin(x/10)


    #A dictionary of all the edges of a tetrahedron
    #format:(x1,y1, x2,y2, turtle.heading, edges that share a face)
    #Note that there are 2 edges per letter, these edges correspond to each other
    edges = {'A0' : (x*0,   x*0,            x*1,   x*0,              0,   'C1', 'D0'),
             'A1' : (x*2,   x*0,            x*1,   x*0,              180,   'B0', 'E0'),
             'B0' : (x*2,   x*0,            x*1.5, x*math.sqrt(3)/2, 120,   'A1', 'E0'),
             'B1' : (x*1,   x*math.sqrt(3), x*1.5, x*math.sqrt(3)/2, 300, 'C0', 'F0'),
             'C0' : (x*1,   x*math.sqrt(3), x*0.5, x*math.sqrt(3)/2, 240,  'B1', 'F0'),
             'C1' : (x*0,   x*0,            x*0.5, x*math.sqrt(3)/2, 60, 'A0', 'D0'),
             'D0' : (x*1,   x*0,            x*0.5, x*math.sqrt(3)/2, 120,  'C1', 'A0'),
             'D1' : (x*1,   x*0,            x*0.5, x*math.sqrt(3)/2, 120,  'E1', 'F1'),
             'E0' : (x*1,   x*0,            x*1.5, x*math.sqrt(3)/2, 60, 'B0', 'A1'),
             'E1' : (x*1,   x*0,            x*1.5, x*math.sqrt(3)/2, 60, 'D1', 'F1'),
             'F0' : (x*0.5, x*math.sqrt(3)/2, x*1.5, x*math.sqrt(3)/2, 0, 'C0', 'B1'),
             'F1' : (x*0.5, x*math.sqrt(3)/2, x*1.5, x*math.sqrt(3)/2, 0, 'D1', 'E1'), 
             }
    #For each edge in the edge table, the edge is drawn
    
    for edge in edges:
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
        #setting nextEdge, nextX, nextY if the solution (x,y) for an edge is between (x1,y1) and (x2,y2)
        if(((min(y1,y2)-1e8)<= y <=(max(y1,y2)+1e8)) and (min(x1,x2) <= x <= max(x1,x2))):
            endEdge = potentialEdge
            nextX=x
            nextY=y
            
            
        
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
    
    



tetrahedron(100)
jump('A0', 10, 30)

    


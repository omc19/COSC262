import time
"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: Oscar McLaren
   Usercode: omc19
"""


def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    file = open(filename)
    listPts = []
    for i in range(N):
        line = file.readline()
        x = line.split(" ")
        a = x[0].strip()
        b = x[1].strip()
        tup = (float(a), float(b))
        listPts.append(tup)
    return listPts


def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    h = listPts
    min_y_value = 0
    Pk = (0,0) #min point
    i = 0 
    v = 0 
    k = 0 #i = current position in the array
    Pk = minimumY(h)
    h.append(Pk)
    k = h.index(Pk) #index
    chull = [] 
    while k != (len(h) - 1):
        h[i], h[k] = h[k], h[i]
        min_Angle = 361
        chull.append(h[i])
        for b in range(i+1, len(h)):
            angle = theta(h[i], h[b])
            if angle < min_Angle and angle > v and h[b] != h[i]:
                min_Angle = angle
                k = b
            #elif min_Angle == angle:
        i += 1
        v = min_Angle
    return chull
                        
    
    #return chull

def theta(pointA, pointB):
    ''' Computes an approximation of the angle between
    the line AB and a horizontal line through A.
    '''
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))

    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    if t == 0:
        return 360.00
    else:
        return t*90 

def dist(ptA, ptB):
    """calculate the distance between two points"""
    dx = ptA[0] - ptB[0]
    dy = ptA[1] - ptB[1]
    distance = (dx*dx) + (dy*dy)

def minimumY(listPts):
    """Function to find minimum y value"""
    min_y_value = 0
    Pk = (0,0)  
    for a in listPts:
        if min_y_value == 0:
            min_y_value = a[1]
            Pk = a
        elif min_y_value > a[1]:
            min_y_value = a[1]
            Pk = a
        elif min_y_value == a[1]:
            maxy = a[0]
            if maxy > Pk[0]:
                Pk = a   
    return Pk


def simpleClosedPath(listPts, min_y):
    """Simple closed path algorithm"""
    angles = [] 
    scp_list = [] #simple closed path list
    k = listPts.index(min_y)
    for i in range(0, len(listPts)):
        angle = theta(listPts[k], listPts[i])
        if angle == 360:
            angle = 0
        angles.append((angle, i))
    angles.sort()
    for j in angles:
        scp_list.append(listPts[j[1]])
    return scp_list
    
def lineFn(ptA, ptB, ptC):
    """line function"""
    return(((ptB[0]-ptA[0])*(ptC[1]-ptA[1])) - ((ptB[1]-ptA[1])*(ptC[0]-ptA[0])))
    
def isCCW(ptA, ptB, ptC):
    """Check if c makes a clockwise turn"""
    return lineFn(ptA, ptB, ptC) > 1.e-6


def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """
    pts = listPts  
    h = []
    Pk = minimumY(pts)
    simple = simpleClosedPath(pts, Pk)
    for i in range(0, 3):
        h.append(simple[i])
    for j in range(3, len(simple)):
        while not isCCW(h[-2], h[-1], simple[j]): #While False
            h.pop()
        h.append(simple[j]) #When it is CCW = True append
    return h[1:]
    
    
def xFirst_Y_Next(listPts):
    """Sort thelistPts by x values, if same x then by y values"""
    pts_sorted = sorted(listPts)
    return pts_sorted


def monotoneChain(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    pts = xFirst_Y_Next(listPts)
    upperHull = []
    lowerHull = []
    for i in pts:
        while len(lowerHull) >= 2 and not isCCW(lowerHull[-2], lowerHull[-1], i):
            lowerHull.pop()
        lowerHull.append(i)
    for j in reversed(pts):
        while len(upperHull) >= 2 and not isCCW(upperHull[-2], upperHull[-1], j):
            upperHull.pop()
        upperHull.append(j)
        
    hull_combined = lowerHull[:-1] + upperHull[:-1]       
       
    return hull_combined


def main():
    listPts = readDataPts('Set_B.dat', 30000)  #File name, numPts given as example only
    start_time = time.time()
    #print(giftwrap(listPts))      #You may replace these three print statements
    print("--- %s seconds ---" %(time.time() - start_time))
    print(" ")
    start_time2 = time.time()
    #print (grahamscan(listPts))   #with any code for validating your outputs
    print("--- %s seconds ---" %(time.time() - start_time2))
    print(" ")
    start_time3 = time.time()
    print(monotoneChain(listPts))
    print("--- %s seconds ---" %(time.time() - start_time3))



 
if __name__  ==  "__main__":
    main()
  
  
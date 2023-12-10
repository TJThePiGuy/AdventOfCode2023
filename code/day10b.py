import helper.aocdUtil as util

data = util.getData(10,2023,False).split('\n')
width = len(data[0])
height = len(data)

startPos = None
for y in range(height):
    for x in range(width):
        if data[y][x] == 'S':
            startPos = (x,y)

rules = [
    (1,0, '-J7', '-FLS'),
    (-1,0,'-FL', '-J7S'),
    (0,1, '|JL', '|F7S'),
    (0,-1,'|F7', '|JLS')]

pointsVisited = []
pointsToVisit = [startPos]
while(len(pointsToVisit) != 0):
    nextPoints = []
    for point in pointsToVisit:
        x,y = point
        currChar = data[y][x]
        for (dx,dy,endChars, startChars) in rules:
            if not(currChar in startChars) :
                continue
            if not(x+dx in range(width) and y+dy in range(height)):
                continue
            if (x+dx,y+dy) in pointsVisited:
                continue
            if data[y+dy][x+dx] in endChars:
                nextPoints.append((x+dx,y+dy))
        pointsVisited.append(point)
    pointsToVisit = nextPoints.copy()

areaEnclosed = 0
for y in range(height):
    enclosed = False
    inWall = False
    wallChar = ''
    for x in range(width):
        currChar = data[y][x]
        if (x,y) in pointsVisited:
            if currChar in '|':
                enclosed = not enclosed
            elif data[y][x] in 'FL':
                inWall = True
                wallChar = currChar
            elif data[y][x] in '7J':
                inWall = False
                if (wallChar == 'F' and currChar == 'J') or (wallChar == 'L' and currChar == '7'):
                    enclosed = not enclosed
        else:
            areaEnclosed += int(enclosed)
util.submit(areaEnclosed, 10,2023,'b')
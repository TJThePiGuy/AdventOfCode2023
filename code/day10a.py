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
steps = 0
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

    steps += 1
util.submit(steps-1,10,2023,'a')
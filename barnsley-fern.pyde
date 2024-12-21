x = 0
y = 0

def setup():
    size(800, 1000)
    background(0)
    stroke(0, 255, 0)
    noLoop()

def draw():
    global x, y
    for i in range(50000):
        r = random(1)
        if r < 0.01:
            nextX = 0
            nextY = 0.16 * y
        elif r < 0.86:
            nextX = 0.85 * x + 0.04 * y
            nextY = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            nextX = 0.2 * x - 0.26 * y
            nextY = 0.23 * x + 0.22 * y + 1.6
        else:
            nextX = -0.15 * x + 0.28 * y
            nextY = 0.26 * x + 0.24 * y + 0.44

        plotX = map(nextX, -2.182, 2.6558, 0, width)
        plotY = map(nextY, 0, 9.9983, height, 0)

        point(plotX, plotY)

        x = nextX
        y = nextY

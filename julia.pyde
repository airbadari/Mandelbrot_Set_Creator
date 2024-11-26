from random import randint

class Complex(object):
    def __init__(self,r,c):
        self.r = r
        self.c = c
       
pal = []
def setPallete():
    for i in range(75):
        pal.append(randint(0,256))

def setup():
    size(900,900)
    background(255)
    colorMode(RGB)
    noLoop()
 
def draw():
    global pal
    frameRate(10000)
    stroke(0)
    setPallete()
    maxIter = 40

    c = Complex(-0.4, 0.6)  # dendrite-like structure
    # c = Complex(0.285, 0)   # rabbit-like structure
    # c = Complex(-0.70176, -0.3842)  # Siegel disk
    # c = Complex(-0.4, 0.6)  # interesting dendrite pattern

    for x in range(width):
        for y in range(height):
            # Use screen coordinates as initial z value
            z = Complex(-2 + 4.0 * x / width, 2 - 4.0 * y / height)
            iter = 0

            while(iter < maxIter) and (z.r**2 + z.c**2 < 4):
                temp = z.r
                z.r = temp**2 - z.c**2 + c.r
                z.c = 2 * temp * z.c + c.c
                iter += 1

            if iter == maxIter:
                stroke(0,0,0)
                point(x,y)
            else:
                t = iter % 25
                stroke(pal[3*t], pal[3*t+1], pal[3*t+2])
                point(x,y)

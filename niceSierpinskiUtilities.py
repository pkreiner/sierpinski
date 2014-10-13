from utilities import *

# takes a point in space and returns a pair (pixels, colors),
# where pixels and colors are each length-4 lists.
# This essentially portions out a black square of side length
# sideLength <=1 among the four pixels it might overlap.
def pointToFourPixels(point, sideLength, center, scale):
	# print point
	point = np.array(point)
	u = point * scale
	u[1] = -u[1]
	u += center
	x, y = u

	def nearestIntsWithPortions(x, sideLength):
		n = int(math.floor(x))
		a = (n + 0.5) - (x - sideLength/2.0)
		if a < 0:
			a = 0
		b = (x + sideLength/2.0) - (n + 0.5)
		if b < 0:
			b = 0
		return ((n, a), (n+1, b))

	xInts = nearestIntsWithPortions(x, sideLength)
	yInts = nearestIntsWithPortions(y, sideLength)

	fourIntsWithPortions = [((xElt[0], yElt[0]), xElt[1]*yElt[1]) \
							for xElt in xInts for yElt in yInts]
	return fourIntsWithPortions


def addPointToMatrix(point, sideLength, matrix, center, scale):
	fourPixelPortions = pointToFourPixels(point, sideLength, center, scale)
	for pixelPortion in fourPixelPortions:
		i, j = pixelPortion[0]
		portion = pixelPortion[1]
		matrix[i][j] += portion

# We have several functions below that draw simply by changing
# a pixel array passed to them. 
# (This is different from the drawing functions in utilities.py,
# Which just call PyGame's built-in drawing functions.)
# 'matrix' is a numpy array containing floats between 0 (white) and 1 (black)
# 'pixelArray' is a numpy array containing (r,g,b) triples

# updates only part of the pixel array
def drawFromMatrixLimited(pixelArray, matrix, pixels, f):
	for (x, y) in pixels:
		pixelArray[x][y] = f(matrix[x][y])

def drawPoint(point, sideLength, matrix, pixelArray, center, scale, f):
	fourPixelPortions = pointToFourPixels(point, sideLength, center, scale)
	for pixelPortion in fourPixelPortions:
		i, j = pixelPortion[0]
		portion = pixelPortion[1]
		matrix[i][j] += portion
		drawFromMatrixLimited(pixelArray, matrix, [(i, j)], f)

def drawPointGrey(point, sideLength, matrix, pixelArray, \
					center, scale):	
	def RToGrey(r):
		if r < 0: r = 0
		if r > 1: r = 1
		c = int((1.0 - r) * 255)
		return (c, c, c)
	drawPoint(point, sideLength, matrix, pixelArray, \
				center, scale, RToGrey)


# These functions were used to explore variations to the 
# updating rule. Instead of using taking the midpoint between
# the current point and a random base point, you can take a
# weighted average, or other things.

def midpoint(p, q):
	return (p + q)/2.0
def weightedMidpoint(p, q, w):
	return w*p + (1.0-w)*q
def norm(u):
	return np.sqrt(np.square(u[0])+np.square(u[1]))
def sqrtMidpoint(p, q):
	d = norm(p-q)
	if d == 0.0:
		w = 0
	else:
		w = np.sqrt(d)/d
	print w
	return p + w*(q-p)

# Try with e.g. alpha = 0.3
def logMidpoint(p, q, alpha):
	d = norm(p-q)
	if d == 0.0:
		w = 0
	else:
		w = np.exp(alpha * np.log(d))/d
	return p + w * (q - p)

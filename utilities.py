import pygame, sys, random, time, math
import numpy as np
from pygame.locals import *

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
grey = 128, 128, 128
niceBlue = 85, 108, 255
violet = 255, 0, 255
lightRed = 255, 127, 127
lightBlue = 127, 127, 255
lightGreen = 127, 255, 127
lightViolet = 255, 127, 255

# Maps from abstract coordinates to actual (x, y) pixel locations. 
# Returns (int, int)
# point and center should be numpy arrays
# center is where the origin should be mapped to;
# scale: a scale of s means that a unit vector gets mapped to a vector of length s.
def pointToPixel(point, center, scale):
	point = np.array(point)
	u = point * scale
	u[1] = -u[1]  # increasing y should be up on the screen
	u += center
	pixel = tuple([int(c) for c in u])
	return pixel

def pixelToPoint(pixel, center, scale):
	scale = float(scale)
	point = (np.array(pixel) - center) / scale
	point[1] = -point[1]
	return point

# draws a horizontal and a vertical line, across the surface,
# that cross at the center
def drawAxes(surface, center, size, color = black, width = 1):
	x, y = int(center[0]), int(center[1])
	maxX, maxY = size
	# draw horizontal line
	pygame.draw.line(surface, color, (0, y), (maxX, y), width)
	# draw vertical line
	pygame.draw.line(surface, color, (x, 0), (x, maxY), width)

def drawPoint(surface, point, center, scale, color=black, radius=1):
	pixel = pointToPixel(point, center, scale)
	pygame.draw.circle(surface, color, pixel, radius)

def drawLine(surface, start, end, center, scale, color=black, width=1):
	startPixel = pointToPixel(start, center, scale)
	endPixel = pointToPixel(end, center, scale)
	pygame.draw.line(surface, color, startPixel, endPixel, width)

def matrixFromColumns(xImage, yImage):
	return np.array([xImage, yImage]).transpose()
def columnsFromMatrix(M):
	return M.transpose()

def drawVerticalBar(surface, size, width, color=black):
	left = size[0]/2 - width/2
	height = size[1]
	rect = pygame.Rect((left, 0), (width, height))
	pygame.draw.rect(surface, color, rect)

# draws the parallelogram with points 0, u, v, u+v
def drawParallelogram(surface, u, v, center, scale, \
					  colors=[black]*4, width=1):
	# for concise drawLine
	def cDrawLine(start, end, color):
		drawLine(surface, start, end, center, scale, color, width)
	zero = np.array([0, 0])
	w = u + v
	cDrawLine(zero, u, colors[0])
	cDrawLine(zero, v, colors[1])
	cDrawLine(v, w, colors[2])
	cDrawLine(u, w, colors[3])
def drawParallelogramFromMatrix(surface, M, center, scale, \
								colors=[black]*4, width=1):
	MT = M.transpose()
	u = MT[0]
	v = MT[1]
	drawParallelogram(surface, u, v, center, scale, colors, width)

class callEvery:
	def __init__(self):
		self.lastCall = 0

	# calls f if more than 'duration' seconds have passed
	# since last call
	def call(self, f, duration):
		if time.time() - self.lastCall > duration:
			f()
			self.lastCall = time.time()

class MyClock:
	def __init__(self):
		self.startTime = time.time()
		self.lastTime = self.startTime
	def time(self):
		t = time.time()
		self.lastTime = t
		return t - self.startTime
	def sinceLast(self):
		t = time.time()
		elapsed = t - self.lastTime
		self.lastTime = t
		return elapsed
	def mark(self):
		self.markTime = time.time()
	def sinceMark(self):
		return time.time() - self.markTime

	
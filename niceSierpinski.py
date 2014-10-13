# This program draws fractal shapes generalized from the Sierpinski triangle.
# To start, left-click on the screen to make some number
# (say, three) of base points.
# Then right click to begin the drawing.
# The drawing works as follows. At each step, we have a current point.
# We pick one of the base points at random and move the current point
# halfway to it, and draw a dot on the current point.
# The first current point is simply the first base point.

# Fun shapes to try include triangles, trapezoids, pentagons, hexagons.

import utilities as utils
import niceSierpinskiUtilities as niceUtils
# from utilities import *
# from niceSierpinskiUtilities import *
from numpy import *
import pygame
from pygame.locals import *

pygame.init()
clock = utils.MyClock()

width, height = 1200, 600
size = (width, height)
screen = pygame.display.set_mode((width, height))
screen.fill(utils.white)
screenMatrix = zeros((width, height))
print "Time to initialize screen and screenMatrix:", clock.sinceLast()

center = width/2, height/2
scale = 300

# Starting points for the process,
# Entered later by the user
basePoints = []

mode = 'setting'
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if mode == 'setting':
			if event.type == MOUSEBUTTONUP:
				if event.button == 1: 	# left mouse button click
					pos = pygame.mouse.get_pos()
					p = utils.pixelToPoint(pos, center, scale)
					basePoints.append(p)
					utils.drawPoint(screen, p, center, scale, utils.black, 2)
				if event.button == 3:	# right mouse button click
					mode = 'starting'

	if mode == 'starting':
		p = array(basePoints[0])  # one of the functions down the line needs
								  # p to be of type np.array
		count = 0
		pixelArray = pygame.PixelArray(screen)
		clock.mark()
		mode = 'running'

	if mode == 'running':
		i = random.randint(0, len(basePoints))
		p = niceUtils.midpoint(p, array(basePoints[i]))
		niceUtils.drawPointGrey(p, 1, screenMatrix, pixelArray, center, scale)

		if clock.sinceMark() > 10:
			print count, " dots."
			clock.mark()
		count += 1

	pygame.display.update()

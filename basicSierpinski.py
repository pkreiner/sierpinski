from utilities import *
from niceSierpinskiUtilities import *
from numpy import *
import pygame

pygame.init()
clock = MyClock()

width, height = 1200, 600
size = (width, height)
screen = pygame.display.set_mode((width, height))
screen.fill(white)
screenMatrix = zeros((width, height))
print "Time to initialize screen and screenMatrix:", clock.sinceLast()

center = width/2, height/2
scale = 300

basePoints = [(0, 1), (-1*sqrt(3)/2, -1.0/2), (sqrt(3)/2, -1.0/2)]

count = 0
p = array(basePoints[0])
# drawAxes(screen, center, size)
pixelArray = pygame.PixelArray(screen)
clock.mark()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	i = random.randint(0, len(basePoints))
	p = midpoint(p, array(basePoints[i]))
	drawPointGrey(p, 0.5, screenMatrix, pixelArray, center, scale)

	if clock.sinceMark() > 10:
		print count, " dots."
		clock.mark()

	count += 1
	t = clock.time()
	# pos = q(t)

	# screen.fill(white)
	# drawAxes(screen, center, size, width)
	# drawPoint(screen, pos, center, scale, radius=5)

	pygame.display.update()

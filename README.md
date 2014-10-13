sierpinski
==========

This is a couple of programs for exploring the Sierpinski triangle and similar shapes. It uses the process described in:
http://en.wikipedia.org/wiki/Sierpinski_triangle#Chaos_game

It's in Python, and uses numpy (for working with big arrays efficiently) and pygame (for the graphics).

utilities.py has functions for plotting in a coordinate system, where each any point (x, y) in the coordinate system gets mapped to a single pixel.

niceSierpinskiUtilities.py has functions for doing finer plotting, where each point is drawn by darkening the four pixels it lands closest to.
It also has functions for exploring variations of the basic algorithm (e.g. replacing the midpoint with a weighted average).

niceSierpinski.py lets the user enter a set of points (left-mouse clicks) on which the algorithm runs (start with a right-click). Three points, for example, generate the classic Sierpinski triangle.

basicSierpinski.py is the same, but instead of the user inputting points, it just starts with three preset points.

It's fun to experiment with variations of the Chaos Game: instead of just taking the midpoint of the current point and one of the base points, you can use another function that gives a point between them: a weighted average, a logarithmic average, etc. To try these out, just replace the line (in either basicSierpinski or NiceSierpinski)
p = midpoint(...)
with, for example,
p = logMidpoint(..., alpha=0.3). There are more such functions implemented in niceSierpinskiUtilities.py.

Enjoy!

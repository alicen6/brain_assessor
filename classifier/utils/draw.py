import pyglet
from pyglet.gl import *
from math import *


class RectangularButton():
	'''
	A generic rectangular button
	'''

	def __init__(self, text, value, x, y, w=200, h=50, color=[255, 255, 0], textcolor=[0,0,0,255], textsize = 14):
		self.text = text
		self.value = value
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color[:]
		self.textcolor = textcolor[:]
		self.textsize = textsize
		if len(self.textcolor) == 3:
			self.textcolor += [255]
		
		self.label = pyglet.text.Label(text, x = x + self.w//2, anchor_x = 'center', y = y - self.h//2, anchor_y = 'center', font_size = self.textsize, color=self.textcolor )


	def draw(self):
		'''
		Draw the button
		'''
		self.figure = rectangle(self.x, self.y, self.w, self.h, filled=True, color=self.color)
		self.figure.draw()
		self.label.draw()


	def changecolor(self, newcolor=[255,255,0]):
		'''
		change button color
		'''
		self.figure.delete()
		self.color = newcolor[:]
		self.draw()



class Figure():
	'''
	figure class
	'''
	def __init__(self, figure, mode):
		self.figure = figure
		self.drawmode = mode


	def draw(self):
		'''
		Draw the figure on the window
		'''
		self.figure.draw(self.drawmode)


	def delete(self):
		'''
		Delete the figure
		'''
		self.figure.delete()


def _setColor(color=[]):
	# pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
	if len(color) == 0:
		color = [255, 255, 0]
	pyglet.gl.glColor3f( color[0]/255.0 , color[1]/255.0 , color[2]/255.0 )


def square(x, y, length, **kwargs):
	'''
	returns a square figure
	'''
	return rectangle(x, y, length, length, **kwargs)


def rectangle(x, y, length, breadth, filled=True, color=[]):
	'''
	returns a rectangle figure
	'''
	verts = [x, y,
			x+length, y,
			x+length, y-breadth,
			x, y-breadth]
	shape = pyglet.graphics.vertex_list(4, ('v2i', verts))
	_setColor(color)
	return Figure(shape, GL_QUADS if filled else GL_LINE_LOOP)


def circle(xp, yp, radius, filled=True, color=[], numPoints=70):
	'''
	returns a circle figure
	'''
	verts = []
	xp += radius
	yp -= radius
	for i in range(numPoints):
		angle = radians(float(i)/numPoints * 360.0)
		x = radius*cos(angle) + xp
		y = radius*sin(angle) + yp
		verts += [x,y]
	circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))
	_setColor(color)
	return Figure(circle, GL_POLYGON if filled else GL_LINE_LOOP)


def hexagon(xp, yp, radius, filled=True, color=[]):
	'''
	returns a hexagon figure
	'''
	return circle(xp, yp, radius, filled, color, numPoints=6)


def triangle(x, y, length, filled=True, color=[]):
	'''
	returns a triangle figure
	'''
	verts = [x + length//2, y,
			x, y - length,
			x + length, y - length]
	shape = pyglet.graphics.vertex_list(3, ('v2i', verts))
	_setColor(color)
	return Figure(shape, GL_TRIANGLES)


def color2Array(rgb):
	'''
	Converts color to array
	'''
	if rgb[0:1] == '#':
		rgb = rgb[1:]
	r = int(rgb[0:2], 16)
	g = int(rgb[2:4], 16)
	b = int(rgb[4:], 16)
	return [r, g, b]
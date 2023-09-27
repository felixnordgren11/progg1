
import random
import turtle

class Dice:
	def __init__(self, sides):
		self.sides = sides
		self.value = random.randint(1, self.sides)

	def __str__(self):
		return f'Sidor: {self.sides:2d}, varde: {self.value:2d}'

	def roll(self):
		self.value = random.randint(1, self.sides)


class PokerDice:
	def __init__(self, number):
		self.dice_list = [Dice(6) for _ in range(number)]


	def number_of_dice(self, number):
		return number


	def __str__(self):
		res = []
		for d in self.dice_list:
			res.append(d.value)
		return str(sorted(res))


	def roll(self):
		for d in self.dice_list:
			d.roll() 	#Using the roll function from the Dice class to roll all the dice in PokerDice


class Rectangle:
	def __init__(self, height, width, xpos, ypos):
		self.height = height
		self.width = width
		self.xpos = xpos
		self.ypos = ypos

	def __str__(self):
		return f'The rectangle has height {self.height} and width {self.width}'

	def area(self, height, width):
		return f'The rectangle has an area of {self.height*self.width}'

	def draw(self):
		t = turtle.Turtle()
		t.speed(0)
		t.penup()
		t.goto(self.xpos, self.ypos)
		t.pendown()
		t.hideturtle()
		for dist in [self.width, self.height, self.width, self.height]:
			t.forward(dist)
			t.left(90)
		turtle.Screen().exitonclick()



r = Rectangle(100, 200, 0, 0)
print(r)
r.draw()

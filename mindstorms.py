import turtle
def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():	
	window=turtle.Screen()
	window.bgcolor("red")
	#create turle brad
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(3)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

#create reeses
	reeses=turtle.Turtle()
	reeses.shape("arrow")
	reeses.color("green")
	reeses.circle(100)

	window.exitonclick()





draw_art()
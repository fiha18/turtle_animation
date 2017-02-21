import turtle

window=turtle.Screen()
window.bgcolor("blue")
for i in range(8,2,-1):
	for j in range(1,10):
	
		bro=turtle.Turtle()
		bro.shape("turtle")
		bro.color("red")
		bro.circle(10*j,None,i)
window.exitonclick()

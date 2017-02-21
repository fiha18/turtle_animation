import turtle

window=turtle.Screen()
window.bgcolor("blue")
for i in range(14,3,-1):
	bro=turtle.Turtle()
	bro.shape("turtle")
	bro.color("yellow")
	bro.circle(100-5*i,None,i)
window.exitonclick()

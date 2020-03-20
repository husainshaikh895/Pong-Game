''' Pong game in python turtle'''

'''https://Github.com/HusainShaikh895'''

import turtle
import os
import time
import platform

# Take names
player_1 = input('Enter player 1 name: ')
player_2 = input('Enter player 2 name: ')


window = turtle.Screen()
window.title('Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 3


# instruction pen
spen = turtle.Turtle()
spen.speed(0)
spen.color('white')
spen.penup()
spen.hideturtle()
spen.goto(0, 0)
spen.write(f'''Welcome to PONG.\n
	This is two player game.\n {player_1} should use keys [w, s]\n and {player_2} should use keys [Up, Down] \nto move their paddles up and Down respectively.\n
	Your goal is to defend the ball from going behind you.
	Press \'p or m\' to enable or disable background music''', align='center', font=('ComicSans', 20, 'italic'))
time.sleep(7)
spen.clear()


# scoring pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'{player_1} : 0     {player_2}: 0', align='center', font=('Courier', 24, 'bold'))
score_1 = 0
score_2 = 0


# Functions
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

def play_bg():
	if platform.system() == 'Darwin':
		os.system('afplay background.mp3&')
	elif platform.system() == 'Windows':
		pass
	elif platform.system() == 'Linux':
		os.system('aplay background.mp3&')
	else:
		pass

def play_hit():
	if platform.system() == 'Darwin':
		os.system('afplay hit.mp3&')
	elif platform.system() == 'Windows':
		pass
	elif platform.system() == 'Linux':
		os.system('aplay hit.mp3&')
	else:
		pass

def stop_music():
	if platform.system() == 'Darwin':
		os.system("killall afplay")
	elif platform.system() == 'Linux':
		os.system("killall aplay")
	else:
		pass

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

play_bg()

window.onkeypress(stop_music, 'm')
window.onkeypress(play_bg, 'p')

# main loop
try:
	while(True):
		window.update()

		# Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border checking
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1
			play_hit()

		if ball.ycor() < -280:
			ball.sety(-280)
			ball.dy *= -1
			play_hit()

		if ball.xcor() > 390:
			score_1 += 1
			pen.clear()
			pen.write(f'{player_1} : {score_1}     {player_2}: {score_2}', align='center', font=('Courier', 24, 'bold'))
			ball.goto(0, 0)
			ball.dx *= -1

		if ball.xcor() < -390:
			score_2 += 1
			pen.clear()
			pen.write(f'{player_1} : {score_1}     {player_2}: {score_2}', align='center', font=('Courier', 24, 'bold'))
			ball.goto(0, 0)
			ball.dx *= -1

		# To make sure paddles stay within window
		if paddle_a.ycor() > 250:
			paddle_a.sety(250)

		if paddle_a.ycor() < -250:
			paddle_a.sety(-250)

		if paddle_b.ycor() > 250:
			paddle_b.sety(250)

		if paddle_b.ycor() < -250:
			paddle_b.sety(-250)


		# paddle and ball collision
		if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
			ball.setx(340)
			ball.dx *= -1
			ball.color('red')
			play_hit()

		if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
			ball.setx(-340)
			ball.dx *= -1
			ball.color('green')
			play_hit()
except:
	# on closing the window music should stop
	stop_music()






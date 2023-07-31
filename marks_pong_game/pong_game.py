import pygame
import turtle
import time
import tkinter as tk

def main_pong_game():

    pygame.mixer.init()

    # Load sound files
    intro_sound = pygame.mixer.Sound("sounds/cool_tetris1.wav")
    paddle_hit_sound = pygame.mixer.Sound("sounds/paddle_hit1.wav")
    goal_scored_sound = pygame.mixer.Sound("sounds/goal_hit1.wav")
    


    def setup_game_window():
        window = turtle.Screen()
        window.title("PONG by Mark")
        window.bgcolor("black")
        window.setup(width=800, height=600)
        window.tracer(0)
        return window

    def draw_text(text, position, size, color):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color(color)
        pen.penup()
        pen.hideturtle()
        pen.goto(position)
        pen.write(text, align="center", font=("Courier", size, "normal"))

    def create_paddle(x, color):
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color(color)
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(x, 0)
        return paddle

    def create_ball():
        ball = turtle.Turtle()
        ball.speed(1)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.15
        ball.dy = 0.15
        return ball

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

    def check_border_collision():
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

    def check_paddle_collision():
        if (340 > ball.xcor() > 330 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50) or \
        (-340 < ball.xcor() < -330 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.dx *= -1
            paddle_hit_sound.play()

    def check_goal():
        nonlocal score_a, score_b
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            update_score()
            goal_scored_sound.play()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            update_score()
            goal_scored_sound.play()

        if score_a == 3 or score_b == 3:
            end_game()

    def update_score():
        score_pen.clear()
        score_pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    
    # show_welcome_message()
    def show_welcome_message():

        intro_sound.play()
        draw_text("Welcome to Mark's PONG! Please, wait...", (0, 0), 24, "white")
        window.update()
        time.sleep(5)
        turtle.resetscreen()
        window.update()

    def game_over_delay():
        end_game()
        # Delay for a few seconds before closing the window
        time.sleep(5)
        # Close the turtle graphics window after the game
        turtle.bye()

        # Clean up the pygame.mixer resources
        pygame.mixer.quit()

   
    window = setup_game_window()
    show_welcome_message()
        

    def game_loop():
        
        while True:
            if score_a == 3 or score_b == 3:
                end_game()
                break
            
            try:
                
                window.update()        
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)

                check_border_collision()
                check_paddle_collision()
                check_goal()
            except tk.TclError:
                break
        
            
    def end_game():

        if score_a == 3:
            draw_text("Player A wins!", (0, 0), 24, "white")
            
                    
        elif score_b == 3:
            draw_text("Player B wins!", (0, 0), 24, "white")
            
   
        
    # Paddle A
    paddle_a = create_paddle(-350, "white")

    # Paddle B
    paddle_b = create_paddle(350, "white")

    # Ball
    ball = create_ball()

    # Score
    score_a = 0
    score_b = 0
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.goto(0, 260)
    update_score()

    window.listen()
    window.onkeypress(paddle_a_up, "w")
    window.onkeypress(paddle_a_down, "s")
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")

    game_loop()

    turtle.ontimer(game_over_delay, 100)

    turtle.mainloop()

# call the function
main_pong_game()  
import turtle
import random
import time

def show_intro_and_wait():
    screen = turtle.Screen()
    screen.setup(width=1440, height=900)
    screen.title("Game Setup")
    screen.bgcolor("black")

    intro_turtle = turtle.Turtle()
    intro_turtle.color("white")
    intro_turtle.penup()
    intro_turtle.hideturtle()
    intro_turtle.goto(0, 100)
    intro_turtle.write("Welcome to the Game!", align="center", font=("Courier", 24, "bold"))
    intro_turtle.goto(0, 0)
    intro_turtle.write("Game Rules:\n- Navigate with arrow keys & fire with the spacebar\n- Avoid enemies and allies\n- Destroy enemies to score", align="center", font=("Courier", 18, "normal"))
    intro_turtle.goto(0, -50)
    intro_turtle.write("Press Enter to start", align="center", font=("Courier", 16, "normal"))

    def initiate_game():
        global game  # Use the global keyword to access the game variable
        intro_turtle.clear()
        game = Game()
        game.start()  # Calls the start method of Game class

    screen.onkey(initiate_game, "Return")  # Use the renamed function here
    screen.listen()

class Sprite(turtle.Turtle):
    def __init__(self, color, shape, boundary_x, boundary_y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.boundary_x = boundary_x  # Dynamic horizontal boundary
        self.boundary_y = boundary_y  # Dynamic vertical boundary
        self.movement_speed = 0
        self.start_position()
        
    def start_position(self):
            self.goto(random.randint(-self.boundary_x, self.boundary_x), random.randint(-self.boundary_y, self.boundary_y))  # Set the initial position to a random location

    def move(self):
        self.forward(self.movement_speed) 
        if self.xcor() > self.boundary_x or self.xcor() < -self.boundary_x:
            self.setx(max(min(self.xcor(), self.boundary_x), -self.boundary_x))
            self.right(180)
        if self.ycor() > self.boundary_y or self.ycor() < -self.boundary_y:
            self.sety(max(min(self.ycor(), self.boundary_y), -self.boundary_y))
            self.right(180)

class Player(Sprite):
    def __init__(self, boundary_x, boundary_y):
        super().__init__("blue", "classic", boundary_x, boundary_y)
        self.goto(0, 0)
        self.movement_speed = 0
        self.shapesize(1, 2)
        self.shield = 100
        self.health = 100

    def move(self):
        super().move()

    def accelerate(self, speed_increase):
        self.movement_speed += speed_increase

    def decelerate(self, speed_decrease):
        self.movement_speed = max(0, self.movement_speed - speed_decrease)

class Rocket(Sprite):
    def __init__(self, boundary_x, boundary_y):
        super().__init__("yellow", "triangle", boundary_x, boundary_y)
        self.setheading(90)
        self.shapesize(0.25, 0.5)
        self.hideturtle()
        self.movement_speed = 5

    def move(self):
        self.forward(self.movement_speed) 
        if self.xcor() > self.boundary_x or self.xcor() < -self.boundary_x:
            self.hideturtle()
        if self.ycor() > self.boundary_y or self.ycor() < -self.boundary_y:
            self.hideturtle()

    def fire(self, player):
        if not self.isvisible():
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.showturtle()

class Enemy(Sprite):
    def __init__(self, boundary_x, boundary_y):
        super().__init__("red", "triangle", boundary_x, boundary_y)
        sizes = [(2, 1), (1.5, 1.5), (1, 2)]  # Define the possible sizes
        speeds = {(2, 1): 1, (1.5, 1.5): 2, (1, 2): 3}  # Define the speeds for each size
        self.size = random.choice(sizes)  # Assign size as an attribute of the class
        self.shapesize(*self.size)  # Apply the size
        self.movement_speed = speeds[self.size]  # Apply the speed
        self.setheading(random.randint(0, 360))
        # Store a single dimension for collision detection
        self.collision_size = max(self.size)
        self.start_position()

    def move(self):
            super().move()

class Ally(Enemy):
    def __init__(self, boundary_x, boundary_y):
        super().__init__(boundary_x, boundary_y)
        self.color("green")
        self.shape("turtle")
        self.movement_speed = random.uniform(1, 3.0)
        self.size = random.uniform(1, 3.0)
        self.shapesize(self.size)

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("yellow")
        self.penup()
        self.goto(0, 360)
        self.score = 0
        self.shape("square")
        self.shapesize(stretch_wid=0.25, stretch_len=8)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

class Shield(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("yellow")
        self.penup()
        self.goto(-200, 360)
        self.shape("square")
        self.shapesize(stretch_wid=0.25, stretch_len=8)

    def display_shield(self, shield):
        self.clear()
        self.write(f"Shield: {shield}", align="center", font=("Courier", 24, "normal"))

class Health(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("yellow")
        self.penup()
        self.goto(200, 360)
        self.shape("square")
        self.shapesize(stretch_wid=0.25, stretch_len=8)

    def display_health(self, health):
        self.clear()
        self.write(f"Health: {health}", align="center", font=("Courier", 24, "normal"))

class Game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor("black")

        screen_width = self.win.window_width()  # Get the width of the screen
        screen_height = self.win.window_height()  # Get the height of the screen
        self.win.setup(width=screen_width, height=screen_height)        
        self.game_boundary_x = screen_width // 2 - 20  # Adjust as needed
        self.game_boundary_y = screen_height // 2 - 20  # Adjust as needed

        self.player = Player(self.game_boundary_x, self.game_boundary_y)
        self.player_speed = 0

        self.rockets = [Rocket(self.game_boundary_x, self.game_boundary_y) for _ in range(2)]
        for rocket in self.rockets:
            rocket.setheading(90)
            rocket.shapesize(0.25, 0.75)
            rocket.hideturtle()

        self.sprites =  [Enemy(self.game_boundary_x, self.game_boundary_y) for _ in range(5)] + \
                        [Ally(self.game_boundary_x, self.game_boundary_y) for _ in range(10)]
        
        for sprite in self.sprites:
            sprite.start_position()
        
        self.max_speed = 3
        self.min_rocket_speed = 4
        self.rocket_delay = 0.25
        self.last_rocket_time = 0

        self.score = Score()
        self.shield = Shield()
        self.health = Health()
        self.health.display_health(self.player.health)
        self.shield.display_shield(self.player.shield)

        self.prev_score = self.score.score
        self.prev_shield = self.player.shield
        self.prev_health = self.player.health

        self.game_over = False

        self.setup_keyboard_bindings()
        self.win.tracer(0)
        pass

    def setup_keyboard_bindings(self):
        self.win.listen()
        self.win.onkeypress(self.accelerate, "Up")
        self.win.onkeypress(self.decelerate, "Down")
        self.win.onkeypress(self.turn_left, "Left")
        self.win.onkeypress(self.turn_right, "Right")
        self.win.onkeypress(self.fire_rocket, "space")
        self.win.onkeypress(self.end_game, "Escape")

    def accelerate(self):
        if self.player.movement_speed < self.max_speed:
            self.player.movement_speed += 0.25

    def decelerate(self):
        if self.player.movement_speed > 0:
            self.player.movement_speed -= 0.25

    def turn_left(self):
        self.player.left(15)

    def turn_right(self):
        self.player.right(15)

    def fire_rocket(self):
        # Check if the game is over before allowing the rocket to fire
        if not self.game_over:
            current_time = time.time()
            if current_time - self.last_rocket_time >= self.rocket_delay:
                for rocket in self.rockets:
                    if not rocket.isvisible():
                        rocket.fire(self.player)
                        self.last_rocket_time = current_time
                        break  # Only fire one rocket and then exit the loop

    def check_collisions(self):
        for sprite in self.sprites[:]:
            if self.player.distance(sprite, Enemy) < 15 + sprite.collision_size * 10:
                if isinstance(sprite, Enemy):
                    # Handle collision with enemy or ally
                    if self.player.shield > 0:
                        self.player.shield -= 20
                    else:
                        self.player.health -= 20
                    if self.check_win_lose():
                        return True
                    sprite.clear()
                    sprite.reset()
                    self.sprites.remove(sprite)
                    self.sprites.append(Enemy(self.game_boundary_x, self.game_boundary_y))
                elif isinstance(sprite, Ally):
                    # Handle collision with ally for points
                    self.score.score -= 100
                    self.score.update_score()
                    # sprite.clear()
                    # sprite.reset()
                    self.sprites.remove(sprite)
                    self.sprites.append(Ally(self.game_boundary_x, self.game_boundary_y))

        for rocket in self.rockets:
            if rocket.isvisible():
                for sprite in self.sprites[:]:
                    if rocket.distance(sprite) < 15 + sprite.collision_size * 10:
                        if isinstance(sprite, Ally):
                            # Handle rocket hitting ally
                            self.score.score -= 100
                            self.score.update_score()
                        elif isinstance(sprite, Enemy):
                            # Handle rocket hitting enemy
                            self.score.score += 100
                            self.score.update_score()
                        sprite.clear()
                        sprite.reset()
                        self.sprites.remove(sprite)
                        rocket.hideturtle()
                        if isinstance(sprite, Ally):
                            self.sprites.append(Ally(self.game_boundary_x, self.game_boundary_y))
                        elif isinstance(sprite, Enemy):
                            self.sprites.append(Enemy(self.game_boundary_x, self.game_boundary_y))

    def display_status(self):
        if self.prev_score != self.score.score:
            self.score.update_score()
            self.prev_score = self.score.score
        if self.prev_shield != self.player.shield:
            self.shield.display_shield(self.player.shield)
            self.prev_shield = self.player.shield
        if self.prev_health != self.player.health:
            self.health.display_health(self.player.health)
            self.prev_health = self.player.health

    def start(self):
        self.game_loop()
        pass

    def check_win_lose(self):
        win_lose_turtle = turtle.Turtle()
        win_lose_turtle.hideturtle()
        win_lose_turtle.color("white")

        if self.player.health <= 0 and self.player.shield <= 0:
            win_lose_turtle.write("You lose!", align="center", font=("Courier", 24, "normal"))
            self.player.hideturtle()
            self.game_over = True
        elif self.score.score >= 1000 and not self.game_over:
            win_lose_turtle.write("You win!", align="center", font=("Courier", 24, "normal"))
            self.player.hideturtle()
            self.game_over = True
        return self.game_over

    def end_game(self):
        self.game_over = True
        # self.close_game() I have added this to close the game without a game over message if needed
        # Disable all key bindings except for the "Escape" key
        self.win.onkeypress(None, "Up")
        self.win.onkeypress(None, "Down")
        self.win.onkeypress(None, "Left")
        self.win.onkeypress(None, "Right")
        self.win.onkeypress(None, "space")
        # Keep "Escape" key binding to allow closing the game
        self.win.onkeypress(self.close_game, "Escape")
        # Additional logic to handle game over state (e.g., displaying a message) can be added here

    def close_game(self):
        self.win.bye()

    def game_loop(self):
        frame_rate = 60
        frame_period = 1 / frame_rate
        while True:
            start_time = time.time()

            if not self.game_over:
                self.display_status()
                # self.player.movement_speed = self.player_speed
                self.player.move()

                for sprite in self.sprites:
                    sprite.move()

                for rocket in self.rockets:
                    if rocket.isvisible():
                        rocket_speed = max(self.player_speed * 2, self.min_rocket_speed)
                        # rocket.movement_speed = rocket_speed
                        rocket.move()

                self.check_collisions()
                self.check_win_lose()

            self.win.update()

            elapsed_time = time.time() - start_time
            if elapsed_time < frame_period:
                time.sleep(frame_period - elapsed_time)

if __name__ == "__main__":
    show_intro_and_wait()
    turtle.mainloop()

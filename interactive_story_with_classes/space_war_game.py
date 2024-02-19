import turtle
import random
import time
# import logging

# logging.basicConfig(level=logging.DEBUG)

class Sprite(turtle.Turtle):
    def __init__(self, color, shape, startx, starty):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.setposition(startx, starty)

    def move(self, speed):
        self.forward(speed)
        if self.xcor() > 300 or self.xcor() < -300:
            self.right(180)
        if self.ycor() > 300 or self.ycor() < -300:
            self.right(180)

class Player(Sprite):
    def __init__(self):
        super().__init__("blue", "triangle", 0, 0)  # Initialize the player with color, shape, and starting position
        self.speed = 0  # Initialize player's speed to 0
        self.shield = 100  # Initialize player's shield to 100
        self.health = 100  # Initialize player's health to 100
        self.direction = "stop"  # Initialize player's direction to "stop"

    def move(self):
        # Move the player based on the current direction
        if self.direction == "up":
            self.sety(self.ycor() + self.speed)
        elif self.direction == "down":
            self.sety(self.ycor() - self.speed)
        elif self.direction == "left":
            self.setx(self.xcor() - self.speed)
        elif self.direction == "right":
            self.setx(self.xcor() + self.speed)

        # Boundary checking to prevent the player from moving out of the window
        if self.xcor() > 290 or self.xcor() < -290:
            self.setx(max(min(self.xcor(), 290), -290))
        if self.ycor() > 290 or self.ycor() < -290:
            self.sety(max(min(self.ycor(), 290), -290))

    def change_direction(self, direction):
        self.direction = direction  # Update the player's direction based on user input

    def accelerate(self, speed_increase):
        self.speed += speed_increase  # Increase the player's speed

    def decelerate(self, speed_decrease):
        self.speed = max(0, self.speed - speed_decrease)  # Decrease the player's speed, ensuring it doesn't go below 0

class Rocket(Sprite):
    def __init__(self, startx, starty):
        super().__init__("yellow", "triangle", startx, starty)
        self.setheading(90)  # Rockets face upwards initially
        self.shapesize(0.25, 0.5)  # Adjusting the rocket size
        self.hideturtle()  # Rockets are hidden until fired
        self.speed = 5  # Set a standard speed for rockets

    def move(self):
        super().move(self.speed)  # Use the inherited move method with the rocket's speed
        # Automatically hide the rocket if it moves out of bounds
        if not (-300 < self.xcor() < 300 and -300 < self.ycor() < 300):
            self.hideturtle()

    def fire(self, player):
        if not self.isvisible():
            self.goto(player.xcor(), player.ycor())  # Move to the player's position
            self.setheading(player.heading())  # Match the player's heading
            self.showturtle()  # Make the rocket visible and start moving

class Enemy(Sprite):
    def __init__(self, startx, starty):
        super().__init__("red", "circle", startx, starty)  # Initialize with the base Sprite setup
        self.size = random.uniform(0.5, 2.0)  # Randomize the size of the enemy for variety
        self.shapesize(self.size)  # Apply the size to the shape
        self.speed = min(random.uniform(1, 2) / self.size, 5)  # Calculate speed based on size
        self.setheading(random.randint(0, 360))  # Set a random heading for movement

    def move(self, speed=None):
        if speed is not None:
            self.speed = speed  # Allow dynamic speed adjustment
        super().move(self.speed)  # Use the inherited move method
        # Check for boundary collision to bounce back at an angle
        if self.xcor() > 290 or self.xcor() < -290:
            self.right(60)  # Bounce back at 60 degrees when hitting the side boundaries
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)  # Bounce back at 60 degrees when hitting the top or bottom boundaries

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("green")
        self.penup()
        self.goto(0, 360)
        self.score = 0
        self.shape("square")  # Change the shape to a square
        self.shapesize(stretch_wid=0.25, stretch_len=8)  # Stretch the width to 0.5 and the length to 5
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

class Shield(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("green")
        self.penup()
        self.goto(-200, 360)
        self.shape("square")  # Change the shape to a square
        self.shapesize(stretch_wid=0.25, stretch_len=8)  # Stretch the width to 0.5 and the length to 5

    def display_shield(self, shield):
        self.clear()
        self.write(f"Shield: {shield}", align="center", font=("Courier", 24, "normal"))

class Health(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("green")
        self.penup()
        self.goto(200, 360)
        self.shape("square")  # Change the shape to a square
        self.shapesize(stretch_wid=0.25, stretch_len=8)  # Stretch the width to 0.5 and the length to 5

    def display_health(self, health):
        self.clear()
        self.write(f"Health: {health}", align="center", font=("Courier", 24, "normal"))

class Game:
    def __init__(self):
        self.win = turtle.Screen()  # Create the game window
        self.win.bgcolor("black")  # Set the background color of the window
        self.player = Player()  # Initialize the player
        self.player_speed = 0  # Initialize player speed to 0

        # Initialize rockets, setting their heading, size, and hiding them initially
        self.rockets = [Rocket(0, 0) for _ in range(2)]
        for rocket in self.rockets:
            rocket.setheading(90)  # Rockets face upwards
            rocket.shapesize(0.25, 0.5)  # Adjust rocket appearance
            rocket.hideturtle()  # Rockets are hidden until fired

        # Initialize enemies at random positions
        self.enemies = [Enemy(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(5)]

        self.max_speed = 3  # Set the maximum speed for the player
        self.min_rocket_speed = 4  # Set the minimum speed for rockets
        self.rocket_delay = 0.25  # Set the delay between rocket fires
        self.last_rocket_time = 0  # Track the last time a rocket was fired

        # Initialize UI components for displaying score, shield, and health
        self.score = Score()
        self.shield = Shield()
        self.health = Health()
        # Display the initial health and shield values
        self.health.display_health(self.player.health)
        self.shield.display_shield(self.player.shield)

        # Variables to track changes in score, shield, and health for efficient UI updates
        self.prev_score = self.score.score
        self.prev_shield = self.player.shield
        self.prev_health = self.player.health

        self.game_over = False  # Flag to control the game loop

        self.setup_keyboard_bindings()  # Set up keyboard bindings for player control

        self.win.tracer(0)  # Disable automatic screen updates for performance

    def setup_keyboard_bindings(self):
        # Listen for keyboard events
        self.win.listen()

        # Bind the arrow keys and spacebar to player actions
        self.win.onkeypress(self.accelerate, "Up")
        self.win.onkeypress(self.decelerate, "Down")
        self.win.onkeypress(self.turn_left, "Left")
        self.win.onkeypress(self.turn_right, "Right")
        self.win.onkeypress(self.fire_rocket, "space")
        self.win.onkeypress(self.end_game, "Escape")  # Assuming you want a quick way to quit the game

    def accelerate(self):
        # Increase the player's speed, up to a maximum
        if self.player_speed < self.max_speed:
            self.player_speed += 0.25

    def decelerate(self):
        # Decrease the player's speed, not going below 0
        if self.player_speed > 0:
            self.player_speed -= 0.25

    def turn_left(self):
        # Turn the player left (counter-clockwise)
        self.player.left(15)

    def turn_right(self):
        # Turn the player right (clockwise)
        self.player.right(15)

    def fire_rocket(self):
        # Fire a rocket if the cooldown period has passed
        current_time = time.time()
        if current_time - self.last_rocket_time >= self.rocket_delay:
            for rocket in self.rockets:
                if not rocket.isvisible():
                    rocket.fire(self.player)
                    self.last_rocket_time = current_time
                    break  # Stop searching after firing a rocket
    
    def check_collisions(self):
        for enemy in self.enemies[:]:
            if self.player.distance(enemy) < 15 + enemy.size * 10:  # player collision with enemy
                if self.player.shield > 0:
                    self.player.shield -= 20
                else:
                    self.player.health -= 20
                if self.check_win_lose():  # Check if the game should end
                    return True
                enemy.hideturtle()
                self.enemies.remove(enemy)
                # spawn a new enemy
                self.enemies.append(Enemy(random.randint(-300, 300), random.randint(-300, 300)))
                break

        for rocket in self.rockets:
            if rocket.isvisible():
                for enemy in self.enemies[:]:
                    if rocket.distance(enemy) < 15 + enemy.size * 10:  # rocket collision with enemy
                        self.score.score += 100
                        self.score.update_score()
                        enemy.hideturtle()
                        self.enemies.remove(enemy)
                        rocket.hideturtle()
                        # spawn a new enemy
                        self.enemies.append(Enemy(random.randint(-300, 300), random.randint(-300, 300)))
                        break

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

    def check_win_lose(self):
        win_lose_turtle = turtle.Turtle()
        win_lose_turtle.hideturtle()
        win_lose_turtle.color("white")

        if self.player.health <= 0 and self.player.shield <= 0:
            win_lose_turtle.write("You lose!", align="center", font=("Courier", 24, "normal"))
            self.player.hideturtle()  # Hide the player's turtle
            self.game_over = True  # Set the game over flag
        elif self.score.score >= 1000 and not self.game_over:
            win_lose_turtle.write("You win!", align="center", font=("Courier", 24, "normal"))
            self.player.hideturtle()  # Hide the player's turtle
            self.game_over = True  # Set the game over flag
        return self.game_over  # Return the game over flag
    
    def fire_rocket_if_game_not_over(self):
        if not self.game_over:  # Only allow the player to fire rockets if the game is not over
            current_time = time.time()
            if current_time - self.last_rocket_time > self.rocket_delay:
                self.last_rocket_time = current_time
                for rocket in self.rockets:
                    if not rocket.isvisible():
                        rocket.fire(self.player)
                        break

    def end_game(self):
        self.game_over = True
        self.win.bye()  # Close the game window
    
def main():
    game = Game()
    game.start()

def game_loop(game):
    frame_rate = 60
    frame_period = 1 / frame_rate
    while not game.game_over:  # Use the game_over flag to control the loop
        start_time = time.time()

        # Update game status displays
        game.display_status()

        # Move the player based on current speed and direction
        game.player.move(game.player_speed)

        # Update enemy positions
        for enemy in game.enemies:
            enemy.move(enemy.speed)

        # Update rocket positions and check visibility
        for rocket in game.rockets:
            if rocket.isvisible():
                # Calculate rocket speed based on player speed and minimum rocket speed
                rocket_speed = max(game.player_speed * 1.5, game.min_rocket_speed)
                rocket.move(rocket_speed)

        # Check for collisions and win/lose conditions
        if game.check_collisions() or game.check_win_lose():
            break  # Exit the loop if the game is over

        # Update the screen with the latest game state
        game.win.update()

        # Calculate elapsed time and adjust to maintain the desired frame rate
        elapsed_time = time.time() - start_time
        if elapsed_time < frame_period:
            time.sleep(frame_period - elapsed_time)


if __name__ == "__main__":
    main()
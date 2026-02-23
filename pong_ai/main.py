import pygame
from sprites import Paddle, Ball

# Initialize the game engine
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong AI")

paddleA = Paddle(WHITE, 10, 100, is_ai=False)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100, is_ai=True)
paddleB.rect.x = 670
paddleB.rect.y = 200

paddleB.speed = 4 # slightly slower than human so it is beatable

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

# -------- Start Screen -----------
start_screen = True
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_screen = False

    screen.fill(BLACK)
    title_text = font_large.render("PONG AI", True, WHITE)
    controls_text = font_small.render("Controls: 'W' for Up, 'S' for Down", True, WHITE)
    start_text = font_small.render("Press SPACE to Start. First to 10 wins!", True, WHITE)
    
    screen.blit(title_text, title_text.get_rect(center=(350, 150)))
    screen.blit(controls_text, controls_text.get_rect(center=(350, 250)))
    screen.blit(start_text, start_text.get_rect(center=(350, 350)))
    
    pygame.display.flip()
    clock.tick(60)

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x: # Pressing the x Key will quit the game
                     carryOn = False

    # Moving the paddles when the user uses the arrow keys (Player A) or "W/S" keys (Player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5, 500)
    
    # Update the AI paddle
    paddleB.update_ai(ball, 500)

    # --- Game logic should go here
    all_sprites_list.update()
    
    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 345
        ball.rect.y = 195
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 345
        ball.rect.y = 195
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1] 

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_rect(ball, paddleA):
        ball.rect.left = paddleA.rect.right
        ball.bounce()
    elif pygame.sprite.collide_rect(ball, paddleB):
        ball.rect.right = paddleB.rect.left
        ball.bounce()

    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 

    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    # Check Win Condition
    if scoreA >= 10 or scoreB >= 10:
        win_text = "YOU WIN!" if scoreA >= 10 else "AI WINS!"
        font_large = pygame.font.Font(None, 100)
        text_surface = font_large.render(win_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(350, 250))
        screen.blit(text_surface, text_rect)
        pygame.display.flip() # Force one last draw
        pygame.time.wait(3000) # Wait 3 seconds to read the message
        carryOn = False

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

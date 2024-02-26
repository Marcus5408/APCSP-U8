import pygame
from datetime import datetime

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('HYWenHei-85W', 24)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)

person = {
    "name": "Issac Liu",
    "slogan": "I don't care",
    "date": datetime.now().strftime("%m/%d/%Y")
}

# render the text for later
display_name = my_font.render(person['name'], True, (255, 255, 255))
display_slogan = my_font.render(f"Slogan: {person['slogan']}", True, (255, 255, 255))
display_date = my_font.render(f"Date: {person['date']}", True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((38, 35, 53))
    screen.blit(display_name, (0, 0))
    screen.blit(display_slogan, ((size[0]//2) - 125, (size[1]//2) - 30))
    screen.blit(display_date, (size[0] - 225, size[1] - 30))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
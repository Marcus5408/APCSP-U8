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
    "slogan": "yippee !!!",
    "date": datetime.now().strftime("%m/%d/%Y")
}

colors = {
    "0": {
        "text": (0, 0, 0),
        "background": (137, 210, 220)
    },
    "1": {
        "text": (0, 0, 0),
        "background": (101, 100, 219)
    },
    "2": {
        "text": (255, 255, 255),
        "background": (35, 46, 209)
    },
    "3": {
        "text": (255, 255, 255),
        "background": (16, 29, 66)
    },
    "4": {
        "text": (255, 255, 255),
        "background": (13, 19, 23)
    }
}

def render_text(person: dict):
    # render the text for later
    mod_time = str(int(datetime.now().strftime("%S")) // 2 % 5)
    display_name = my_font.render(person['name'], True, colors[mod_time]['text'])
    display_slogan = my_font.render(f"Slogan: {person['slogan']}", True, colors[mod_time]['text'])
    display_date = my_font.render(f"Date: {person['date']}", True, colors[mod_time]['text'])

    return display_name, display_slogan, display_date

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
time_started = datetime.now()

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill(colors[str(int(datetime.now().strftime("%S")) // 2 % 5)]["background"])
    display_name, display_slogan, display_date = render_text(person)
    time_elapsed = datetime.now() - time_started
    time_elapsed = time_elapsed.total_seconds()
    time_elapsed = round(time_elapsed, 3)
    time_elapsed = f"{time_elapsed} seconds"
    display_time_elapsed = my_font.render(f"Time Elapsed: {time_elapsed}", True, colors[str(int(datetime.now().strftime("%S")) // 2 % 5)]["text"])
    screen.blit(display_time_elapsed, (0, size[1] - 30))
    screen.blit(display_name, (0, 0))
    screen.blit(display_slogan, ((size[0]//2) - 100, (size[1]//2) - 30))
    screen.blit(display_date, (size[0] - 225, size[1] - 30))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
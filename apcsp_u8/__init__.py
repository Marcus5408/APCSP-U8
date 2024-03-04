from random import randint
import pygame
from datetime import datetime

fonts = {
    "HYWenHei-85W": "fonts/zhcn.ttf",
    "Arial": "fonts/arial.ttf",
    "Comic Sans MS": "fonts/comic.ttf",
    "Dubai Regular": "fonts/DUBAI-REGULAR.TTF",
    "JetBrainsMono NF": "fonts/JetBrainsMonoNerdFont-Regular.ttf",
    "Segoe UI": "fonts/segoeui.ttf",
    "Papyrus": "fonts/PAPYRUS.TTF",
    "SF Compact Regular": "fonts/SF-Compact-Display-Regular.otf",
    "SpaceMono Nerd Font": "fonts/SpaceMonoNerdFont-Regular.ttf",
    "Verdana": "fonts/verdana.ttf",
    "Calibri": "fonts/calibri.ttf",
    "Century Gothic": "fonts/GOTHIC.TTF"
}

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.Font(fonts['HYWenHei-85W'], 24)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)

person = {
    "name": "Issac Liu",
    "message": "yippee !!!",
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

def render_text(person: dict, color: tuple = (None, None, None)) -> tuple:
    # render the text for later
    if color == (None, None, None):
        color = colors[str(int(datetime.now().strftime("%S")) // 2 % 5)]['text']
    else:
        color = color
    display_name = my_font.render(person['name'], True, color)
    display_message = my_font.render(f"{person['message']}", True, color)
    display_date = my_font.render(f"Date: {person['date']}", True, color)

    return display_name, display_message, display_date

def generate_color() -> tuple:
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def generate_color_text(r:int, g:int, b:int) -> str:
    return f"RGB value = ( {r}, {g}, {b} )"

anarchy_chess = [
    "google en passant",
    "holy hell",
    "new response just dropped",
    "actual zombie",
    "call the exorcist!",
    "???",
    "bishop goes on vacation, never comes back",
    "Queen sacrifice anyone?",
    "pawn storm incoming!",
    "google dementia"
]

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
time_started = datetime.now()

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        match event.type:
            case pygame.QUIT:
                run = False
            case pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    person["message"] = anarchy_chess[randint(0, len(anarchy_chess) - 1)]
                elif event.button == 3:
                    my_font = pygame.font.Font(fonts[list(fonts.keys())[randint(0, len(fonts) - 1)]], 24)
                    render_text(person, tuple(generate_color()))

    screen.fill(colors[str(int(datetime.now().strftime("%S")) // 2 % 5)]["background"])

    time_elapsed = datetime.now() - time_started
    time_elapsed = time_elapsed.total_seconds()
    time_elapsed = round(time_elapsed, 3)
    time_elapsed = f"{time_elapsed} seconds"
    display_time_elapsed = my_font.render(f"Time Elapsed: {time_elapsed}", True, colors[str(int(datetime.now().strftime("%S")) // 2 % 5)]["text"])
    screen.blit(display_time_elapsed, (0, size[1] - 30))

    display_name, display_message, display_date = render_text(person)
    screen.blit(display_name, (0, 0))
    text_width, text_height = display_message.get_size()
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2
    screen.blit(display_message, (text_x, text_y))
    screen.blit(display_date, (size[0] - 225, size[1] - 30))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
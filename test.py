
import pyretro_gui as rg
from pyretro_gui import app_state, close_app, MenuBar, MenuItem, DropDown, Container

from constants import SCREEN_X_POS, SCREEN_Y_POS

import pygame
rg.create_window(640, 480, "copy - untitled_image.png", "testicon2.png", flags = pygame.RESIZABLE)
# rg.create_window(640, 480, "copy - untitled_image.png", "testicon2.png", flags = 0)

surf = pygame.Surface((50, 50))
surf.fill([255] * 3)
img = pygame.image.load("evangelion.jpg").convert()
app_state.widgets.append(
        Container(SCREEN_X_POS, SCREEN_Y_POS, 600, 400, img)
        )

app_state.widgets.append(MenuBar([
    MenuItem("File", 0, DropDown([
        MenuItem("Open", 0, DropDown([
            MenuItem("image 1"), 
            MenuItem("image 2"), 
            MenuItem("Nested", dropdown = DropDown([
                MenuItem("Option 1"), 
                MenuItem("Option 2"),
                MenuItem("Nested deep", dropdown = DropDown([
                    MenuItem("Option 3"), 
                    MenuItem("Option 4")
                ], width = 100))
            ]))
        ])), 
        MenuItem("Close", 0, shortcut = "Alt+F4", onclick = close_app)
    ]) ),
    MenuItem("Edit", 0, None),
    MenuItem("View", 1, None)
    ]))


while rg.app_state.running:
    rg.window_update()
    rg.window_render()


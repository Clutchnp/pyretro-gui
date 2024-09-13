
import pygame

from app_core import app_state
from constants import Colors, UI_FPS

class DropDown:
    X_OFF = 2
    DROPDOWN_PAD = 4
    TEXT_X_OFF = 16
    TOGGLE_DELAY = UI_FPS / 2

    def __init__ (self, items: list = [], width: int = 150):
        self.items = items

        self.width = width
        self.rect = None
        self.focused = False
        self.opened = False

        self.toggle_timer = 0
    
    def toggle (self):
        if (self.toggle_timer > 0): return
        self.opened = not self.opened
        self.toggle_timer = self.TOGGLE_DELAY

    def update (self, mouse_pos, mouse_btns):
        if self.toggle_timer > 0:
            self.toggle_timer -= 1 * app_state.get_dt()

        self.focused = self.rect and self.rect.collidepoint(mouse_pos)

        if not self.focused and mouse_btns[0] and self.toggle_timer <= 0:
            self.opened = False

        for it in self.items:
            it.update(mouse_pos, mouse_btns)

    def render (self, win, rect):
        y_offset = rect.h + self.DROPDOWN_PAD
        self.rect = pygame.Rect(rect.x - self.X_OFF, rect.y + y_offset - self.DROPDOWN_PAD, self.width, 1)

        for it in self.items:
            r = pygame.Rect(rect.x, rect.y + y_offset, self.width - 4, 0)
            y_offset += it.render(win, [rect.x + self.TEXT_X_OFF, rect.y + y_offset], custom_rect = r)[1] + self.DROPDOWN_PAD

        self.rect.h = y_offset - self.DROPDOWN_PAD * 3
        pygame.draw.rect(win, Colors.TEXT, self.rect, 1)
        # pygame.draw.rect(win, Colors.TEXT, [self.rect.x + 1, self.rect.y + 1, self.rect.w - 2, self.rect.h - 2], 1)
        pygame.draw.rect(win, Colors.DARK_SHADOW, [self.rect.x, self.rect.y, self.rect.w - 1, self.rect.h - 1], 1)

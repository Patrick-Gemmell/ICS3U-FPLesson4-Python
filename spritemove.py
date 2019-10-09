#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: October 2019
# This program moves sprites on pybadge

import ugame
import stage

image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
sprites = []


def main():
    background = stage.Grid(image_bank_1, 10, 8)

    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 74, 56)
    sprites.insert(0, ship)

    game = stage.Stage(ugame.display, 60)
    game.layers = sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            pass
        elif keys & ugame.K_O:
            pass
        elif keys & ugame.K_START:
            pass
        elif keys & ugame.K_SELECT:
            pass
        elif keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        elif keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            pass
        elif keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            pass
        elif keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()

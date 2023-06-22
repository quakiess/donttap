from time import *
import pyautogui as mouse
from pynput.keyboard import Listener
import sys

amount_of_moves = 0
amount_of_horizontal_moves = 1
running = False
started = True


def move_mouse():
    # global: is needed to change a global variable inside a function
    global amount_of_moves
    global amount_of_horizontal_moves
    # distance between row where tiles appear
    row_distance = 180
    column_distance = 180
    amount_of_moves += 1
    if amount_of_moves % 5 == 0 and amount_of_moves != 0:
        mouse.move(-row_distance * 3, column_distance)
        amount_of_horizontal_moves += 1
    else:
        mouse.move(row_distance, 0)
    if amount_of_horizontal_moves % 5 == 0:
        mouse.move(0, -4 * column_distance)
        amount_of_horizontal_moves += 1


def on_press(key):
    global amount_of_moves
    global amount_of_horizontal_moves
    global running
    if "{0}".format(key) == 'Key.esc':
        running = False
        print("Exiting...")
        sys.exit()
    if "{0}".format(key) == 'Key.f2':
        running = not running
        if running:
            amount_of_moves = 1
            amount_of_horizontal_moves = 1


def main():
    listener = Listener(on_press=on_press)
    listener.start()
    while started:
        while running:
            sleep(0.1)
            pos_X = mouse.position().x
            pos_Y = mouse.position().y
            pixel = mouse.pixel(pos_X, pos_Y)
            # print(pixel)
            if pixel[0] == 0 & pixel[1] == 0 & pixel[2] == 0:
                # print("tile detected")
                mouse.click()
            else:
                # print("not a tile")
                move_mouse()


if __name__ == "__main__":
    main()

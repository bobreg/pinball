import window
import GameTetris
import GameSource
import AgainstAnother

change_tetris_level = 0
change_tetris_speed = 0

change_w = 0
change_h = 0


def game0():
    window_new_game.new_game.destroy()  # перед запуском основного игрового окна закроем окно выбора игры чтобы не мешало
    GameSource.game1()


def game1():
    window_new_game.new_game.destroy()
    GameTetris.start(change_tetris_level+1, change_tetris_speed, window_new_game.choice_platform.get())


def game2():
    window_new_game.new_game.destroy()
    AgainstAnother.start(change_w + 40, change_h + 20)


def game1_change_level_plus():
    global change_tetris_level
    change_tetris_level = (change_tetris_level + 1) % 8
    window_new_game.label_level_value['text'] = str(change_tetris_level+1)


def game1_change_level_minus():
    global change_tetris_level
    change_tetris_level = (change_tetris_level - 1) % 8
    window_new_game.label_level_value['text'] = str(change_tetris_level+1)


def game1_change_speed_plus():
    global change_tetris_speed
    change_tetris_speed = (change_tetris_speed + 1) % 7
    window_new_game.label_speed_value['text'] = str(change_tetris_speed+1)


def game1_change_speed_minus():
    global change_tetris_speed
    change_tetris_speed = (change_tetris_speed - 1) % 7
    window_new_game.label_speed_value['text'] = str(change_tetris_speed+1)


def game2_change_width_window_plus():
    global change_w
    change_w = (change_w + 1) % 41
    window_new_game.label_width_value['text'] = str(change_w + 40)


def game2_change_width_window_minus():
    global change_w
    change_w = (change_w - 1) % 41
    window_new_game.label_width_value['text'] = str(change_w + 40)


def game2_change_height_window_plus():
    global change_h
    change_h = (change_h+ 1) % 21
    window_new_game.label_height_value['text'] = str(change_h + 20)


def game2_change_height_window_minus():
    global change_h
    change_h = (change_h - 1) % 21
    window_new_game.label_height_value['text'] = str(change_h + 20)


# -------------создадим окно выбора игры-------------

window_new_game = window.WindowNewGame()
window_new_game.button1['command'] = game1
window_new_game.button2['command'] = game2
window_new_game.button3['command'] = game0
window_new_game.button1_plus['command'] = game1_change_level_plus
window_new_game.button1_minus['command'] = game1_change_level_minus
window_new_game.button2_plus['command'] = game1_change_speed_plus
window_new_game.button2_minus['command'] = game1_change_speed_minus
window_new_game.button3_plus['command'] = game2_change_width_window_plus
window_new_game.button3_minus['command'] = game2_change_width_window_minus
window_new_game.button4_plus['command'] = game2_change_height_window_plus
window_new_game.button4_minus['command'] = game2_change_height_window_minus
window_new_game.start()

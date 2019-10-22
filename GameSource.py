import window
import threading
import time
import keyboard
import random

# параметры поля и игры
height_pole = 0
width_pole = 0
speed_ball = 0.08   # 0.08
speed_polygon = 0.05
type_polygon = 'y'
type_game = 2
level_polygon = -1
# системные параметры
flag_game_restart = False
napravlenie_x = -1
napravlenie_y = 1
count_right = 0
count_left = 0


def drive_ball():
    print('start')
    global x, y
    global napravlenie_x, napravlenie_y
    global count_left, count_right
    global flag_left_up, flag_right_down, flag_game_restart
    global c
    while True:  # пошлём в window координаты положения мячика и затрём его положение
        if flag_game_restart is not True:
            window_game.labels[y][x]['bg'] = 'gray40'
            x += napravlenie_x  # изменим координаты и сделаем проверки
            y += napravlenie_y
    # ----меняем координату х--------
            if x >= width_pole-1:
                x = width_pole - 1
                napravlenie_x = -1
            elif x <= 0:
                x = 0
                napravlenie_x = 1
    # ----меняем координату у--------
            if y >= height_pole-1:
                y = height_pole - 1
                napravlenie_y = -1
            elif y <= 0:
                y = 0
                napravlenie_y = 1
    # ---------отрисуем новое положение мячика---------------
            window_game.labels[y][x]['bg'] = 'red'
            time.sleep(speed_ball)
    # ---------отскок----------------
            otskok()  # для оптимизации проверку отскока от площадки проводим когда мячик будет внизу поля


def otskok():
    global x, y
    global napravlenie_x, napravlenie_y
    global count_left, count_right
    global flag_left_up, flag_right_down, flag_game_restart
    if type_polygon == 'y':  # отскок от вертикальной платформы
        if window_game.labels[y][x + napravlenie_x]['bg'] == 'white':
            napravlenie_x *= -1
            count_left += 1
            window_game.label1['text'] = str(count_left)
        elif window_game.labels[y + napravlenie_y][x + napravlenie_x]['bg'] == 'white':
            napravlenie_x *= -1
            napravlenie_y *= -1
            count_left += 1
            window_game.label1['text'] = str(count_left)
        elif x == 0:
            print('Проиграл!')
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = int(height_pole / 2)
            napravlenie_x = random.choice([-1, 1])
            napravlenie_y = random.choice([-1, 1])
    else:  # отскок от горизонтальной платформы
        if window_game.labels[y + napravlenie_y][x]['bg'] == 'white':
            napravlenie_y *= -1
            count_left += 1
        elif window_game.labels[y + napravlenie_y][x + napravlenie_x]['bg'] == 'white': # ??? иногда выпадает ошибка
            napravlenie_x *= -1
            napravlenie_y *= -1
        elif y == height_pole-1:  # last_y
            print('Проиграл!')
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = int(height_pole / 2)
            napravlenie_x = random.choice([-1, 1])
            napravlenie_y = random.choice([-1, 1])


def drive_polygon_y():
    while True:
        if keyboard.is_pressed('up') is True:
            window_game.up_polygon()
        if keyboard.is_pressed('down') is True:
            window_game.down_polygon()
        time.sleep(speed_polygon)
        # а можно так, но будет не очень
        # keyboard.add_hotkey('up', window_game.up_polygon)
        # keyboard.add_hotkey('down', window_game.down_polygon)
        # keyboard.wait()


def drive_polygon_x():
    global height_pole, x, napravlenie_x
    while True:
        if keyboard.is_pressed('left') is True and window_game.polygon[0] != 0:
            window_game.shift_left_polygon()
            if y > height_pole - 3 and window_game.labels[height_pole-1][x]['bg'] == 'white':
                if x != 0:
                    window_game.labels[y][x]['bg'] = 'gray40'
                    napravlenie_x = -1
                    x -= 1
                    window_game.labels[y][x]['bg'] = 'red'
        if keyboard.is_pressed('right') is True and window_game.polygon[-1] != width_pole-1:
            window_game.shift_right_polygon()
            if y > height_pole - 3 and window_game.labels[height_pole-1][x]['bg'] == 'white':
                if x < width_pole - 2:
                    window_game.labels[y][x]['bg'] = 'gray40'
                    napravlenie_x = 1
                    x += 1
                    window_game.labels[y][x]['bg'] = 'red'
        time.sleep(speed_polygon)


def pause():
    global c
    window_game.labels[y][x]['bg'] = 'red'
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed('space') is True:
            c.start()
            break


def game1():
    global window_game
    global x, y
    global c
    global napravlenie_x, napravlenie_y
    global height_pole, width_pole
    global type_polygon
    global type_game

    # -------------параметры поля и игры-------------

    height_pole = 40
    width_pole = 20
    width_polygon = 8
    type_polygon = ' x'
    type_game = ''

    # -------------системные параметры-------------

    x = int(width_pole / 2)
    y = int(height_pole / 2)
    napravlenie_x = random.choice([-1, 1])
    napravlenie_y = random.choice([-1, 1])

    # -------------создадим игровое окно-------------

    if type_game == 1:
        window_game = window.Framuga(type_polygon,
                                     width_polygon,
                                     width_pole,
                                     height_pole,
                                     level_polygon)  # объявим элементы окна
        window_game.figure()  # вызовем метод рисования фигуры для одинчного режима тетрис
    else:
        window_game = window.FramugaTwoPolygons(type_polygon,
                                     width_polygon,
                                     width_pole,
                                     height_pole,
                                     level_polygon)  # объявим элементы окна

    # -------------создадим пару потоков для движения мячика и движения платформы-------------

    c = threading.Thread(target=drive_ball)  # объявим поток движения мячика
    if type_polygon == 'y':  # в зависимости от типа игры объявим поток с горизонтальной или вертикальной платформой
        wait_key = threading.Thread(target=drive_polygon_y)
    else:
        wait_key = threading.Thread(target=drive_polygon_x)
    ready_game_spase = threading.Thread(target=pause)

    # -------------запустим все потоки-------------

    # c.start()  # запустим поток движения мячика
    ready_game_spase.start()
    wait_key.start()  # запустим поток движения платформы
    window_game.bild_window()


if __name__ == '__main__':
    game1()
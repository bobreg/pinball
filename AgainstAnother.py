import window
import threading
import time
import keyboard
import random

# параметры поля и игры
height_pole = 0
width_pole = 0
speed_ball = 0.04   # 0.08
speed_polygon = 0.05
type_polygon = 'y'
type_game = ''
# системные параметры
flag_game_restart = False
napravlenie_x = -1
napravlenie_y = 1
count_right = 0
count_left = 0
health_left = 5
health_right = 5
level_polygon_left = 0
level_polygon_right = 0


def drive_ball():
    print('start')
    global x, y
    global napravlenie_x, napravlenie_y
    global count_left, count_right
    global flag_game_restart
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
        else:
            flag_game_restart = False
            c = threading.Thread(target=drive_ball)
            pause()
            break


def otskok():
    global x, y
    global napravlenie_x, napravlenie_y
    global count_left, count_right
    global flag_game_restart
    global health_left, health_right
    global level_polygon_left, level_polygon_right
    if type_polygon == 'y':  # отскок от вертикальной платформы
        if window_game.labels[y][x + napravlenie_x]['bg'] == 'white':
            napravlenie_x *= -1
            if x < int(width_pole / 2):
                count_left += 1
                window_game.label1['text'] = str(count_left)
            else:
                count_right += 1
                window_game.label2['text'] = str(count_right)
        elif window_game.labels[y + napravlenie_y][x + napravlenie_x]['bg'] == 'white':
            napravlenie_x *= -1
            napravlenie_y *= -1
            if y < int(width_pole / 2):
                count_left += 1
                window_game.label1['text'] = str(count_left)
            else:
                count_right += 1
                window_game.label2['text'] = str(count_right)
        elif x == 0 or x == width_pole-1:
            print('Проиграл!')
            flag_game_restart = True
            if x < int(width_pole / 2):
                health_left -= 1
                if health_left == -1:
                    health_left = 5
                    for i in window_game.polygon_right_down:
                        window_game.labels[i][level_polygon_right]['bg'] = 'gray40'
                    if level_polygon_right > -int(width_pole / 2) + 3:
                        level_polygon_right -= 1
                    else:
                        level_polygon_right = -1
                    for i in window_game.polygon_right_down:
                        window_game.labels[i][level_polygon_right]['bg'] = 'white'
                    window_game.level_polygon_right = level_polygon_right
            else:
                health_right -= 1
                if health_right == -1:
                    health_right = 5
                    for i in window_game.polygon_left_up:
                        window_game.labels[i][level_polygon_left]['bg'] = 'gray40'
                    if level_polygon_left < int(width_pole / 2) - 3:
                        level_polygon_left += 1
                    else:
                        level_polygon_left = 0
                    for i in window_game.polygon_left_up:
                        window_game.labels[i][level_polygon_left]['bg'] = 'white'
                    window_game.level_polygon_left = level_polygon_left
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = int(height_pole / 2)
            napravlenie_x = random.choice([-1, 1])
            napravlenie_y = random.choice([-1, 1])
    else:  # отскок от горизонтальной платформы
        if window_game.labels[y + napravlenie_y][x]['bg'] == 'white':
            napravlenie_y *= -1
            if y < int(width_pole / 2):
                count_left += 1
            else:
                count_right += 1
        elif window_game.labels[y + napravlenie_y][x + napravlenie_x]['bg'] == 'white':  # ??? иногда выпадает ошибка
            napravlenie_x *= -1
            napravlenie_y *= -1
        elif y == height_pole-1:  # last_y
            print('Проиграл!')
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = int(height_pole / 2)
            napravlenie_x = random.choice([-1, 1])
            napravlenie_y = random.choice([-1, 1])


def drive_polygon_y_left():
    while True:
        if keyboard.is_pressed('w') is True:
            window_game.up_polygon_left()
        if keyboard.is_pressed('s') is True:
            window_game.down_polygon_left()
        time.sleep(speed_polygon)


def drive_polygon_y_right():
    while True:
        if keyboard.is_pressed('8') is True:
            window_game.up_polygon_right()
        if keyboard.is_pressed('5') is True:
            window_game.down_polygon_right()
        time.sleep(speed_polygon)


def pause():
    global c
    window_game.labels[y][x]['bg'] = 'red'
    window_game.label7['text'] = str(health_left)
    window_game.label8['text'] = str(health_right)
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed('space') is True:
            c.start()
            break


def start(change_w, change_h):
    global window_game
    global x, y
    global c
    global napravlenie_x, napravlenie_y
    global height_pole, width_pole
    global type_polygon
    global type_game
    global level_polygon_left, level_polygon_right

    # -------------параметры поля и игры-------------

    height_pole = change_h
    width_pole = change_w
    width_polygon = 5
    type_polygon = 'y'
    type_game = ''
    level_polygon_left = 0
    level_polygon_right = -1

    # -------------системные параметры-------------

    x = int(width_pole / 2)
    y = int(height_pole / 2)
    napravlenie_x = random.choice([-1, 1])
    napravlenie_y = random.choice([-1, 1])

    # -------------создадим игровое окно-------------

    window_game = window.FramugaTwoPolygons(type_polygon, width_polygon, width_pole, height_pole)  # объявим окно

    # -------------создадим пару потоков для движения мячика и движения платформы-------------

    c = threading.Thread(target=drive_ball)  # объявим поток движения мячика
    wait_key_left = threading.Thread(target=drive_polygon_y_left)
    wait_key_right = threading.Thread(target=drive_polygon_y_right)
    ready_game_spase = threading.Thread(target=pause)

    # -------------запустим все потоки-------------

    # c.start()  # запустим поток движения мячика
    ready_game_spase.start()
    wait_key_left.start()  # запустим поток движения левой платформы
    wait_key_right.start()  # запустим поток движения правой платформы
    window_game.bild_window()


if __name__ == '__main__':
    start(40, 20)

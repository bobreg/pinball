import window
import threading
import time
import keyboard
import random


# параметры поля и игры
height_pole = 20
width_pole = 10
speed_ball = [0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05]  # 0.08
choice_speed_ball = 0
speed_polygon = 0.02
width_polygon = 5
level_polygon = -1
type_polygon = 'x'
type_game = 2
# системные параметры
x = int(width_pole / 2)
y = height_pole - 2
vector_x = random.choice([-1, 1])
vector_y = -1
flag_left_up = False
flag_right_down = False
flag_game_restart = False
flag_next_level = False
count_right = 0
count_left = 0


def drive_ball():
    print('start')
    global x, y, level_polygon
    global vector_x, vector_y
    global count_left, count_right
    global flag_left_up, flag_right_down, flag_game_restart
    global c
    global choice_speed_ball
    while True:  # пошлём в window координаты положения мячика и затрём его положение
        if flag_game_restart is not True:
            window_game.labels[y][x]['bg'] = 'gray40'
            x += vector_x  # изменим координаты и сделаем проверки
            y += vector_y
    # ----меняем координату х--------
            if x >= width_pole-1:
                x = width_pole - 1
                vector_x = -1
            elif x <= 0:
                x = 0
                vector_x = 1
    # ----меняем координату у--------
            if y >= height_pole-1:
                y = height_pole - 1
                vector_y = -1
            elif y <= 0:
                y = 0
                vector_y = 1
    # ---------отрисуем новое положение мячика---------------
            window_game.labels[y][x]['bg'] = 'red'
            time.sleep(speed_ball[choice_speed_ball])
    # ---------отскок----------------
            if y < 9:  # для оптимизации проверку отскока от фигуры будем проводить когда мячик будет вверху поля
                otskok_of_figure()
                if flag_next_level is True:
                    flag_game_restart = False
                    c = threading.Thread(target=drive_ball)
                    window_game.labels[y][x]['bg'] = 'gray40'
                    for i in window_game.polygon:
                        window_game.labels[level_polygon][i]['bg'] = 'gray40'
                    if level_polygon > -8:
                        level_polygon -= 1
                    else:
                        level_polygon = -1
                        choice_speed_ball = (choice_speed_ball + 1) % 7
                    window_game.level_polygon = level_polygon
                    x = int(width_pole / 2)
                    y = height_pole - 2
                    vector_x = random.choice([-1, 1])
                    vector_y = -1
                    window_game.figure()
                    for i in window_game.polygon:
                        window_game.labels[level_polygon][i]['bg'] = 'white'
                    pause()
                    break
            if y > 9 or y < 2:
                otskok()  # для оптимизации проверку отскока от площадки проводим когда мячик будет внизу поля
        else:
            flag_game_restart = False
            c = threading.Thread(target=drive_ball)
            pause()
            break


def otskok():
    global x, y
    global vector_x, vector_y
    global count_left, count_right
    global flag_left_up, flag_right_down, flag_game_restart
    if window_game.labels[y + vector_y][x]['bg'] == 'white':
        vector_y *= -1
        count_left += 1
    elif window_game.labels[y + vector_y][x + vector_x]['bg'] == 'white':  # ??? иногда выпадает ошибка
        vector_x *= -1
        vector_y *= -1
    elif type_game == 1:
        if y == height_pole - 1:
            print('Проиграл!')
            # window_game.figure()
            flag_game_restart = True
            count_left = 0
            window_game.label1['text'] = str(count_left)
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = height_pole - 2
            vector_x = random.choice([-1, 1])
            vector_y = -1
    elif type_game == 2:
        if y == height_pole-1 or y == 0:
            print('Проиграл!')
            # window_game.figure()
            flag_game_restart = True
            count_left = 0
            window_game.label1['text'] = str(count_left)
            window_game.labels[y][x]['bg'] = 'gray40'
            x = int(width_pole / 2)
            y = height_pole - 2
            vector_x = random.choice([-1, 1])
            vector_y = -1


def otskok_of_figure():
    global x, y
    global vector_x, vector_y
    global count_left, count_right
    global flag_next_level
    if x + vector_x < 10 and y + vector_y < 10:
        if window_game.labels[y + vector_y][x]['bg'] == 'sandy brown':
            window_game.labels[y + vector_y][x]['bg'] = 'gray40'
            vector_y *= -1
            count_left += 1
            window_game.label1['text'] = str(count_left)
        else:
            if window_game.labels[y + vector_y][x + vector_x]['bg'] == 'sandy brown':
                window_game.labels[y + vector_y][x + vector_x]['bg'] = 'gray40'
                vector_x *= -1
                vector_y *= -1
                count_left += 1
                window_game.label1['text'] = str(count_left)
    if x + vector_x < 10 and y + vector_y < 10:
        if window_game.labels[y][x + vector_x]['bg'] == 'sandy brown':
            window_game.labels[y][x + vector_x]['bg'] = 'gray40'
            vector_x *= -1
            count_left += 1
            window_game.label1['text'] = str(count_left)
        else:
            if window_game.labels[y + vector_y][x + vector_x]['bg'] == 'sandy brown':
                window_game.labels[y + vector_y][x + vector_x]['bg'] = 'gray40'
                vector_x *= -1
                vector_y *= -1
                count_left += 1
                window_game.label1['text'] = str(count_left)
    k = -1
    flag_next_level = True
    for i in range(5):
        if i < 3:
            k += 1
        else:
            k -= 1
        for j in range(8 - 2 * k):
            if window_game.labels[3 + i][1 + k + j]['bg'] == 'sandy brown':
                flag_next_level = False


def drive_polygon_x():
    global flag_left_up, flag_right_down
    global height_pole, x, vector_x
    while True:
        if keyboard.is_pressed('left') is True and window_game.polygon[0] != 0:
            window_game.shift_left_polygon()
            if y > height_pole - 3 + level_polygon + 1 and \
                    window_game.labels[window_game.level_polygon][x]['bg'] == 'white':
                if x != 0:
                    window_game.labels[y][x]['bg'] = 'gray40'
                    vector_x = -1
                    x -= 1
                    window_game.labels[y][x]['bg'] = 'red'
        if keyboard.is_pressed('right') is True and \
                window_game.polygon[-1] != width_pole-1:
            window_game.shift_right_polygon()
            if y > height_pole - 3 + level_polygon + 1 and \
                    window_game.labels[window_game.level_polygon][x]['bg'] == 'white':
                if x < width_pole - 2:
                    window_game.labels[y][x]['bg'] = 'gray40'
                    vector_x = 1
                    x += 1
                    window_game.labels[y][x]['bg'] = 'red'
        time.sleep(speed_polygon)


def pause():
    global c, y
    y = y + level_polygon + 1
    window_game.labels[y][x]['bg'] = 'red'
    window_game.label4['text'] = str(level_polygon * -1)
    window_game.label6['text'] = str(choice_speed_ball+1)
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed('space') is True:
            c.start()
            break


def start(a, b, d):
    global c
    global window_game
    global level_polygon, choice_speed_ball
    global type_game
    level_polygon = -a
    choice_speed_ball = b
    type_game = d
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
        window_game.figure()  # вызовем метод рисования фигуры для одинчного режима тетрис

    # -------------создадим пару потоков для движения мячика и движения платформы-------------

    c = threading.Thread(target=drive_ball)  # объявим поток движения мячика
    wait_key = threading.Thread(target=drive_polygon_x)
    ready_game_space = threading.Thread(target=pause)

    # -------------запустим все потоки-------------

    # c.start()  # запустим поток движения мячика
    ready_game_space.start()
    wait_key.start()  # запустим поток движения платформы
    # window_new_game.new_game.destroy()  # оставить в main.py не забыть
    window_game.bild_window()


if __name__ == '__main__':
    start(1, 1, 1)

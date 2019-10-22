import tkinter
import os


class Kletka(tkinter.Label):
    def __init__(self,
                 frame,
                 text='     ',
                 width=2,
                 height=1,
                 bg='gray40',
                 relief='ridge',
                 font='Arial 9'):
        self.text = text
        self.width = width
        self.height = height
        self.bg = bg
        self.relief = relief
        self.font = font
        tkinter.Label.__init__(self,
                               frame,
                               text=self.text,
                               width=self.width,
                               height=self.height,
                               bg=self.bg,
                               relief=self.relief,
                               font=self.font)
        self.frame = frame


class MyButton(tkinter.Button):
    def __init__(self,
                 frame,
                 text='     ',
                 width=2,
                 height=1,
                 font='Arial 12',
                 command=None):
        self.text = text
        self.width = width
        self.height = height
        self.frame = frame
        self.font = font
        self.command = command
        tkinter.Button.__init__(self,
                                frame,
                                text=self.text,
                                width=self.width,
                                height=self.height,
                                font=self.font,
                                command=self.command)


class MyFrame(tkinter.Frame):
    def __init__(self,
                 frame,
                 bg='SystemButtonFace',
                 height=300,
                 width=100):  # 'SystemButtonFace'
        self.frame = frame
        self.bg = bg
        self.height = height
        self.width = width
        tkinter.Frame.__init__(self, self.frame, bg=self.bg, height=self.height, width=self.width)


class Framuga:
    def __init__(self,
                 type_polygon='y',
                 len_polygon=8,
                 widtn_pole=50,
                 height_pole=25,
                 level_polygon=-1):

        self.len_polygon = len_polygon
        self.widtn_pole = widtn_pole
        self.height_pole = height_pole
        self.type_polygon = type_polygon
        self.k = -1
        self.level_polygon = level_polygon
        self.piypiy = tkinter.Tk()
        self.piypiy.title('Пин-Пон от Alex_Chel_Man')
        self.piypiy.geometry('{}x{}'.format(widtn_pole*20+150, height_pole*23+10))
        self.pole = tkinter.Frame(self.piypiy)
        self.labels = [[Kletka(self.pole) for self.i in range(self.widtn_pole)] for self.j in range(self.height_pole)]

        if self.type_polygon == 'y':
            self.start_poligone = int(self.height_pole / 2) - int(self.len_polygon / 2)
            self.stop_poligone = self.start_poligone + self.len_polygon
        else:
            self.start_poligone = int(self.widtn_pole / 2) - int(self.len_polygon / 2)
            self.stop_poligone = self.start_poligone + self.len_polygon
        self.polygon = [i for i in range(self.start_poligone, self.stop_poligone)]
        for self.i in self.polygon:
            if self.type_polygon == 'y':
                self.labels[self.i][0]['bg'] = 'white'
            else:
                self.labels[self.level_polygon][self.i]['bg'] = 'white'

        self.label1 = Kletka(self.piypiy, '0', 3, 2, 'gray50', 'groove', 'Arial 15')
        self.label2 = Kletka(self.piypiy, '0', 3, 2, 'gray50', 'groove', 'Arial 15')
        self.label3 = Kletka(self.piypiy, 'Уровень', 7, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label4 = Kletka(self.piypiy, '0', 3, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label5 = Kletka(self.piypiy, 'Скорость', 8, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label6 = Kletka(self.piypiy, '0', 3, 1, 'SystemButtonFace', 'flat', 'Arial 12')

    def bild_window(self):
        self.pole.place(x=0, y=0)
        for self.i in range(self.height_pole):
            for self.j in range(self.widtn_pole):
                self.labels[self.i][self.j].grid(row=self.i, column=self.j)
        self.label1.place(x=int(self.widtn_pole*18/2)-50, y=self.height_pole*22-20)
        self.label2.place(x=int(self.widtn_pole*18/2)+50, y=self.height_pole*22-20)
        self.label3.place(x=int(self.widtn_pole * 20)+50, y=10)
        self.label4.place(x=int(self.widtn_pole * 20)+60, y=40)
        self.label5.place(x=int(self.widtn_pole * 20) + 50, y=100)
        self.label6.place(x=int(self.widtn_pole * 20) + 60, y=130)
        self.piypiy.protocol('WM_DELETE_WINDOW', lambda: os._exit(0))
        self.piypiy.mainloop()
        return 0
        # тоже вариант, но всё-таки движение не должно быть в классе
        # self.piypiy.bind('w', self.up_polygon)
        # self.piypiy.bind('s', self.down_polygon)

    def up_polygon(self):
        if self.polygon[0] >= 1:
            self.labels[self.polygon[-1]][0]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] -= 1
                self.labels[self.polygon[self.i]][0]['bg'] = 'white'

    def down_polygon(self):
        if self.polygon[-1] < self.height_pole-1:
            self.labels[self.polygon[0]][0]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] += 1
                self.labels[self.polygon[self.i]][0]['bg'] = 'white'

    def shift_left_polygon(self):
        if self.polygon[0] > 0:
            self.labels[self.level_polygon][self.polygon[-1]]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] -= 1
                self.labels[self.level_polygon][self.polygon[self.i]]['bg'] = 'white'

    def shift_right_polygon(self):
        if self.polygon[-1] < self.widtn_pole-1:
            self.labels[self.level_polygon][self.polygon[0]]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] += 1
                self.labels[self.level_polygon][self.polygon[self.i]]['bg'] = 'white'

    def figure(self):
        self.k = -1
        for self.i in range(5):
            if self.i < 3:
                self.k += 1
            else:
                self.k -= 1
            for self.j in range(8-2*self.k):
                self.labels[3 + self.i][1 + self.k + self.j]['bg'] = 'sandy brown'


class FramugaTwoPolygons:
    def __init__(self,
                 type_polygon='y',
                 len_polygon=8,
                 widtn_pole=50,
                 height_pole=25,
                 level_polygon_left=0,
                 level_polygon_right=-1,
                 level_polygon=-1):

        self.len_polygon = len_polygon
        self.widtn_pole = widtn_pole
        self.height_pole = height_pole
        self.type_polygon = type_polygon
        self.k = -1
        self.level_polygon_left = level_polygon_left
        self.level_polygon_right = level_polygon_right
        self.level_polygon = level_polygon
        self.piypiy = tkinter.Tk()
        self.piypiy.title('Пин-Пон от Alex_Chel_Man')
        self.piypiy.geometry('{}x{}'.format(widtn_pole*20+150, height_pole*23+10))
        self.pole = tkinter.Frame(self.piypiy)
        self.labels = [[Kletka(self.pole) for self.i in range(self.widtn_pole)] for self.j in range(self.height_pole)]

        if self.type_polygon == 'y':
            self.start_poligone = int(self.height_pole / 2) - int(self.len_polygon / 2)
            self.stop_poligone = self.start_poligone + self.len_polygon
        else:
            self.start_poligone = int(self.widtn_pole / 2) - int(self.len_polygon / 2)
            self.stop_poligone = self.start_poligone + self.len_polygon
        self.polygon = [i for i in range(self.start_poligone, self.stop_poligone)]
        self.polygon_left_up = [i for i in range(self.start_poligone, self.stop_poligone)]
        self.polygon_right_down = [i for i in range(self.start_poligone, self.stop_poligone)]
        for self.i in self.polygon:
            if self.type_polygon == 'y':
                self.labels[self.i][self.level_polygon_left]['bg'] = 'white'
                self.labels[self.i][self.level_polygon_right]['bg'] = 'white'
            else:
                self.labels[0][self.i]['bg'] = 'white'
                self.labels[self.level_polygon][self.i]['bg'] = 'white'

        self.label1 = Kletka(self.piypiy, '0', 3, 2, 'gray50', 'groove', 'Arial 15')
        self.label2 = Kletka(self.piypiy, '0', 3, 2, 'gray50', 'groove', 'Arial 15')
        self.label3 = Kletka(self.piypiy, 'Уровень', 7, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label4 = Kletka(self.piypiy, '0', 3, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label5 = Kletka(self.piypiy, 'Скорость', 8, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label6 = Kletka(self.piypiy, '0', 3, 1, 'SystemButtonFace', 'flat', 'Arial 12')
        self.label7 = Kletka(self.piypiy, '0', 3, 2, 'DarkOliveGreen3', 'groove', 'Arial 15')
        self.label8 = Kletka(self.piypiy, '0', 3, 2, 'DarkOliveGreen3', 'groove', 'Arial 15')

    def bild_window(self):
        self.pole.place(x=0, y=0)
        for self.i in range(self.height_pole):
            for self.j in range(self.widtn_pole):
                self.labels[self.i][self.j].grid(row=self.i, column=self.j)
        self.label1.place(x=int(self.widtn_pole*18/2)-50, y=self.height_pole*22-20)
        self.label2.place(x=int(self.widtn_pole*18/2)+50, y=self.height_pole*22-20)
        self.label3.place(x=int(self.widtn_pole * 20) + 50, y=10)
        self.label4.place(x=int(self.widtn_pole * 20) + 60, y=40)
        self.label5.place(x=int(self.widtn_pole * 20) + 50, y=100)
        self.label6.place(x=int(self.widtn_pole * 20) + 60, y=130)
        self.label7.place(x=0, y=self.height_pole * 22 - 20)
        self.label8.place(x=int(self.widtn_pole * 18), y=self.height_pole * 22 - 20)
        self.piypiy.protocol('WM_DELETE_WINDOW', lambda: os._exit(0))
        self.piypiy.mainloop()
        return 0
        # тоже вариант, но всё-таки движение не должно быть в классе
        # self.piypiy.bind('w', self.up_polygon)
        # self.piypiy.bind('s', self.down_polygon)

    def up_polygon(self):
        if self.polygon[0] >= 1:
            self.labels[self.polygon[-1]][0]['bg'] = 'gray40'
            self.labels[self.polygon[-1]][-1]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] -= 1
                self.labels[self.polygon[self.i]][0]['bg'] = 'white'
                self.labels[self.polygon[self.i]][-1]['bg'] = 'white'

    def down_polygon(self):
        if self.polygon[-1] < self.height_pole-1:
            self.labels[self.polygon[0]][0]['bg'] = 'gray40'
            self.labels[self.polygon[0]][-1]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] += 1
                self.labels[self.polygon[self.i]][0]['bg'] = 'white'
                self.labels[self.polygon[self.i]][-1]['bg'] = 'white'

    def up_polygon_left(self):
        if self.polygon_left_up[0] >= 1:
            self.labels[self.polygon_left_up[-1]][self.level_polygon_left]['bg'] = 'gray40'
            for self.i in range(len(self.polygon_left_up)):
                self.polygon_left_up[self.i] -= 1
                self.labels[self.polygon_left_up[self.i]][self.level_polygon_left]['bg'] = 'white'

    def down_polygon_left(self):
        if self.polygon_left_up[-1] < self.height_pole-1:
            self.labels[self.polygon_left_up[0]][self.level_polygon_left]['bg'] = 'gray40'
            for self.i in range(len(self.polygon_left_up)):
                self.polygon_left_up[self.i] += 1
                self.labels[self.polygon_left_up[self.i]][self.level_polygon_left]['bg'] = 'white'

    def up_polygon_right(self):
        if self.polygon_right_down[0] >= 1:
            self.labels[self.polygon_right_down[-1]][self.level_polygon_right]['bg'] = 'gray40'
            for self.i in range(len(self.polygon_right_down)):
                self.polygon_right_down[self.i] -= 1
                self.labels[self.polygon_right_down[self.i]][self.level_polygon_right]['bg'] = 'white'

    def down_polygon_right(self):
        if self.polygon_right_down[-1] < self.height_pole-1:
            self.labels[self.polygon_right_down[0]][self.level_polygon_right]['bg'] = 'gray40'
            for self.i in range(len(self.polygon_right_down)):
                self.polygon_right_down[self.i] += 1
                self.labels[self.polygon_right_down[self.i]][self.level_polygon_right]['bg'] = 'white'

    def shift_left_polygon(self):
        if self.polygon[0] > 0:
            self.labels[self.level_polygon][self.polygon[-1]]['bg'] = 'gray40'
            self.labels[0][self.polygon[-1]]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] -= 1
                self.labels[self.level_polygon][self.polygon[self.i]]['bg'] = 'white'
                self.labels[0][self.polygon[self.i]]['bg'] = 'white'

    def shift_right_polygon(self):
        if self.polygon[-1] < self.widtn_pole-1:
            self.labels[self.level_polygon][self.polygon[0]]['bg'] = 'gray40'
            self.labels[0][self.polygon[0]]['bg'] = 'gray40'
            for self.i in range(len(self.polygon)):
                self.polygon[self.i] += 1
                self.labels[self.level_polygon][self.polygon[self.i]]['bg'] = 'white'
                self.labels[0][self.polygon[self.i]]['bg'] = 'white'

    def figure(self):
        self.k = -1
        for self.i in range(5):
            if self.i < 3:
                self.k += 1
            else:
                self.k -= 1
            for self.j in range(8-2*self.k):
                self.labels[3 + self.i][1 + self.k + self.j]['bg'] = 'sandy brown'


class WindowNewGame:
    def __init__(self):
        self.new_game = tkinter.Tk()
        self.new_game.title('Во что хочешь поиграть?')
        self.new_game.geometry('400x200')

        self.choice_platform = tkinter.IntVar()
        self.choice_platform.set(1)
# -----------------------------
        self.frame1 = MyFrame(self.new_game)
        self.button1 = MyButton(self.frame1, 'Пин-пон', 10, 2)
        self.frame_none1 = MyFrame(self.frame1, height=25, width=100)
        self.button2 = MyButton(self.frame1, 'Против всех', 10, 2)
        self.frame_none2 = MyFrame(self.frame1, height=25, width=100)
        self.button3 = MyButton(self.frame1, 'Тест', 10, 2)
# -----------------------------
        self.frame2 = MyFrame(self.new_game, 'SystemButtonFace')
        self.label_level = Kletka(self.frame2, 'Уровень:', 7, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.label_level_value = Kletka(self.frame2, '1', 1, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.button1_plus = MyButton(self.frame2, '+', 2, 1, 'Arial 6')
        self.button1_minus = MyButton(self.frame2, '-', 2, 1, 'Arial 6')

        self.label_width = Kletka(self.frame2, 'Ширина:', 7, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.label_width_value = Kletka(self.frame2, '40', 1, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.button3_plus = MyButton(self.frame2, '+', 2, 1, 'Arial 6')
        self.button3_minus = MyButton(self.frame2, '-', 2, 1, 'Arial 6')
# -----------------------------
        self.frame3 = MyFrame(self.new_game, 'SystemButtonFace')
        self.label_speed = Kletka(self.frame3, 'Скорость:', 8, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.label_speed_value = Kletka(self.frame3, '1', 1, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.button2_plus = MyButton(self.frame3, '+', 2, 1, 'Arial 6')
        self.button2_minus = MyButton(self.frame3, '-', 2, 1, 'Arial 6')

        self.label_height = Kletka(self.frame3, 'Высота:', 7, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.label_height_value = Kletka(self.frame3, '20', 1, 1, 'SystemButtonFace', 'flat', 'Arial 8')
        self.button4_plus = MyButton(self.frame3, '+', 2, 1, 'Arial 6')
        self.button4_minus = MyButton(self.frame3, '-', 2, 1, 'Arial 6')
# -----------------------------
        self.frame4 = MyFrame(self.new_game, 'SystemButtonFace')
        self.check1 = tkinter.Radiobutton(self.frame4, text='Одна\nплатформа', value=1,
                                          font='Arial 6', variable=self.choice_platform)
        self.check2 = tkinter.Radiobutton(self.frame4, text='Две\nплатформы', value=2,
                                          font='Arial 6', variable=self.choice_platform)
# -----------------------------
        self.frame1.pack_propagate(False)  # это очень нужная штука.делает так что бы можно было подгонять размер фрейма
        self.frame2.pack_propagate(False)
        self.frame3.pack_propagate(False)
        self.frame4.pack_propagate(False)
# -----------------------------
        self.frame1.pack(side='left')
        self.button1.pack()
        self.frame_none1.pack()
        self.button2.pack()
        self.frame_none2.pack()
        self.button3.pack()
# -----------------------------
        self.frame2.pack(side='left')
        self.label_level.place(x=15, y=0)
        self.label_level_value.place(x=64, y=0)
        self.button1_plus.place(x=20, y=25)
        self.button1_minus.place(x=50, y=25)

        self.label_width.place(x=15, y=70)
        self.label_width_value.place(x=64, y=70)
        self.button3_plus.place(x=20, y=95)
        self.button3_minus.place(x=50, y=95)
# -----------------------------
        self.frame3.pack(side='left')
        self.label_speed.place(x=15, y=0)
        self.label_speed_value.place(x=67, y=0)
        self.button2_plus.place(x=20, y=25)
        self.button2_minus.place(x=50, y=25)

        self.label_height.place(x=15, y=70)
        self.label_height_value.place(x=64, y=70)
        self.button4_plus.place(x=20, y=95)
        self.button4_minus.place(x=50, y=95)
# -----------------------------
        self.frame4.pack(side='left')
        self.check1.place(x=15, y=0)
        self.check2.place(x=15, y=25)

    def start(self):
        self.new_game.mainloop()


if __name__ == '__main__':
    okno = WindowNewGame()
    # okno = Framuga().bild_window()

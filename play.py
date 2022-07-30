from modules import * 

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')
system("clear")
class tttApp(App):
    
    title="ttt game"
    
    def build(self):
        self.figure = 'O'
        self.arr = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

        def press_btn(instance):
            if not instance.text.isdigit():
                return

            self.arr[int(instance.text)] = self.figure

            if self.figure == 'O':
                instance.color = (0, 0, 1)
                instance.text = self.figure
                instance.font_size = 70
                self.figure = 'X'
            else:
                instance.text = self.figure
                instance.color = (1, 0, 0)
                instance.font_size = 70
                self.figure = 'O'

            check_combination(self.arr)

        def check_combination(arr):
            wining_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

            for (x, y, z) in wining_combination:
                if arr[x] == arr[y] and arr[y] == arr[z] and (arr[x] == 'X' or arr[x] == 'O'):
                    self.label.text = f'{arr[x]} won'
                    self.field.disabled = True
                    Clock.schedule_once(restart_game, 1.5)
                    return

            if '_' not in arr:
                self.label.text = 'draw'
                self.field.disabled = True
                Clock.schedule_once(restart_game, 1.5)
                return

        def restart_game(dt):
            self.field.clear_widgets()
            self.label.text = 'play'
            self.field.disabled = False
            self.figure = 'O'
            self.arr = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            render_field()

        def render_field():
            for id_num in range(9):
                self.field.add_widget(Button(text=str(id_num), font_size=0, on_press=press_btn, color=(0, 0, 0, 0)))

        main_bl = BoxLayout(orientation='vertical', spacing=5, padding=3)
        self.label = Label(text='play', font_size=50, size_hint=(1, .3))
        self.field = GridLayout(cols=3, spacing=3)

        render_field()

        main_bl.add_widget(self.label)
        main_bl.add_widget(self.field)

        return main_bl





if __name__ == '__main__':
    tttApp().run()
    system("clear")

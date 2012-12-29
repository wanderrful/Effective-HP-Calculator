'''
brainstorming

i want to just type the hp, hit enter, type the armor, hit enter,
then be shown my ehp.  if i hit enter again, i can reset it.

i just need a small window with large print that will let me do this quickly.
'''
#Made by wanderrful on 29 December 2012
import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width                  =   485
        self.height                 =   300

        self.textLabelOffsetX       =   0
        self.textLabelOffsetY       =   -90

        self.gs                     =   0
        '''
        key for self.gs:
        -1  ->  Input Error
        0   ->  query HP
        1   ->  query Armor
        2   ->  display EHP
        3   ->  Error loading image
        '''

        try:
            self.Dota2Logo          =   pyglet.image.load('Dota2.png')
            self.Dota2Logo.anchor_x =   self.Dota2Logo.width//2
            self.Dota2Logo.anchor_y =   self.Dota2Logo.height//2
        except pyglet.image.ImageException:
            self.gs = 3

        self.labelHP                =   pyglet.text.Label(
            'HP? ',
            font_name   =   'Times New Roman',
            font_size   =   24,
            bold        =   True,
            italic      =   False,
            color       =   (255, 255, 255, 255),
            x = self.width // 2 + self.textLabelOffsetX, y = self.height // 2 + self.textLabelOffsetY,
            width = None, height = None,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left'
            )
        self.labelArmor             =   pyglet.text.Label(
            'Armor? ',
            font_name   =   'Times New Roman',
            font_size   =   24,
            bold        =   True,
            italic      =   False,
            color       =   (255, 255, 255, 255),
            x = self.width // 2 + self.textLabelOffsetX, y = self.height // 2 + self.textLabelOffsetY,
            width = None, height = None,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left'
            )
        self.labelEHP               =   pyglet.text.Label(
            'EHP = ',
            font_name   =   'Times New Roman',
            font_size   =   24,
            bold        =   True,
            italic      =   False,
            color       =   (255, 255, 255, 255),
            x = self.width // 2 + self.textLabelOffsetX, y = self.height // 2 + self.textLabelOffsetY,
            width = None, height = None,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left'
            )
        self.inputLabelError        =   pyglet.text.Label(
            'Error! Press Enter to start over.',
            font_name   =   'Times New Roman',
            font_size   =   24,
            bold        =   True,
            italic      =   False,
            color       =   (255, 255, 255, 255),
            x = self.width // 2 + self.textLabelOffsetX, y = self.height // 2 + self.textLabelOffsetY,
            width = None, height = None,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left'
            )
        self.loadImageError         =   pyglet.text.Label(
            'Error! Can\'t find the DotA2 logo!',
            font_name   =   'Times New Roman',
            font_size   =   24,
            bold        =   True,
            italic      =   False,
            color       =   (255, 255, 255, 255),
            x = self.width // 2 + self.textLabelOffsetX, y = self.height // 2 + self.textLabelOffsetY,
            width = None, height = None,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left'
            )

        self.labelLeft              =   pyglet.text.Label(
            'Just type numbers and hit Enter!',
            font_name   =   'Times New Roman',
            font_size   =   12,
            bold        =   False,
            italic      =   True,
            color       =   (255, 255, 255, 255),
            x = 10, y = self.height - 100,
            width = 150, height = 10,
            anchor_x = 'left', anchor_y = 'center',
            halign      =   'left',
            multiline   =   True
            )

        self.labelRight             =   pyglet.text.Label(
            'Hit Enter afterward to reset!',
            font_name   =   'Times New Roman',
            font_size   =   12,
            bold        =   False,
            italic      =   True,
            color       =   (255, 255, 255, 255),
            x = self.width - 70, y = self.height - 100,
            width = 150, height = 10,
            anchor_x = 'center', anchor_y = 'center',
            halign      =   'left',
            multiline   =   True
            )
        
        self.getEHP                 =   lambda hp, armor: int(hp + 0.06*armor*hp)
        
        self.reset()

    def reset(self): #not apart of the API, I must made this up

        self.labelHP.text           =   'HP? '
        self.labelArmor.text        =   'Armor? '
        self.labelEHP.text          =   'EHP = '
        self.gs                     =   0

    def on_draw(self):
        self.clear()

        try:
            self.Dota2Logo.blit(self.width // 2, self.height // 2 + self.Dota2Logo.height // 2 - 75)
        except:
            pass

        self.labelLeft.draw()
        self.labelRight.draw()

        #gamestate-dependent things to draw
        if self.gs == 0:
            self.labelHP.draw()
        elif self.gs == 1:
            self.labelArmor.draw()
        elif self.gs == 2:
            self.labelEHP.draw()
        elif self.gs == 3:
            self.loadImageError.draw()
        else:
            self.inputLabelError.draw()

    def on_key_press(self, symbol, modifiers):        
        #gamestate-dependent keybinds
        if self.gs == 0:
            if symbol == pyglet.window.key.ENTER:
                if len(self.labelHP.text) > 4:
                    self.gs = 1
                else:
                    pass
            elif symbol == pyglet.window.key.BACKSPACE:
                if len(self.labelHP.text) > 4:
                    self.labelHP.text = self.labelHP.text[:-1]
            else:
                try:
                    if isinstance(int(pyglet.window.key.symbol_string(symbol)[-1]),(int,long)):
                        self.labelHP.text += pyglet.window.key.symbol_string(symbol)[-1]
                    else:
                        pass
                except ValueError:
                    pass
                
        elif self.gs == 1:
            if symbol == pyglet.window.key.ENTER:
                if len(self.labelArmor.text) > 7:
                    self.labelEHP.text += `self.getEHP(int(self.labelHP.text.split()[-1]),int(self.labelArmor.text.split()[-1]))`
                    self.gs = 2
                else:
                    pass
            elif symbol == pyglet.window.key.BACKSPACE:
                if len(self.labelArmor.text) > 7:
                    self.labelArmor.text = self.labelArmor.text[:-1]
            else:
                try:
                    if isinstance(int(pyglet.window.key.symbol_string(symbol)[-1]),(int,long)):
                        self.labelArmor.text += pyglet.window.key.symbol_string(symbol)[-1]
                    else:
                        pass
                except ValueError:
                    pass
                
        elif self.gs in {2,3}:
            if symbol == pyglet.window.key.ENTER:
                self.reset()
            else:
                pass
        
    def on_key_release(self, symbol, modifiers):
        pass

if __name__ == '__main__':
    window = MainWindow()
    pyglet.app.run()

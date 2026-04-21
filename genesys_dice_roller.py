import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty, StringProperty, ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('genesys_dice_roller.kv')
class MyLayout(Widget):
    # TODO: Refactor this to follow DRY.
    die_faces_Yellow = ListProperty([1,2,3,4,5,6,7,8,9,10,11,12])
    die_count_Yellow = NumericProperty(1)
    die_faces_Green = ListProperty([1,2,3,4,5,6,7,8])
    die_count_Green = NumericProperty(1)
    die_faces_Blue = ListProperty([1,2,3,4,5,6])
    die_count_Blue = NumericProperty(1)
    die_faces_Red = ListProperty([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    die_count_Red = NumericProperty(1)
    die_faces_Purple = ListProperty([8, 7, 6, 5, 4, 3, 2, 1])
    die_count_Purple = NumericProperty(1)
    die_faces_Black = ListProperty([6, 5, 4, 3, 2, 1])
    die_count_Black = NumericProperty(1)

    def press_roll(self, button):
        result = 0
        # TODO: Refactor this to follow DRY
        for i in range(0, self.die_count_Yellow):
            result += roll_die(self.die_faces_Yellow)
        for i in range(0, self.die_count_Green):
            result += roll_die(self.die_faces_Green)
        for i in range(0, self.die_count_Blue):
            result += roll_die(self.die_faces_Blue)
        for i in range(0, self.die_count_Red):
            result -= roll_die(self.die_faces_Red)
        for i in range(0, self.die_count_Purple):
            result -= roll_die(self.die_faces_Purple)
        for i in range(0, self.die_count_Black):
            result -= roll_die(self.die_faces_Black)
        self.ids.results_label.text = f"{result}"
    def press_mod_dice(self, dice, mod):
        if dice == "Yellow":
            self.die_count_Yellow = adjust_value(self.die_count_Yellow, mod, 1, 5)
        if dice == "Green":
            self.die_count_Green = adjust_value(self.die_count_Green, mod, 1, 5)
        if dice == "Blue":
            self.die_count_Blue = adjust_value(self.die_count_Blue, mod, 1, 5)
        if dice == "Red":
            self.die_count_Red = adjust_value(self.die_count_Red, mod, 1, 5)
        if dice == "Purple":
            self.die_count_Purple = adjust_value(self.die_count_Purple, mod, 1, 5)
        if dice == "Black":
            self.die_count_Black = adjust_value(self.die_count_Black, mod, 1, 5)
    

class DiceRollerApp(App):
    def build(self):
        return MyLayout()
   
def smallest_int(int1, int2):
    if int1 >= int2:
        return int2
    elif int1 < int2:
        return int1
    
def roll_die(die):
    die_face = random.randrange(0,len(die))
    return die[die_face]

def adjust_value(value, adj, min, max):
    return_value = value + adj
    if (return_value > max):
        return_value = max
    if (return_value < min):
        return_value = min
    return return_value

if __name__ == "__main__":
    DiceRollerApp().run()
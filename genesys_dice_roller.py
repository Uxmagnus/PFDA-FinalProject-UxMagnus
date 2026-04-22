import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty, StringProperty, ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('genesys_dice_roller.kv')

class dice():
    def __init__(self, faces, count = 1):
        self.faces = faces
        self.count = count

class MyLayout(Widget):
    # TODO: Refactor this to follow DRY.
    dice_types = {}
    dice_types["Yellow"] = dice([1,2,3,4,5,6,7,8,9,10,11,12])
    dice_types["Green"] = dice([1,2,3,4,5,6,7,8])
    dice_types["Blue"] = dice([1,2,3,4,5,6])
    dice_types["Red"] = dice([-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])
    dice_types["Purple"] = dice([-8, -7, -6, -5, -4, -3, -2, -1])
    dice_types["Black"] = dice([-6, -5, -4, -3, -2, -1])


    def press_roll(self, button):
        result = 0
        # TODO: Refactor this to follow DRY
        for k,v in MyLayout.dice_types.items():
            for i in range(v.count):
                result += roll_die(v.faces)
        self.ids.results_label.text = f"{result}"

    def press_mod_dice(self, dice, mod):
        for k,v in MyLayout.dice_types.items():
            if dice == k:
                v.count = adjust_value(int(v.count), mod, 0, 5)
                for widget_id, widget_instance in self.ids.items():
                    if k.lower() in widget_id.lower():
                        widget_instance.text = f"{v.count}"
    

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
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

#might do something like this later. This iteration of the code will do it a stupid way first.
""" class faces():
    def __init__(self, success, advantage, triumph, despair):
        self.success = success
        self.advantage = advantage
        self.triumph = triumph
        self.despair = despair """

class MyLayout(Widget):
    dice_types = {}
    dice_types["Yellow"] = dice(["NN","SN","SS","AA","SA","SA","AA","SA","SS","SN","AN","SV"])
    dice_types["Green"] = dice(["NN","AA","AN","SN","SN","SS","AN","SA"])
    dice_types["Blue"] = dice(["NN","AA","AN","SN","SA","NN"])
    dice_types["Red"] = dice(["FD", "TN", "FN", "TT", "FT", "FF", "FN", "TN", "FF", "TT", "FT", "NN"])
    dice_types["Purple"] = dice(["FF", "TN", "FN", "FT", "TN", "TN", "TT", "NN"])
    dice_types["Black"] = dice(["NN", "FN", "TN", "FN", "TN", "NN"])


    def press_roll(self, button):
        success = 0
        advantage = 0
        triumph = 0
        despair = 0
        roll_result = "" 
        for k,v in MyLayout.dice_types.items():
            for i in range(v.count):
                result = roll_die(v.faces)
                for letter in result:
                    match letter:
                        case "S":
                            success += 1
                        case "A":
                            advantage += 1
                        case "V":
                            triumph += 1
                        case "F":
                            success -= 1
                        case "T":
                            advantage -= 1
                        case "D":
                            despair += 1
                        case "N":
                            pass
        self.ids.results_label.text = f"{success} successes, {advantage} advantage, {triumph} triumphs, and {despair} despairs"

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
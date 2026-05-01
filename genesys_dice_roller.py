import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty, StringProperty, ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('genesys_dice_roller.kv')

Window.size = (600, 800)

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
    # Proficiency Dice Breakdown: Blank, Success, Success, 2 Successes, 2 Successes, Advantage, Success+Advantage, Success+Advantage, Success+Advantage, 2 Advantages, 2 Advantages, Triumph (+Success)
    dice_types["Yellow"] = dice(["NN","SN","SS","AA","SA","SA","AA","SA","SS","SN","AN","SV"])
    # Ability Dice Breakdown: Blank, Success, Success, 2 Successes, Advantage, Advantage, Success+Advantage, 2 Advantages.
    dice_types["Green"] = dice(["NN","AA","AN","SN","SN","SS","AN","SA"])
    # Boost Dice Breakdown: Blank, Blank, Success, Success+Advantage, Advantage, Advantage.
    dice_types["Blue"] = dice(["NN","AA","AN","SN","SA","NN"])
    # Challenge Dice Breakdown: Blank, Failure, Failure, 2 Failures, 2 Failures, Threat, Threat, Failure+Threat, Failure+Threat, 2 Threats, 2 Threats, Despair (+Failure)
    dice_types["Red"] = dice(["FD", "TN", "FN", "TT", "FT", "FF", "FN", "TN", "FF", "TT", "FT", "NN"])
    # Difficulty Dice Breakdown: Blank, Failure, Failure, 2 Failures, 2 Failures, Threat, Threat, Failure+Threat, Failure+Threat, 2 Threats, 2 Threats, Despair.
    dice_types["Purple"] = dice(["FF", "TN", "FN", "FT", "TN", "TN", "TT", "NN"])
    # Setback Dice Breakdown: Blank, Blank, Failure, Failure, Threat, Threat.
    dice_types["Black"] = dice(["NN", "FN", "TN", "FN", "TN", "NN"])
    # Force Dice Breakdown: 5 Dark Side, 1 Dark Side * 2, 3 Light Side, 3 Light Side * 2
    dice_types["Force"] = dice(["BN", "BN", "BN", "BN", "BN", "BB", "LN", "LN","LN", "LL", "LL", "LL"]) 

    def press_roll(self, button):
        success = 0
        advantage = 0
        triumph = 0
        despair = 0
        light_points = 0
        dark_points = 0
        force = False
        
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
                        case "B":
                            dark_points += 1
                            force = True
                        case "L":
                            light_points += 1
                            force = True
                        case "N":
                            pass
        
        self.ids.results_label.text = f"{generate_roll_result(success, advantage, triumph, despair, light_points, dark_points, force)}"

    def press_mod_dice(self, dice, mod):
        for k,v in MyLayout.dice_types.items():
            if dice == k:
                v.count = adjust_value(int(v.count), mod, 0, 5)
                for widget_id, widget_instance in self.ids.items():
                    if k.lower() in widget_id.lower():
                        new_text = ""
                        for i in range(v.count):
                            if k == "Yellow" or k == "Red" or k == "Force":
                                new_text = new_text + "0"
                            if k == "Green" or k == "Purple":
                                new_text = new_text + "^"
                            if k == "Blue" or k == "Black":
                                new_text = new_text + "o"
                        widget_instance.text = f"{new_text}" 
    

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

def generate_roll_result(success, advantage, triumph, despair, light_points, dark_points, force):
    roll_result = "" 
    if success > 0:
        roll_result += f"successes: {success}\n"
    elif success < 0:
        roll_result += f"failures: {success * -1}\n "
    if advantage > 0:
        roll_result += f"advantage: {advantage}\n "
    elif advantage < 0:
        roll_result += f"threat: {advantage * -1}\n"
    if triumph > 0:
        roll_result += f"triumphs: {triumph}\n"
    if despair > 0:
        roll_result += f"despairs: {despair}\n"
    if force == True:
        roll_result += f"Force Points: {light_points} Light / {dark_points} Dark"
    return roll_result

if __name__ == "__main__":
    DiceRollerApp().run()
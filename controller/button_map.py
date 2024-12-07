from os import system

AXES = {
    0:"LSX",
    1:"LSY",
    2:"RSX",
    3:"RSY",
    4:"LT",
    5:"RT"
}

BUTTONS = {
    0:"A",
    1:"B",
    3:"X",
    4:"Y",
    6:"LB",
    7:"RB",
    10:"SL",
    11:"ST",
    12:"HM",
    13:"RS",
    14:"LS",
    15:"EX"
}

def button_test(controller):
    for button_index in range(controller.get_numbuttons()):
        if controller.get_button(button_index):
            button_name = BUTTONS.get(button_index, f"Button {button_index}")
            print(f"{button_name} pressed.")
    return

def axes_test(controller):
    for axis_index in range(controller.get_numaxes()):
        axis_value = controller.get_axis(axis_index)
        if abs(axis_value) > 0.15:
            axis_name = AXES.get(axis_index, f"Axis {axis_index}")
            print(f"{axis_name} at {axis_value:.2f}")
    return
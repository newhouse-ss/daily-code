color_rgb = {'Red':(255, 0, 0), 'Green':(0, 255, 0), 'Blue':(0, 0, 255)}

def rgb_to_color(tp, list):
    for key in list:
        if tp == list[key]:
            return key
    return 'no such color.'
print(rgb_to_color((0, 255, 0), color_rgb))

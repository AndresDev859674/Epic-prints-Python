import sys
import time
import os

def animation_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  
    sys.stdout.write('\b' * len(message))  
    sys.stdout.flush()

def color_print(message, color):
    colors = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    
    if color not in colors:
        raise ValueError("Color no válido")
    
    sys.stdout.write(colors[color])
    
    print(message)
    
    sys.stdout.write(colors['reset'])

color_print("red", 'red')
color_print("blue", 'blue')
color_print("green", 'green')
color_print("yellow", 'yellow')
animation_print('¡Hello!')
print('¡Hello!')

os.system('pause')

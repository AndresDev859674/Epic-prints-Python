# Epic-prints-Python
The Best Python Prints!

# Color Print
These Are Message Colors.
That You Can Put an Easy Color Message

```python
import sys

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

````
And now with this put in your code. use this code to be able to put the color in your message

```python
color_print("This message will be printed in red", 'red')
color_print("This message will be printed in blue", 'blue')
color_print("This message will be printed in green", 'green')
color_print("This message will be printed in yellow", 'yellow')
````

You can put any color you want for example.

```python

         'reset': '\033[0m',
         'black': '\033[30m',
         'network': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'magenta': '\033[35m',
         'cyan': '\033[36m',
         'white': '\033[37m'
````
copy the color you want for example

```python
color_print("This message will be printed in cyan'", 'cyan'')
````

# Animation Print
Animation in your Python Message

```python
def animation_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  
    sys.stdout.write('\b' * len(message))  
    sys.stdout.flush()
````
Now To put the Message put

```python
animation print('Hello!')
````

# Complete Example

```python
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
````

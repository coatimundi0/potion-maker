from random import randrange 
from random import randint

'''
Colors
    The liquid inside the container is [COLOR].
'''
colorshift = "a shimmering color-shift, like oil"
rainbow = "a beautiful, never-mixing rainbow"
clear = "clear"

colors = [clear, "pink", "hot pink", "red", "blood red", "orange", "metallic bronze", "blinding orange", "neon yellow", "pale yellow", "yellow", "true green", "forest green", "pale green", "blue", "dark blue", "midnight blue", "indigo", "violet", "night sky purple", "fuschia", "milky white", "metallic silver", "dirty brown", "soft brown", "inky black", "tinted red", "tinted orange", "tinted yellow", "tinted green", "tinted blue", "tinted purple", colorshift, rainbow]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
def determineColors(form):
    ### PICK MAIN COLOR
    color1 = colors[randrange(0, len(colors)-1)] 
    secondary_color = randint(0, 100)
    color2 = colors[randrange(1, len(colors)-1)]

    if color1 == color2:
        # SAME COLOR
        #print("SAME")
        num_colors = 1
    elif color1 != color2:
        # DIFFERENT COLORS
        num_colors = 2
    else:
        print("determineColors ERROR 1")
        return -1
    
    final = [color1, color2, secondary_color, num_colors]

    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
    if form == 0:
        phrase = liquidColor(final)
    elif form == 1:
        phrase = powderColor(final)
    elif form == 2:
        phrase = pasteColor(final)
    elif form == 3:
        phrase = gelColor(final)
    else:
        print("determineColors ERROR 2")
        return -1

    return phrase

def liquidColor(final):
    color1 = final[0]
    color2 = final[1]
    secondary_color = final[2]
    num_colors = final[3]
    phrase = "The liquid inside the container is " + color1 + "." 
    
        # ONE COLOR
    if (0 <= secondary_color <= 84) or (color1 == colorshift) or (color1 == rainbow) or (color2 == clear) or (num_colors == 1):
        #print("SINGLE")
        return phrase
    
        # TWO COLORS
    elif (85 <= secondary_color <= 89) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The liquid inside the container is " + color1 + " with a few little flecks of " + color2 + ". Interesting color mix..."
    elif (90 <= secondary_color <= 94) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The liquid inside the container is " + color1 + " with additional swirls of " + color2 + ". The movement is a little mesmerizing."
    elif (95 <= secondary_color <= 100) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The liquid inside the container is " + color1 + " and " + color2 + ". The two colors are clearly separated and do not mix, even if you shake it."
    else:
        print("liquidColor ERROR")
        return -1
    
    return phrase

def powderColor(final):
    #print(final)

    color1 = final[0]
    color2 = final[1]
    secondary_color = final[2]
    num_colors = final[3]
    phrase = "Opening the container, you find that the powder inside is " + color1 + "."

        # ONE COLOR
    if (0 <= secondary_color <= 75) or (color1 == colorshift) or (color1 == rainbow) or (color2 == clear) or (num_colors == 1):
        #print("SINGLE")
        return phrase
    
        # TWO COLORS
    elif (76 <= secondary_color <= 100) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "Opening the container, you find that the powder inside is " + color1 + ". There are a few " + color2 + " bits in there, too."
    else:
        print("powderColor ERROR")
        return -1
    
    return phrase

def pasteColor(final):
    color1 = final[0]
    color2 = final[1]
    secondary_color = final[2]
    num_colors = final[3]
    phrase = "You can see that the paste is " + color1 + "."
    
        # ONE COLOR
    if (0 <= secondary_color <= 24) or (color1 == colorshift) or (color1 == rainbow) or (color2 == colorshift) or (num_colors == 1):
        #print("SINGLE")
        return phrase
    
        # TWO COLORS
    elif (25 <= secondary_color <= 49) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The paste inside the container is " + color1 + " with some swirls of " + color2 + "."
    elif (50 <= secondary_color <= 74) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The paste inside the container is " + color1 + " with a thin layer of a " + color2 + " top coating."
    elif (75 <= secondary_color <= 100) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The top half of the paste is " + color1 + " and the bottom half is " + color2 + ". Sucks that the colors will mix when you start using it."
    else:
        print("pasteColor ERROR")
        return -1
    
    return phrase

def gelColor(final):
    color1 = final[0]
    color2 = final[1]
    secondary_color = final[2]
    num_colors = final[3]
    phrase = "You can see that the gel is " + color1 + "."
    
        # ONE COLOR
    if (0 <= secondary_color <= 39) or (color1 == colorshift) or (color1 == rainbow) or (color2 == colorshift) or (color2 == rainbow) or (num_colors == 1):
        #print("SINGLE")
        return phrase
    
        # TWO COLORS
    elif (40 <= secondary_color <= 59) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The gel inside the container is " + color1 + " with a thin " + color2 + " top coat."
    elif (60 <= secondary_color <= 100) and (num_colors == 2):
        #print("DIFFERENT")
        phrase = "The gel is half " + color1 + " and half " + color2 + "."
    else:
        print("gelColor ERROR")
        return -1
    
    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
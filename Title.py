from random import randrange 
from random import randint
from Form import makeForm

'''
TITLE
    The label reads [TITLE] of [EFFECT].
    The label reads [EFFECT] [TITLE].
'''
liquid_title = ["Potion", "Elixir", "Draught", "Vial", "Philter", "Tonic", "Brew", "Ichor", "Juice", "Concoction"]
powder_title = ["Powder", "Particles", "Grains", "Talc", "Sprinkles", "Scatter", "Strew", "Dust", "Dredge", "Grind", "Crumble"]
paste_title = ["Paste", "Gum", "Glue", "Cement", "Pate", "Puree", "Spread"]
gel_title = ["Amalgam", "Gel", "Compound", "Mix", "Synthesis", "Bond", "Gum", "Goo"]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeTitle(form):
    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
    title_form = form[0]

    if title_form == 0:
        title = liquid_title
    elif title_form == 1:
        title = powder_title
    elif title_form == 2: 
        title = paste_title
    elif title_form == 3:
        title = gel_title        
    else: 
        print("makeTitle ERROR")
        return -1
    
    title = title[randrange(0, len(title)-1)]
    return title 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
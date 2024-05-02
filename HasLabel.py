from random import randrange 
from random import randint
from Containers import makeContainer

'''
LABEL 
    LEGIBLE   --> TITLE
    ILLEGIBLE --> NO_TITLE
'''
no_label = "It has no label."
rubbed = "It seems like there was writing on this label here, but it's been rubbed off."
faded = "It seems like there was writing on this label here, but it's faded beyond belief..."
blank = "There's a paper label glued to the container, but there's nothing on it."
bloody = "There's writing here, but it's stained by bloody fingerprints.Yikes."
symbols = "The writing is just a bunch of weird, nonsense symbols."
recipe = "There's no title on this label, but it does have a painfully detailed recipe if you unfold the paper..."
ingredients = "There's no title, but it does have an ingredient list. It's surprisingly short..."
invisible = "There's a thick, paper label hastily taped to the container, but there's nothing on it."

no_title = [no_label, rubbed, faded, blank, symbols, recipe, ingredients, invisible]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeLabel(container):
    label = bool(True)
    cont = container[1]
    phrase = ""

    # container :: INGESTIBLE (0); SPLASH (1); DROPLET (2); POWDER (3); OTHER (4)
    if (cont == 2):
        legible = randint(1,30)
        phrase = f"The label is a little too small to read. You'll need to look closer. (DC {legible})"

    elif (cont == 0) or (cont == 1) or (cont == 3) or (cont == 4):
        # legible :: YES (0-74); NO (75-100)
        legible = randint(0,99)

        if 0 <= legible <= 74:
            phrase = "Looks like there's a label on it..."
        elif 75 <= legible <= 99:
            illegible = no_title[randrange(0, len(no_title)-1)]
            phrase = illegible
            label = bool(False)
        else: 
            print("makeLabel ERROR LEGIBLE")
            return -1
        
    else: 
            print("makeLabel ERROR")
            return -1
    
    final = [phrase, label]
    return final

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

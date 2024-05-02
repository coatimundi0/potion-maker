from random import randrange 
from random import randint

'''
FORM
    Based on the container, it must be a liquid that [LIQUID].
    Looking closely, you're able to figure out that it is a powder that [POWDER].
    It's a [PASTE], so you know that the only useful way to use it is to smear it onto a target.
    It's a [GEL], so you know that the only useful way to use it is to rub it onto a target.
'''
    # LIQUID
ingestible = "is ingested by the user."
splash = "is used as a ranged attack at the target."
droplet = "is that is dripped onto a target."
liquid = [ingestible, splash, droplet]
    # POWDER
puff_powder = "is blown onto a target or area of effect."
sprinkle_powder = "is sprinkled onto a target or area of effect."
edible_powder = "is ingested by the user."
ingredient_powder = "is mixed into something to cause an effect."

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeForm():
    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
    form_type = randint(0, 3)
    edible = bool(False)

    if form_type == 0:
        form = [ingestible, splash, droplet]
        liquid = form[randrange(0, len(form)-1)]
        phrase = "Based on the container, this " + liquid
        if liquid == form[0]:
            edible = bool(True)
        else:
            pass
    elif form_type == 1:
        form = [edible_powder, puff_powder, sprinkle_powder, ingredient_powder]
        powder = form[randrange(0, len(form)-1)]
        phrase = "Looking closely, you can tell it " + powder
        if powder == form[0]:
            edible = bool(True)
        else:
            pass
    elif form_type == 2:
        phrase = "The only real way to use this is to smear it onto a target."
    elif form_type == 3:
        phrase = "The best way to use something like this is to rub it onto a target."
    else:
        print("makeForm ERROR")
        return -1

    final = [form_type, phrase, edible]
    return final
    
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
from random import randrange 
from random import randint

'''
FORM
    Based on the container, it must be a liquid that [LIQUID].
    Looking closely, you're able to figure out that it is a powder that [POWDER].
    It's a [PASTE], so you know that the only useful way to use it is to smear it onto a target.
    It's a [GEL], so you know that the only useful way to use it is to rub it onto a target.

    0        |   1        |   2       |   3         
    LIQUID   |   POWDER   |   PASTE   |   GEL        
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def make_form():
        # random form
    form_type = randint(0, 3)
        # is it edible?
    edible = bool(False)


        # LIQUID (0) ::: 
    if form_type == 0:
            # phrases to be used
        ingestible = "is ingested by the user."
        splash = "is used as a ranged attack at the target."
        droplet = "is that is dripped onto a target."
        form = [ingestible, splash, droplet]
        
            # determine the full phrase at random
        liquid = form[randrange(0, len(form)-1)]
        phrase = "Based on the container, this " + liquid

            # ingestible = true // otherwise = false
        if liquid == form[0]:
            edible = bool(True)
        else:
            pass


        # POWDER (1) :::
    elif form_type == 1:
            # phrases to be used
        puffPowder = "is blown onto a target or area of effect."
        sprinkePowder = "is sprinkled onto a target or area of effect."
        ediblePowder = "is ingested by the user."
        ingredientPowder = "is mixed into something to cause an effect."
        form = [ediblePowder, puffPowder, sprinkePowder, ingredientPowder]

            # determine the full phrase at random
        powder = form[randrange(0, len(form)-1)]
        phrase = "Just by looking, you can tell it " + powder

            # ingestible = true // otherwise, false
        if powder == form[0]:
            edible = bool(True)
        else:
            pass


        # PASTE (2) :::
    elif form_type == 2:
        phrase = "The only real way to use this is to smear it onto a target."


        # GEL (3) :::
    elif form_type == 3:
        phrase = "The best way to use something like this is to rub it onto a target."


        # ERROR :::
    else:
        print("make_form ERROR")
        return -1


        # returns: integer (0-3) / string / bool
    final = [form_type, phrase, edible]
    return final
    
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # DELETE LATER: for testing purposes
test = make_form()
#print(test[1])

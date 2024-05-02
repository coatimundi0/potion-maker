from random import randrange 
from random import randint

'''
CONTAINER
    The item you pick up is a [CONTAINER].
'''
# container :: INGESTIBLE (0); SPLASH (1); DROPLET (2); POWDER (3); OTHER (4)
ingestible_container = ["a conical, smooth glass", "a square glass bottle", "a leather waterskin", "a stone flask", "a steel metal thermos", "a shot bottle", "a capped horn",  "an ornate, decorated glass bottle", "a geometric diamond glass", "a translucent green wine bottle", "a translucent brown beer bottle", "a leather pouch", "a bone flask", "a twist-cap bottle"]
splash_container = ["a spray bottle", "a delicate, decorated clear bottle", "an inhaler", "a tear-shaped glass bottle", "a translucent green beer bottle", "a clear wine bottle", "a funky, star-shaped glass bottle", "a lightly cracked shot bottle", "a highly cracked bone flask"]
droplet_container = ["a glass syringe", "a medical vial", "a glass pipet", "a metal vial", "a tiny, plastic syringe", "a steel pipet"]
powder_container = ["a tightly tied bandana", "a carefully folded burlap cloth", "a closed glass tupperware", "a capped shot bottle", "a capped triangular flask", "a capped round flask"]
other_container = ["a circular container", "a square-shaped container", "a round bowl with a sticky covering"]

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

def makeContainer(form):
    container_type = form[0]
    
    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
    if container_type == 0:
        if form[2] == bool(True):
            container = ingestible_container
        else: 
            cont = randint(1, 2)
            if cont == 1:
                container = splash_container
            elif cont == 2:
                container = droplet_container
            else: 
                print("makeContainer ERROR DROPLET")
                return -1
    elif container_type == 1:
        container = powder_container
    elif (container_type == 2) or (container_type == 3):
        container = other_container
    else: 
        print("makeContainer ERROR")
        return -1

    container = container[randrange(0, len(container)-1)]
    phrase = "The item you pick up is " + container  + "."

    final = [phrase, container_type]
    return final

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

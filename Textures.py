from random import randrange 

'''
PRIMARY TEXTURE (POTION)
    It looks [TEXTURE].
'''

potion_texture = [ "thick and sludgy... yuck!", "thin and watery.", "airy and bubbly.", "bubbly... like soda...", "thick and slimey! It hurts going down!", "sooo viscous!", "sickly and oily. 10/10 wouldn't recommend.", "nice and milky.", "so light that it's almost gaseous. It feels like you didn't drink anything!", "silky smooth and easy to swallow.", "watery."]

powder_texture = ["a thin, fine powder, but not horrible.", "flaky and hard to swallow...", "like a bunch of little crystals. You try to chew and it doesn't really work. You have to swallow it whole.", "a bunch of fine crystals that instantly melt in your mouth.", "a fine powder. It melts when it touches the saliva in your mouth.", "crunchy! Kinda like chicken when it's fried... well, the skin, at least."]

other_texture = ["really sticky.", "runny and gross.", "snotty... ewww.", "acceptably sticky", "tacky and weird... you don't like it.", "gooey and doesn't really hold its shape.", "weirdly chalky, like it has a translucent powder on it!", "firm. The shape only dips where you touch it.", "jello-like and jiggly. When you move, it moves, too."]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeTexture(form):
    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
    if form == 0:
        phrase = potionTexture()
    elif form == 1:
        phrase = powderTexture()
    elif (form == 2) or (form == 3):
        phrase = otherTexture()
    else:
        print("makeTexture ERROR ")
        return -1
    
    return phrase

def potionTexture():
    ingesting = ["You swallow the liquid. It's ", "You bite the bullet and chug a serving. It's ", "When swallowed, the liquid is ", "It's "]

    verbiage = ingesting[randrange(0, len(ingesting)-1)]
    texture = potion_texture[randrange(0, len(potion_texture)-1)]
    phrase = verbiage + texture

    return phrase

def powderTexture(): 
    ingesting = ["You put the powder in your mouth. It's ", "You go ahead and munch on a serving. It's kind of ", "When swallowed, the powder is ", "The powder is "]

    verbiage = ingesting[randrange(0, len(ingesting)-1)]
    texture = powder_texture[randrange(0, len(powder_texture)-1)]
    phrase = verbiage + texture

    return phrase

def otherTexture():
    touching = ["You dip your fingers in. It feels ", "You go ahead and touch it. It's kind of ", "Against your fingers, it feels ", "It looks exactly like how it feels, and it feels ", "It's a little "]

    verbiage = touching[randrange(0, len(touching)-1)]
    texture = other_texture[randrange(0, len(other_texture)-1)]
    phrase = verbiage + texture

    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 